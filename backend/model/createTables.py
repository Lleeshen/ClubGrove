import psycopg2
from . import startdb as startdb


def createTable():
  con = startdb.startdb()

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
    """,
    """
    CREATE TABLE IF NOT EXISTS clubkeywords (
      name VARCHAR(30) REFERENCES club(name),
      keywords VARCHAR(20) REFERENCES keywords(keywords),
      PRIMARY KEY (name, keywords)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS users (
      email VARCHAR(20) PRIMARY KEY NOT NULL,
      password VARCHAR(64),
      isadmin INT
    )
    """
  )

  cur = con.cursor()
  for statement in statements:
    cur.execute(statement)
  cur.close()
  con.commit()
  con.close()
