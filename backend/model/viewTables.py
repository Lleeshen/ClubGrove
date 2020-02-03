import psycopg2
import psycopg2.extras
import configparser
import os

def viewTable(tableName):
  parser = configparser.ConfigParser()
  parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dbfile.ini'))

  con = psycopg2.connect(dbname=parser.get('postgres','dbname'),
    user=parser.get('postgres','user'),
    host=parser.get('postgres','host'),
    password= parser.get('postgres', 'password'))

  checkNamestatement = "SELECT 1 FROM information_schema.tables WHERE table_schema = 'public' and table_name=%s LIMIT 1"

  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute(checkNamestatement,(tableName,))
  item = cur.fetchall()
  result = []
  if(len(item) == 0):
    result = 'No table ' + tableName
  else:
    statement = "SELECT *  FROM " + tableName
    cur1 = con.cursor()
    cur1.execute(statement)
    item1 = cur1.fetchall()
    column = [desc[0] for desc in cur1.description]
    for row in item1:
        result.append(dict(zip(column,row)))
    cur1.close()
  cur.close()
  con.close()
  return result
