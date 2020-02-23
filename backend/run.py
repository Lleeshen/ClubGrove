from flask import Flask, current_app, jsonify, render_template, request

from flask_cors import CORS
import os
import logging
from . import model
from . import customJson
LOG = logging.getLogger(__name__)

#config
logging.basicConfig(level=logging.DEBUG) #for logging
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

#Change this security purposes
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

@app.route('/db/view/<tableName>/<number>', methods=['GET'])
def viewdbrow(tableName, number):
  res = model.dbModel.viewRow(tableName,number)
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

@app.route('/api/getEvents',methods=['POST'])
def getEvent():
  clubName = request.get_json().get('nm','')
  res = model.dbModel.getEventfromClub(clubName)
  return jsonify(res)

@app.route('/api/getClubCategories',methods=['GET'])
def getCategories():
  res = model.dbModel.getClubKeywords()
  return jsonify(res)

@app.route('/api/getSearchedClubs',methods=['POST'])
def getSearchedClubs():
  searchTerm = request.get_json().get('searchTerm','')
  keyword = request.get_json().get('keyword','')
  sort = request.get_json().get('sort','')
  print(searchTerm,keyword,sort)
  res = model.dbModel.searchClub(searchTerm,keyword,sort)
  return jsonify("test")

@app.route('/api/getEvents2',methods=['GET'])
def getEvent2():
  app.logger.warn(request.args.to_dict())
  res = model.dbModel.getEventfromClub2(**request.args.to_dict())
  return jsonify(res)

@app.route('/',defaults={'path': ''},methods=['GET'])
@app.route('/<path:path>')
def home(path):
    return render_template('index.html')

if __name__ == '__main__':
  app.run('0.0.0.0')
