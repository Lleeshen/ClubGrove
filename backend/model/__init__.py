from . import createTables, dropTables, initTables, clearTables, clubCategories, clubSearch, checkLogin
from .helper import getEvents, viewSelection, viewTables, changeClubs, users, requestMange, getleader


class db:
  def init(self):
    createTables.createTable()
  def reset(self):
    dropTables.dropTable()
  def view(self,tableName, **kwargs):
    return viewTables.viewTable(tableName, **kwargs)
  def insertValues(self,**whateveryouwant):
    initTables.initTable()
  def removeValues(self):
    clearTables.clearTable()
  def getClubKeywords(self):
    return clubCategories.getKeywords()
  def searchClub(self,searchTerm,keyword,sort):
    return clubSearch.clubSearch(searchTerm,keyword,sort)
  def getEventfromClub(self,clubName, **kwargs):
    return getEvents.getEventList(clubName, **kwargs)
  def getEventfromClub2(self, **kwargs):
    return getEvents.getEventList2(**kwargs)
  def getEventfromClub3(self,clubName, **kwargs):
    return getEvents.getEventListWithID(clubName, **kwargs)
  def viewRow(self, tableName, primaryId):
    return viewSelection.viewRow(tableName,primaryId)
  def addClub(self,name,description,website,email,**kwargs):
      changeClubs.addClubs(name,description,website,email)
  def deleteClub(self,name,**kwargs):
      changeClubs.deleteClub(name)
  def checkLogin(self,username,password):
    return checkLogin.checkLogin(username,password)
  def loginLeader(self,clubLeader,clubName):
    return checkLogin.loginLeader(clubLeader,clubName)
  def acceptRequest(self,clubName,email):
    return requestMange.requestMange(clubName,email, True)
  def declineRequest(self,clubName,email):
    return requestMange.requestMange(clubName,email, False)
  def interestedtoRequested(self,clubName,email):
    return requestMange.requestMange(clubName,email, True, 'interested')
  def notInterested(self,clubName,email):
    return requestMange.requestMange(clubName,email, False, 'interested')
  def viewRow2(self, clubname, **kwargs):
    return requestMange.view(clubname, **kwargs)
  def getLeader(self, user, **kwargs):
    return getleader.view(user, **kwargs)

dbModel = db()
# dbModel.init()
# print('Add tables done')
# model.reset()
#print('Drop tables done')
