import psycopg2
import configparser
import os

def initTable():
  parser = configparser.ConfigParser()
  parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dbfile.ini'))

  con = psycopg2.connect(dbname=parser.get('postgres','dbname'),
    user=parser.get('postgres','user'),
    host=parser.get('postgres','host'),
    password= parser.get('postgres', 'password'))

  statements = (
    """
    INSERT INTO student VALUES
    ('test0@gmail.com','John Doe','1111111111'),
    ('test1@gmail.com','John Doe','1111111112')
    """,
    """
    INSERT INTO club VALUES
    ('Test0','Test0',NULL,'k'),
    ('Test1','Test1','s','k')
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
    """,
    """
    CREATE TABLE IF NOT EXISTS interested (
      email VARCHAR(20) REFERENCES student(email),
      name VARCHAR(30) REFERENCES club(name),
      PRIMARY KEY (email, name)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS requests (
      email VARCHAR(20) REFERENCES student(email),
      name VARCHAR(30) REFERENCES club(name),
      PRIMARY KEY (email, name)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS memberships (
      email VARCHAR(20) REFERENCES student(email),
      name VARCHAR(30) REFERENCES club(name),
      PRIMARY KEY (email, name)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS leaders (
      email VARCHAR(20) REFERENCES student(email),
      name VARCHAR(30) REFERENCES club(name),
      PRIMARY KEY (email, name)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS advising (
      email VARCHAR(20) REFERENCES faculty(email),
      name VARCHAR(30) REFERENCES club(name),
      PRIMARY KEY (email, name)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS clubevents (
      name VARCHAR(30) REFERENCES club(name),
      id INT REFERENCES events(id),
      PRIMARY KEY (name, id)
    )
    """
  )

  cur = con.cursor()
  for statement in statements:
    cur.execute(statement)
  cur.close()
  con.commit()
  con.close()
