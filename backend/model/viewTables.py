import psycopg2
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

  cur = con.cursor()
  cur.execute(checkNamestatement,(tableName,))
  item = cur.fetchall()
  if(len(item) == 0):
    result = 'No table ' + tableName
  else:
    statement = "SELECT * FROM " + tableName
    cur1 = con.cursor()
    cur1.execute(statement)
    item1 = cur1.fetchall()
    result = item1
    cur1.close()
  cur.close()
  con.close()
  return result
