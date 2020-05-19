from flask import (Blueprint, jsonify, current_app, request
,session
)
from .. import model
import logging

LOG = logging.getLogger(__name__)
bp = Blueprint('viewController', __name__, url_prefix='/db/view')

@bp.route('/<tableName>', methods=['GET'])
def viewdb(tableName):
  res = model.dbModel.view(tableName, **request.args.to_dict())
  current_app.logger.warn(res)
  return jsonify(res)

@bp.route('/<tableName>/<number>', methods=['GET'])
def viewdbrow(tableName, number):
  res = None
  if (tableName == "requests"):
    res = model.dbModel.viewRow2(number, **request.args.to_dict())
  elif(tableName == "memberships"):
    if 'username' in session:

      res = model.dbModel.viewMembership(number, session['username'], **request.args.to_dict())
      LOG.debug(number + session['username'])
    else:
      return jsonify([])
  else:
    res = model.dbModel.viewRow(tableName,number)
  current_app.logger.warn(res)
  return jsonify(res)