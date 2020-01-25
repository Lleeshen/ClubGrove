import psycopg2
import configparser
import os

def dropTable():
  parser = configparser.ConfigParser()
  parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dbfile.ini'))

  con = psycopg2.connect(dbname=parser.get('postgres','dbname'),
    user=parser.get('postgres','user'),
    host=parser.get('postgres','host'),
    password= parser.get('postgres', 'password'))

  statements = (
    'DROP TABLE events'
    'DROP TABLE faculty',
    'DROP TABLE keywords'
    'DROP TABLE club',
    'DROP TABLE student'
  )

  cur = con.cursor()
  for statement in statements:
    cur.execute(statement)
  cur.close()
  con.commit()
  con.close()
