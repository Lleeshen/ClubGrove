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
    ('test0@gmail.com','John Doe','1111111111') ,
    ('test1@gmail.com','John Doe','1111111112') 
    ON CONFLICT DO NOTHING
    """,
    """
    INSERT INTO club VALUES
    ('Test0','Test0',NULL,'k'),
    ('Test1','Test1','s','k') 
    ON CONFLICT DO NOTHING
    """,
    """
    INSERT INTO keywords VALUES(
      ('sports') 
    ) 
    ON CONFLICT DO NOTHING
    """,
    """
    INSERT INTO faculty VALUES(
      'a@gmail.com',
      'Davis Re'
    )
    ON CONFLICT DO NOTHING
    """,
    """
     INSERT INTO events VALUES(
      1,
      'CLub Club',
      '10:00:00',
      '12:00:00',
      'Benson',
      'Not Much'
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
