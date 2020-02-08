import psycopg2
import psycopg2.extras
import configparser
import os
from . import startdb as startdb

def viewRow(tableName,name):
  con = startdb.startdb()

  checkNamestatement = "SELECT 1 FROM information_schema.tables WHERE table_schema = 'public' and table_name=%s LIMIT 1"

  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute(checkNamestatement,(tableName,))
  item = cur.fetchall()
  result = []
  if(len(item) == 0):
    result = 'No table ' + tableName
  else:
    strname = str(name)
    statement = "SELECT *  FROM " + tableName +" WHERE name = %s"
    cur1 = con.cursor()
    cur1.execute(statement,(strname,))
    item1 = cur1.fetchone()
    column = [desc[0] for desc in cur1.description]
    if (item1 != None):
        result.append(dict(zip(column,item1)))
    cur1.close()
  cur.close()
  con.close()
  return result