from . import viewTables, createTables, dropTables, initTables, clearTables, viewSelection

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
  def viewRow(self, tableName, primaryId):
    return viewSelection.viewRow(tableName,primaryId)

dbModel = db()
# dbModel.init()
# print('Add tables done')
# model.reset()
#print('Drop tables done')
