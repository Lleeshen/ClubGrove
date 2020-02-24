from flask import (Blueprint, jsonify)
from .. import model

bp = Blueprint('dbController', __name__, url_prefix='/db')

@bp.route('/init', methods=['GET'])
def initdb():
  model.dbModel.init()
  return jsonify('Initialized database')

@bp.route('/reset', methods=['GET'])
def resetdb():
  model.dbModel.reset()
  return jsonify('Reset database')

@bp.route('/add', methods=['GET'])
def addVal():
  model.dbModel.insertValues()
  return jsonify('init table database values')

@bp.route('/clear', methods=['GET'])
def cleardb():
  model.dbModel.removeValues()
  return jsonify('Clear database values')