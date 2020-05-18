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

@bp.route('/getEvents3',methods=['POST'])
def getEvent3():
  clubName = request.get_json().get('nm','')
  res = model.dbModel.getEventfromClub3(clubName)
  return jsonify(res)

@bp.route('/getEvents2',methods=['GET'])
def getEvent2():
  current_app.logger.warn(request.args.to_dict())
  res = model.dbModel.getEventfromClub2(**request.args.to_dict())
  return jsonify(res)

@bp.route('/addClub',methods=['POST'])
def addClub():
  clubName = request.get_json().get('name','')
  clubDescription = request.get_json().get('description','')
  clubWebsite = request.get_json().get('website','')
  clubEmail = request.get_json().get('email','')
  model.dbModel.addClub(clubName,clubDescription,clubWebsite,clubEmail)
  return jsonify('success')

@bp.route('/deleteClub',methods=['POST'])
def deleteClub():
  clubName = request.get_json().get('name','')
  model.dbModel.deleteClub(clubName)
  return jsonify('success')