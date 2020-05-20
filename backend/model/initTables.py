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
    ('Fun Club','','www.example.com','k'),
    ('Chinese Student Association',
    'The Chinese Student Association (CSA) aims to
    educate about diversity, as well as to support
    and encourage a further understanding of Chinese culture
    through social events and activities we provide to all
     students of Santa Clara University. CSA also promotes
     outreach to the Asian community through community
     service events.',NULL,'k'),
    ('The Forge Garden Club',
    'We promote a sustainable lifestyle in an urban setting through eating locally and enjoying the outdoors.',NULL,'k'),
    ('Commuter Student Union',
    'The Commuter Student Union serves as a centralized hub for commuters to link with one another,
    integrate into the student community and discuss important commuting-related issues.',NULL,'k'),
    ('Association for Computing Machinery',
    'ACM, the world''s largest educational and scientific computing society, delivers resources that advance computing as a
    science and a profession. ACM provides the computing field''s premier Digital Library and serves its members and the computing
    profession with leading-edge publications, conferences, and career resources.',NULL,'email'),
    ('Engineers Without Borders',
    'Our vision is a world in which the communities we serve have the capacity to sustainably meet their basic human needs, and that
    our members have enriched global perspectives through the innovative, professional, and educational opportunities in which we engage.',NULL,'email'),
    ('Psychology Club',
    'Psychology Club provides fun events and interesting faculty talks for students who are interested in psychology.',NULL,'email'),
    ('SCU Gaming Guild',
    'A relaxed, "kick-back" style of gaming club, where people can come in and play games, talk about games, and make new friends.',NULL,'email'),
    ('SCU Climbing', '',NULL,'email'),
    ('Innovator''s Student Union', '',NULL,'email'),
    ('Association of Transfer Students', 'The Association of Transfer Students aims to give transfer students a voice campus and help them feel connected',NULL,'email'),
    ('SCU Chess Club', 'To provide the Santa Clara student body with an organized venue to practice and learn the great game of chess.',NULL,'email'),
    ('Clara Craft Club', 'Provide an inclusive, stress-free environment for the community of Santa Clara University and to encourage creativity through
    Do-It-Yourself (DIY) arts and crafts projects. CCC will cater to member craft requests to foster an inclusive and communicative atmosphere.',NULL,'email'),
    ('History Club', 'The club aims to provide a social space beyond the classroom for students of all majors to share their passion for history and satisfy their
    curiosity about how the past can inform our understanding of the present.',NULL,'email'),
    ('Santa Clara University Mock Trail Team','Provide students with the opportunity to learn about the nature and process of litigation through a study of the federal rules of evidence,
    coaching from experienced lawyers, and simulated trial experiences (organized by the American Mock Trial Association).', NULL, 'email'),
    ('VRONCOS','To engage SCU students who are interested in various aspects of virtual reality, augmented reality, and mixed reality.', NULL, 'email')
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
      'Not Much ok'),(
      3,
      'Racing',
      '5:00:00',
      '10:00:00',
      'Benson',
      'Running in the 90s'),(
      4,
      'SSBM Tournament',
      '12:00:00',
      '14:00:00',
      'Benson',
      '4 stocks, No items on, Fox only, Final Destination'),(
      5,
      'Scavenger Hunt',
      '12:00:00',
      '14:00:00',
      'Benson',
      'I do not not want to collect eggs, they are trash- Animal Crossing'),(
      6,
      'Food Run',
      '17:00:00',
      '20:00:00',
      'Shappell Lounge',
      'Get food at Mitsuwa'
      ),(
      7,
      'Culture Show',
      '18:00:00',
      '21:00:00',
      'Locatelli Center',
      'Enjoy a skit and various dances related to Chinese Culture'
      )
    ON CONFLICT DO NOTHING
    """,
    """
    INSERT INTO interested VALUES(
      'test0@gmail.com',
      'Chinese Student Association'
    )
    ON CONFLICT DO NOTHING
    """,
    """
    INSERT INTO requests VALUES(
      'test0@gmail.com',
      'Fun Club'
    )
    ON CONFLICT DO NOTHING
    """,
    """
      INSERT INTO memberships VALUES(
      'test1@gmail.com',
      'Fun Club'
    ),
    (
      'test0@gmail.com',
      'SCU Chess Club'
    )
    ON CONFLICT DO NOTHING
    """,
    """
    INSERT INTO leaders VALUES(
      'test1@gmail.com','Chinese Student Association'
    ),
     ('test1@gmail.com','Fun Club')
    ON CONFLICT DO NOTHING
    """,
    """
    INSERT INTO advising VALUES(
      'a@gmail.com',
      'Chinese Student Association'
    )
    ON CONFLICT DO NOTHING
    """,
    """
    INSERT INTO clubevents VALUES(
     'Fun Club',
      1
    ),(
      'Chinese Student Association',
      6
    ),(
      'Chinese Student Association',
      7
    )
    ON CONFLICT DO NOTHING
    """,
    """
    INSERT INTO clubkeywords VALUES
    ('Fun Club','Sports')
    ON CONFLICT DO NOTHING
    """,
    #5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 is sha256 hash of password
    """
    INSERT INTO users VALUES
    ('llshen@scu.edu','5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',0),
    ('admin@scu.edu','5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',1),
    ('test0@gmail.com','5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',0),
    ('test1@gmail.com','5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',0)
    ON CONFLICT DO NOTHING
    """
  )

  cur = con.cursor()
  for statement in statements:
    cur.execute(statement)
  cur.close()
  con.commit()
  con.close()
