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
