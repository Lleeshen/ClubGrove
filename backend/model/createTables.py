import psycopg2
import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dbfile.ini'))


con = psycopg2.connect(dbname=parser.get('postgres','dbname'),
  user=parser.get('postgres','user'),
  host=parser.get('postgres','host'),
  password= parser.get('postgres', 'password'))

cur = con.cursor()
cur.execute("create table student(email varchar(20) primary key not null, name varchar(20) not null, phone varchar(15))")
# item = cur.fetchall()
cur.close()
con.commit()
con.close()
