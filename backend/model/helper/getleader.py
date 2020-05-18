import psycopg2
import psycopg2.extras
import configparser
import os
import logging
from .. import startdb as startdb

LOG = logging.getLogger(__name__)
def view(user, **kwargs):
  result = []
  if 'name' in kwargs and kwargs['name']:
    con = startdb.startdb()
    LOG.debug(kwargs)
    statement = "SELECT Count(*) FROM leaders WHERE name = %s and email = %s"
    cur1 = con.cursor()
    cur1.execute(statement,(kwargs['name'],user,))
    item1 = cur1.fetchall()
    column = [desc[0] for desc in cur1.description]
    for row in item1:
      result.append(dict(zip(column,row)))
    cur1.close()
    con.close()
    LOG.debug(item1)
  return result

def add(clubName, email):
  con = startdb.startdb()
  SQLstatement = " INSERT INTO leaders VALUES (%s,%s) "
  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute(SQLstatement,(email, clubName))
  cur.close()
  con.commit()
  con.close()

def remove(clubName, email):
  con = startdb.startdb()
  SQLstatement = "DELETE from leaders where name= %s and email = %s"
  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute(SQLstatement,(clubName, email))
  cur.close()
  con.commit()
  con.close()
