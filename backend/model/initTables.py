import psycopg2
from . import startdb as startdb

def initTable():
  con = startdb.startdb()

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
    ),(
      2,
      'CLub Club2',
      '1:00:00',
      '2:00:00',
      'Benson',
      'Not Much ok'
      ),(
        3,
        'Hello World',
        '3:00:00',
        '4:00:00',
        'Zoom',
        'Learn to Code'
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
    ON CONFLICT DO NOTHING
    """,
    """
    INSERT INTO clubevents VALUES(
     'Test0',
      1
    ),(
      'Test1',
      2
    ),(
      'Test1',
      3
    )
    ON CONFLICT DO NOTHING
    """,
    """
    INSERT INTO clubkeywords VALUES
    ('Test0','Sports')
    ON CONFLICT DO NOTHING
    """,
    #5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 is sha256 hash of password
    """
    INSERT INTO users VALUES
    ('llshen@scu.edu','5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',0),
    ('test1@gmail.com','5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',0),
    ('admin@scu.edu','5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',1)
    ON CONFLICT DO NOTHING
    """
  )

  cur = con.cursor()
  for statement in statements:
    cur.execute(statement)
  cur.close()
  con.commit()
  con.close()
