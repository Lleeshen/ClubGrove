import psycopg2
from .. import startdb as startdb

def clearTable():
  con = startdb.startdb()

  statements = (
    'DELETE FROM clubevents',
    'DELETE FROM advising',
    'DELETE FROM leaders',
    'DELETE FROM memberships',
    'DELETE FROM requests',
    'DELETE FROM interested',
    'DELETE FROM events',
    'DELETE FROM faculty',
    'DELETE FROM keywords',
    'DELETE FROM club',
    'DELETE FROM student'
  )

  cur = con.cursor()
  for statement in statements:
    cur.execute(statement)
  cur.close()
  con.commit()
  con.close()
