import psycopg2
import psycopg2.extras
import configparser
import os
from . import startdb as startdb

def clubSearch(searchTerm,keyword,sort):
  con = startdb.startdb()
  SQLstatement = "SELECT name, description, website, email FROM club WHERE name ILIKE %s"
  if(keyword):
    SQLstatement += " AND name in (SELECT name FROM clubkeywords WHERE keywords = %s)"
  SQLstatement += " ORDER BY name %s"
  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  if(keyword):
    cur.execute(SQLstatement,('%' + searchTerm + '%',keyword,sort,))
  else:
    cur.execute(SQLstatement,('%' + searchTerm + '%',sort))
  item = cur.fetchall()
  result = []
  column = [desc[0] for desc in cur.description]
  if (item != None):
    for cat in item:
      result.append(dict(zip(column,cat)))
  cur.close()
  con.close()
  print(result)
  return result
