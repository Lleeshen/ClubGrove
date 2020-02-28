import psycopg2
import psycopg2.extras
from .. import startdb as startdb
import logging

LOG = logging.getLogger(__name__)

def addEvent(name,description,website,email, **kargs):
    con = startdb.startdb()

    SQLstatement = " INSERT INTO club VALUES (%s,%s,%s,%s) "

    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(SQLstatement,(name,description,website,email))
    cur.close()
    con.commit()
    con.close()
