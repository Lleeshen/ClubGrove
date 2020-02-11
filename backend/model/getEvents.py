import psycopg2
import psycopg2.extras
import configparser
import os

def getEventList(clubName):
    parser = configparser.ConfigParser()
    parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dbfile.ini'))

    con = psycopg2.connect(dbname=parser.get('postgres','dbname'),
    user=parser.get('postgres','user'),
    host=parser.get('postgres','host'),
    password= parser.get('postgres', 'password'))

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
