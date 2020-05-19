import psycopg2
import psycopg2.extras
import random
from .. import startdb as startdb

def addEvent(clubName, event):
  con = startdb.startdb()
  # Get used IDs
  listEventIdStatement = "SELECT id FROM events"
  cur = con.cursor()
  cur.execute(listEventIdStatement)
  eventIdList = cur.fetchall()
  cur.close()
  print(eventIdList)
  # Find a suitable ID
  newId = 0
  while(True):
    newId = random.randrange(0,2**31-1)
    for usedId in eventIdList:
      if(newId == usedId[0]):
        continue
    break
  print(newId)
  # Insert into clubevents and events table
  insertStatements = ("""
    INSERT INTO events VALUES
    (%s,%s,%s,%s,%s,%s)
  """,
  """
    INSERT INTO clubevents VALUES
    (%s, %s)
  """
  )
  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute(insertStatements[0],(newId,event['name'],event['starttime'],event['endtime'],event['place'],event['description']))
  cur.execute(insertStatements[1],(clubName,newId))
  cur.close()
  con.commit()
  con.close()

def deleteEvent(eventId):
  con = startdb.startdb()
  deleteStatements = ("""
  DELETE FROM clubevents
  WHERE id = %s
  """,
  """
  DELETE FROM events
  WHERE id = %s
  """
  )
  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  for statement in deleteStatements:
    cur.execute(statement,(eventId,))
  cur.close()
  con.commit()
  con.close()

def editEvent(eventId,event):
  con = startdb.startdb()
  editStatement = """
    UPDATE events
    SET name = %s, place = %s, description =  %s, starttime = %s, endtime = %s
    WHERE id = %s
  """
  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute(editStatement,(event['name'],event['place'],event['description'],event['starttime'],event['endtime'],eventId))
  cur.close()
  con.commit()
  con.close()