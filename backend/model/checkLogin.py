import psycopg2
import psycopg2.extras
import hashlib
from . import startdb as startdb

def checkLogin(username,password):
  con = startdb.startdb()
  checkLoginStatement = "SELECT email, isadmin FROM users WHERE email = %s AND password = %s"
  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute(checkLoginStatement,(username,hashlib.sha256(password.encode()).hexdigest()))
  result = []
  item = cur.fetchall()
  column = [desc[0] for desc in cur.description]
  for row in item:
      result.append(dict(zip(column,row)))
  cur.close()
  con.close()
  return result
