import psycopg2
import psycopg2.extras
import configparser
import os

#def getEvents(clubName):
    parser = configparser.ConfigParser()
    parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dbfile.ini'))

    con = psycopg2.connect(dbname=parser.get('postgres','dbname'),
    user=parser.get('postgres','user'),
    host=parser.get('postgres','host'),
    password= parser.get('postgres', 'password'))

    checkNamestatement = "SELECT * FROM clubevents WHERE name = %s"

    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(checkNamestatement,(clubName,))
    item = cur.fetchall()
    cur.close()
    con.close()
    return item
