import psycopg2
import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dbfile.ini'))


con = psycopg2.connect(dbname='testing', user='postgres',
        host='localhost', password= parser.get('postgres', 'password'))
cur = con.cursor()
cur.execute("insert into ok values (1, 't', 'stuff')")
cur.execute("select * from ok")
item = cur.fetchall()
print("connected.",item)
cur.close()
con.close()