import psycopg2
import configparser
import os

def clearTable():
  parser = configparser.ConfigParser()
  parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dbfile.ini'))

  con = psycopg2.connect(dbname=parser.get('postgres','dbname'),
    user=parser.get('postgres','user'),
    host=parser.get('postgres','host'),
    password= parser.get('postgres', 'password'))

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
