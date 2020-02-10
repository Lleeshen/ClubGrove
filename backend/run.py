from flask import Flask, current_app, jsonify, render_template
from flask_cors import CORS
import os
import logging
from . import model
from . import customJson
LOG = logging.getLogger(__name__)

#config
DEBUG = True

app = Flask(__name__,template_folder='../dist',static_folder='../static')
app.config.from_object(__name__)

jinja_options = app.jinja_options.copy()
jinja_options.update(dict(
    variable_start_string='%%',
    variable_end_string='%%'
))
app.jinja_options = jinja_options
app.json_encoder = customJson.Custom_Jsonify

CORS(app,resources={r'/*': {'origins':'*'}})

@app.route('/db/init', methods=['GET'])
def initdb():
  model.dbModel.init()
  return jsonify('Initialized database')

@app.route('/db/reset', methods=['GET'])
def resetdb():
  model.dbModel.reset()
  return jsonify('Reset database')

@app.route('/db/view/<tableName>', methods=['GET'])
def viewdb(tableName):
  res = model.dbModel.view(tableName)
  app.logger.warn(res)
  return jsonify(res)

@app.route('/db/add', methods=['GET'])
def addVal():
  model.dbModel.insertValues()
  return jsonify('init table database values')

@app.route('/db/clear', methods=['GET'])
def cleardb():
  model.dbModel.removeValues()
  return jsonify('Clear database values')

@app.route('/test', methods=['GET'])
def test():
  return jsonify('help!')

@app.route('/api/getEvents/<clubName>',methods=['GET'])
def getEvent(clubName):
  res = model.dbModel.getEventfromClub(clubName)
  return jsonify(res)

@app.route('/',defaults={'path': ''},methods=['GET'])
@app.route('/<path:path>')
def home(path):
    return render_template('index.html')

if __name__ == '__main__':
  app.run('0.0.0.0')
