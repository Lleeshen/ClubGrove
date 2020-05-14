import psycopg2
import psycopg2.extras
from psycopg2 import sql
from .. import startdb as startdb
import logging

LOG = logging.getLogger(__name__)

def getEventList(clubName, **kargs):
    con = startdb.startdb()

    checkNamestatement = """
        SELECT name, description, place, starttime, endtime
        FROM events
        WHERE id IN (SELECT id
        FROM clubevents
        WHERE name = %s)
    """

    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(checkNamestatement,(clubName,))
    result = []
    item = cur.fetchall()
    column = [desc[0] for desc in cur.description]
    for row in item:
        result.append(dict(zip(column,row)))
    cur.close()
    con.close()
    print(result)
    return result

def getEventList2(**kwargs):
    #solve case insesnity
    con = startdb.startdb()
    checkNamestatement = """
    SELECT name, description, place, starttime, endtime
        FROM events
    """
    if 'event' in kwargs and not kwargs['event'] == 'null':
        checkNamestatement += 'Where name ILIKE %s'
    if 'sort' in kwargs and kwargs['sort'] == 'false' or kwargs['sort'] == 'None':
        checkNamestatement += " ORDER BY {table_name} DESC"
    else:
        checkNamestatement += " ORDER BY {table_name} ASC"
    
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    sqlState = sql.SQL("")
    if 'name' in kwargs and kwargs['name']:
        sqlState = sql.SQL(checkNamestatement).format(table_name = sql.Identifier(kwargs['name']))
    else:
        sqlState = sql.SQL(checkNamestatement).format(table_name = sql.Identifier('name'))
    if 'event' in kwargs:
        cur.execute(sqlState,('%' + kwargs['event'] + "%",))
        LOG.debug(sqlState)
    else:
        cur.execute(sqlState)
    result = []
    item = cur.fetchall()

    column = [desc[0] for desc in cur.description]
    for row in item:
        result.append(dict(zip(column,row)))
    cur.close()
    con.close()
    return result
    

        





