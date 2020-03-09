import psycopg2
import psycopg2.extras
import configparser
import os
from . import startdb as startdb

def add(clubName, email):
  con = startdb.startdb()
  SQLstatement = " INSERT INTO requests VALUES (%s,%s) "
  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute(SQLstatement,(clubName, email))
  cur.close()
  con.commit()
  con.close()
  return result

def remove(clubName, email):
  con = startdb.startdb()
  SQLstatement = "DELETE from requests where name= %s and email = %s"
  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute(SQLstatement,(clubName, email))
  cur.close()
  con.commit()
  con.close()
  return result