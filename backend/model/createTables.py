import psycopg2
import configparser
import os

def createTable():
  parser = configparser.ConfigParser()
  parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dbfile.ini'))

  con = psycopg2.connect(dbname=parser.get('postgres','dbname'),
    user=parser.get('postgres','user'),
    host=parser.get('postgres','host'),
    password= parser.get('postgres', 'password'))

  statements = (
    """
    CREATE TABLE IF NOT EXISTS student (
      email VARCHAR(20) PRIMARY KEY NOT NULL,
      name VARCHAR(20) NOT NULL,
      phone VARCHAR(15)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS club (
      name VARCHAR(30) PRIMARY KEY NOT NULL,
      description VARCHAR(150) NOT NULL,
      website varchar(30),
      email varchar(20) NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS keywords (
      keywords VARCHAR(20) PRIMARY KEY NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS faculty (
      email VARCHAR(20) PRIMARY KEY NOT NULL,
      name VARCHAR(20) NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS events (
      id INT PRIMARY KEY NOT NULL,
      name VARCHAR(20) NOT NULL,
      starttime TIME NOT NULL,
      endtime TIME NOT NULL,
      place VARCHAR(30) NOT NULL,
      description VARCHAR(50) NOT NULL
    )
    """
  )

  cur = con.cursor()
  for statement in statements:
    cur.execute(statement)
  cur.close()
  con.commit()
  con.close()
