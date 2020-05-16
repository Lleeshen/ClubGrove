from . import createTables, dropTables, initTables, clearTables, clubCategories, clubSearch, checkLogin
from .helper import getEvents, viewSelection, viewTables, changeClubs, users, requestMange, getleader


class db:
  #db controls
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

  #Searching and events
  def searchClub(self,searchTerm,keyword,sort):
    return clubSearch.clubSearch(searchTerm,keyword,sort)
  def getEventfromClub(self,clubName, **kwargs):
    return getEvents.getEventList(clubName, **kwargs)
  def getEventfromClub2(self, **kwargs):
    return getEvents.getEventList2(**kwargs)
  def viewRow(self, tableName, primaryId):
    return viewSelection.viewRow(tableName,primaryId)

  #management
  def addClub(self,name,description,website,email,**kwargs):
      changeClubs.addClubs(name,description,website,email)
  def deleteClub(self,name,**kwargs):
      changeClubs.deleteClub(name)
  def checkLogin(self,username,password):
    return checkLogin.checkLogin(username,password)

  #interested and requests
  def generateRequest(self,clubName,email):
    return requestMange.add(clubName,email)
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
  
  #memeberships
  def viewMembership(self, clubname, email, **kwargs):
    return users.info(clubname, email, **kwargs)
  def requestOrMember(self, clubname, email, **kwargs):
    return users.requestOrMember(clubname, email, **kwargs)
  
  #leader information
  def getLeader(self, user, **kwargs):
    return getleader.view(user, **kwargs)

dbModel = db()
# dbModel.init()
# print('Add tables done')
# model.reset()
#print('Drop tables done')
