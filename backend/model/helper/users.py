import psycopg2
import psycopg2.extras
from psycopg2 import sql
from urllib.parse import urlparse
from .. import startdb as startdb
import logging
LOG = logging.getLogger(__name__)

def info(clubname, email, **kwargs):
    con = startdb.startdb()
    checkNamestatement = """
    SELECT * from memberships where name = %s and email = %s
    """
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(checkNamestatement,(clubname, email,))
    result = []
    item = cur.fetchall()
    LOG.debug(item)
    column = [desc[0] for desc in cur.description]
    for row in item:
        result.append(dict(zip(column,row)))
    cur.close()
    con.close()
    LOG.debug(result)
    return result

def requestOrMember(clubname, email, **kwargs):
    con = startdb.startdb()
    checkNamestatement = """
    SELECT * from memberships where name = %s and email = %s
    Union 
    SELECT * from requests where name = %s and email = %s 
    """
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(checkNamestatement,(clubname, email,clubname, email,))
    result = []
    item = cur.fetchall()
    column = [desc[0] for desc in cur.description]
    for row in item:
        result.append(dict(zip(column,row)))
    cur.close()
    con.close()
    LOG.debug(result)
    return result