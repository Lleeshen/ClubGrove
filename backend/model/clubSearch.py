import psycopg2
import psycopg2.extras
import configparser
import os
from . import startdb as startdb
import logging
LOG = logging.getLogger(__name__)

def clubSearch(searchTerm,keyword,sort):
  con = startdb.startdb()
  LOG.debug(sort)
  SQLstatement = "SELECT name, description, website, email FROM club WHERE name ILIKE %s"
  if(keyword):
    SQLstatement += " AND name in (SELECT name FROM clubkeywords WHERE keywords = %s)"
  if sort=='ASC':
    SQLstatement += " ORDER BY name ASC"
  elif sort=='DESC':
    SQLstatement += " ORDER BY name DESC"
  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  if(keyword):
    cur.execute(SQLstatement,('%' + searchTerm + '%',keyword,))
  else:
    cur.execute(SQLstatement,('%' + searchTerm + '%',))
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

def clubSearchUser(searchTerm,keyword,sort, user, searchType):
  LOG.debug(user)
  con = startdb.startdb()
  if searchType != "Member":
    SQLstatement = """SELECT name, description, website, email FROM club WHERE name ILIKE %s
    AND name in (select name from memberships where email = %s
        union 
        select name from requests where email = %s
        union
        select name from interested where email = %s)"""
    if(keyword):
      SQLstatement += " AND name in (SELECT name FROM clubkeywords WHERE keywords = %s)"
    if sort=='ASC':
      SQLstatement += " ORDER BY name ASC"
    elif sort=='DESC':
      SQLstatement += " ORDER BY name DESC"
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if(keyword):
      cur.execute(SQLstatement,('%' + searchTerm + '%',user, user, user, keyword,))
    else:
      cur.execute(SQLstatement,('%' + searchTerm + '%',user, user, user,))
  else:
    SQLstatement = """SELECT name, description, website, email FROM club WHERE name ILIKE %s
    AND name in (select name from memberships where email = %s)"""
    if(keyword):
      SQLstatement += " AND name in (SELECT name FROM clubkeywords WHERE keywords = %s)"
    if sort=='ASC':
      SQLstatement += " ORDER BY name ASC"
    elif sort=='DESC':
      SQLstatement += " ORDER BY name DESC"
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if(keyword):
      cur.execute(SQLstatement,('%' + searchTerm + '%',user, keyword,))
    else:
      cur.execute(SQLstatement,('%' + searchTerm + '%',user,))
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