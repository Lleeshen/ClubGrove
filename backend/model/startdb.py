import psycopg2
import psycopg2.extras
import configparser
import os

def startdb():
  parser = configparser.ConfigParser()
  parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dbfile.ini'))

  con = psycopg2.connect(dbname=parser.get('postgres','dbname'),
    user=parser.get('postgres','user'),
    host=parser.get('postgres','host'),
    password= parser.get('postgres', 'password'))
  return con