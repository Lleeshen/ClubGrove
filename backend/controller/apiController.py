from flask import (
    Blueprint, jsonify, current_app, request, session
)
from .. import model
import logging
LOG = logging.getLogger(__name__)

bp = Blueprint('apiController', __name__, url_prefix='/api')
#get events
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

@bp.route('/getLeader',methods=['GET'])
def getLeader():
  res = []
  LOG.debug(session)
  if 'username' in session:
    current_app.logger.warn(request.args.to_dict())
    res = model.dbModel.getLeader(session['username'], **request.args.to_dict())
    LOG.debug(res)
  return jsonify(res)

#managing clubs
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

#club requests
@bp.route('/generateClubRequest',methods=['POST'])
def requestGenerateClub():
  clubName = request.get_json().get('name','')
  email = request.get_json().get('email','')
  model.dbModel.generateRequest(clubName,email)
  return jsonify('success') 

@bp.route('/acceptClubRequest',methods=['POST'])
def requestAddClub():
  clubName = request.get_json().get('name','')
  email = request.get_json().get('email','')
  model.dbModel.acceptRequest(clubName,email)
  return jsonify('success')

@bp.route('/declineClubRequest',methods=['POST'])
def requestRemoveClub():
  clubName = request.get_json().get('name','')
  email = request.get_json().get('email','')
  model.dbModel.declineRequest(clubName, email)
  return jsonify('success')

@bp.route('/toRequest',methods=['POST'])
def interestedAddClub():
  LOG.debug("hey")
  clubName = request.get_json().get('name','')
  email = request.get_json().get('email','')
  model.dbModel.interestedtoRequested(clubName,email)
  return jsonify('success')

@bp.route('/notInterested',methods=['POST'])
def interestedRemoveClub():
  clubName = request.get_json().get('name','')
  email = request.get_json().get('email','')
  model.dbModel.notInterested(clubName, email)
  return jsonify('success')

