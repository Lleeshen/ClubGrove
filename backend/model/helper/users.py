import psycopg2
import psycopg2.extras
from psycopg2 import sql
from urllib.parse import urlparse
from .. import startdb as startdb

def info(**kwargs):

    con = startdb.startdb()
    if 'name' not in kwargs: 
        return None
    checkNamestatement = """
    SELECT * from memberships where name = %s
    """
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(checkNamestatement,(kwargs['name'].lower(),))
    result = []
    item = cur.fetchall()

    column = [desc[0] for desc in cur.description]
    for row in item:
        result.append(dict(zip(column,row)))
    cur.close()
    con.close()
    return result