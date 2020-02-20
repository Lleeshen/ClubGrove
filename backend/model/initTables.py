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
    INSERT INTO keywords VALUES
      ('Sports') ,
      ('Culture')
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
    ON CONFLICT DO NOTHING
    """,
    """
    INSERT INTO interested VALUES(
      'test0@gmail.com',
      'Test0'
    )
    ON CONFLICT DO NOTHING
    """,
    """
    INSERT INTO requests VALUES(
      'test0@gmail.com',
      'Test0'
    )
    ON CONFLICT DO NOTHING
    """,
    """
      INSERT INTO memberships VALUES(
      'test1@gmail.com',
      'Test0'
    )
    ON CONFLICT DO NOTHING
    """,
    """
    INSERT INTO leaders VALUES(
      'test1@gmail.com','Test1'
    )
    ON CONFLICT DO NOTHING
    """,
    """
    INSERT INTO advising VALUES(
      'a@gmail.com',
      'Test0'
    )
    """,
    """
    INSERT INTO clubevents VALUES(
     'Test0',
      1
    )
    """
  )

  cur = con.cursor()
  for statement in statements:
    cur.execute(statement)
  cur.close()
  con.commit()
  con.close()
