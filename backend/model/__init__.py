from createTables import createTable
from dropTables import dropTable

class db:
  def init(self):
    createTable()
  def reset(self):
    dropTable()


model = db()
model.init()
print('Add tables done')
model.reset()
print('Drop tables done')
