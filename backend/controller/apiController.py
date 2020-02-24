from flask import (
    Blueprint, jsonify, current_app, request
)
from .. import model

bp = Blueprint('apiController', __name__, url_prefix='/api')

@bp.route('/getEvents',methods=['POST'])
def getEvent():
  clubName = request.get_json().get('nm','')
  res = model.dbModel.getEventfromClub(clubName)
  return jsonify(res)

@bp.route('/getEvents2',methods=['GET'])
def getEvent2():
  current_app.logger.warn(request.args.to_dict())
  res = model.dbModel.getEventfromClub2(**request.args.to_dict())
  return jsonify(res)