
import psycopg2
import sys

q=sys.argv
q2=q[1].split(',')

conn = psycopg2.connect(database="tcount", user="tali", password="pass", host="localhost", port="5432")

cur = conn.cursor()

cur.execute("SELECT word,count from Tweetwordcount WHERE count>=%s AND count<=%s",(q2[0],q2[1]))
conn.commit()
s=cur.fetchall()
print s