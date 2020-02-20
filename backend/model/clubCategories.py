import psycopg2
import psycopg2.extras
import configparser
import os
from . import startdb as startdb

def getKeywords():
  con = startdb.startdb()
  SQLstatement = "SELECT keywords AS text, keywords AS value FROM keywords"
  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute(SQLstatement)
  item = cur.fetchall()
  result = []
  column = [desc[0] for desc in cur.description]
  if (item != None):
    for cat in item:
      result.append(dict(zip(column,cat)))
  cur.close()
  con.close()
  return result
