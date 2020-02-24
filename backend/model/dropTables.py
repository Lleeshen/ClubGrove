import psycopg2
from . import startdb as startdb

def dropTable():
  con = startdb.startdb()

  statements = (
    'DROP TABLE IF EXISTS clubevents',
    'DROP TABLE IF EXISTS advising',
    'DROP TABLE IF EXISTS leaders',
    'DROP TABLE IF EXISTS memberships',
    'DROP TABLE IF EXISTS requests',
    'DROP TABLE IF EXISTS interested',
    'DROP TABLE IF EXISTS events',
    'DROP TABLE IF EXISTS faculty',
    'DROP TABLE IF EXISTS keywords',
    'DROP TABLE IF EXISTS club',
    'DROP TABLE IF EXISTS student'
  )

  cur = con.cursor()
  for statement in statements:
    cur.execute(statement)
  cur.close()
  con.commit()
  con.close()
