import sys
import psycopg2

q = sys.argv
number=[0]
conn = psycopg2.connect(database="tcount", user="tali", password="pass", host="localhost", port="5432")
cur = conn.cursor()
if len(q) == 1:
  cur.execute("SELECT word, count from Tweetwordcount")
  conn.commit()
  s=cur.fetchall()
  print s
else:
   cur.execute("SELECT count from Tweetwordcount WHERE word=%s;",[q[1]])
   conn.commit()
   number=cur.fetchone()
   if number==None:
     s='Total number of occurences of'+repr(q[1])+': 0'
   else:
     s='Total number of occurences of'+repr(q[1])+':'+repr(number[0])

