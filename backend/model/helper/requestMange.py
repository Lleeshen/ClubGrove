import psycopg2
import psycopg2.extras
import configparser
import os
import logging
from .. import startdb as startdb

LOG = logging.getLogger(__name__)
def view(clubName, section = "request", **kwargs):
  con = startdb.startdb()
  LOG.debug(kwargs)
  #note got this off a wiki Just grabs the primary key
  statement = "SELECT * FROM Requests WHERE name = %s"
  if 'user' in kwargs and kwargs['user']:
    statement = "SELECT * FROM Requests WHERE email = %s"
    LOG.debug(clubName)
  cur1 = con.cursor()
  cur1.execute(statement,(clubName,))
  item1 = cur1.fetchall()
  result = []
  column = [desc[0] for desc in cur1.description]
  for row in item1:
      result.append(dict(zip(column,row)))
  cur1.close()
  con.close()
  LOG.debug(item1)
  return result

def add(clubName, email):
  con = startdb.startdb()
  SQLstatement = " INSERT INTO requests VALUES (%s,%s) "
  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute(SQLstatement,(email, clubName))
  cur.close()
  con.commit()
  con.close()

def removeRM(clubName, email):
  con = startdb.startdb()
  SQLstatement = "Select * from leaders where name= %s and email = %s"
  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute(SQLstatement,(clubName, email))
  item = cur.fetchall()
  if len(item) > 0:
    cur.close()
    con.close()
    return
  SQLstatement = "DELETE from requests where name= %s and email = %s"
  cur.execute(SQLstatement,(clubName, email))
  SQLstatement = "DELETE from memberships where name= %s and email = %s"
  cur.execute(SQLstatement,(clubName, email))
  cur.close()
  con.commit()
  con.close()

def requestMange(clubName, email, isAccept, section = "request"):
  con = startdb.startdb()
  SQLstatement = "DELETE from requests where name= %s and email = %s"
  if section == "interested":
    SQLstatement= "DELETE from interested where name= %s and email = %s"
  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute(SQLstatement,(clubName, email))
  if isAccept:
    SQLstatement = "INSERT INTO memberships VALUES (%s,%s) "
    if section == "interested":
      SQLstatement= "INSERT INTO requests VALUES(%s,%s) on conflict do nothing"
    cur.execute(SQLstatement,(email, clubName))
  cur.close()
  con.commit()
  con.close()
  return

def addInterested(clubName, email):
  con = startdb.startdb()
  SQLstatement = " INSERT INTO interested VALUES (%s,%s) "
  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute(SQLstatement,(email, clubName))
  cur.close()
  con.commit()
  con.close()

def removeInterested(clubName, email):
  con = startdb.startdb()
  SQLstatement = "DELETE from interested where name= %s and email = %s"
  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute(SQLstatement,(clubName, email))
  cur.close()
  con.commit()
  con.close()