from flask import (
  Flask, current_app, jsonify, render_template, 
  )
from flask_cors import CORS
import os
import logging
from . import customJson
from . import model
from .controller import (
  dbController, viewController,
  apiController)
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

app.register_blueprint(dbController.bp)
app.register_blueprint(viewController.bp)
app.register_blueprint(apiController.bp)

@app.route('/test', methods=['GET'])
def test():
  return jsonify('help!')

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
  return jsonify(res)

@app.route('/',defaults={'path': ''},methods=['GET'])
@app.route('/<path:path>')
def home(path):
    return render_template('index.html')

if __name__ == '__main__':
  app.run('0.0.0.0')
