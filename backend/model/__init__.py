from . import createTables, dropTables

class db:
  def init(self):
    createTables.createTable()
  def reset(self):
    dropTables.dropTable()


dbModel = db()
# dbModel.init()
# print('Add tables done')
# model.reset()
#print('Drop tables done')
