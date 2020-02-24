from flask import (Blueprint, jsonify, current_app
)
from .. import model

bp = Blueprint('viewController', __name__, url_prefix='/db/view')

@bp.route('/<tableName>', methods=['GET'])
def viewdb(tableName):
  res = model.dbModel.view(tableName)
  current_app.logger.warn(res)
  return jsonify(res)

@bp.route('/<tableName>/<number>', methods=['GET'])
def viewdbrow(tableName, number):
  res = model.dbModel.viewRow(tableName,number)
  current_app.logger.warn(res)
  return jsonify(res)