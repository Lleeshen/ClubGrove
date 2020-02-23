from . import viewTables, createTables, dropTables, initTables, clearTables, getEvents, viewSelection, clubCategories, clubSearch

class db:
  def init(self):
    createTables.createTable()
  def reset(self):
    dropTables.dropTable()
  def view(self,tableName):
    return viewTables.viewTable(tableName)
  def insertValues(self,**whateveryouwant):
    initTables.initTable()
  def removeValues(self):
    clearTables.clearTable()
  def getClubKeywords(selft):
    return clubCategories.getKeywords()
  def searchClub(self,searchTerm,keyword,sort):
    return clubSearch.clubSearch(searchTerm,keyword,sort)
  def getEventfromClub(self,clubName):
    return getEvents.getEventList(clubName)
  def viewRow(self, tableName, primaryId):
    return viewSelection.viewRow(tableName,primaryId)


dbModel = db()
# dbModel.init()
# print('Add tables done')
# model.reset()
#print('Drop tables done')
