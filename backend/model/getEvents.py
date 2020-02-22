import psycopg2
import psycopg2.extras
from . import startdb as startdb

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
    con = startdb.startdb()
    checkNamestatement = """
    SELECT name, description, place, starttime, endtime
        FROM events
    """
    if 'sort' in kwargs and kwargs['sort']:
        print('ok')
        checkNamestatement += " ORDER BY name DESC"
    else:
        checkNamestatement += " ORDER BY name ASC"
    
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(checkNamestatement)
    result = []
    item = cur.fetchall()
    column = [desc[0] for desc in cur.description]
    for row in item:
        result.append(dict(zip(column,row)))
    cur.close()
    con.close()
    print(result)
    return result
    

        





