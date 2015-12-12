
from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
#conn = psycopg2.connect(database="postgres", user="postgres", host="localhost", port="5432")
#cur = conn.cursor()
#cur.execute('''CREATE DATABASE Tcount;''')
#conn.commit()
conn = psycopg2.connect(database="tcount", user="tali", password="pass", host="localhost", port="5432")
cur = conn.cursor()
#cur.execute('''DROP TABLE Tweet_wordcount;''')
#cur.execute('''CREATE TABLE Tweet_wordcount_1
#       (word TEXT PRIMARY KEY     NOT NULL,
#       count INT     NOT NULL);''')
conn.commit()
#conn.close()
class WordCounter(Bolt):

    cur = conn.cursor()
    def initialize(self, conf, ctx):
        self.counts = Counter()
       # self.redis = StrictRedis()

    def process(self, tup):
        word = tup.values[0]
        self.counts[word] += 1
        self.emit([word, self.counts[word]])
		# If the word doesn't exist in table insert it otherwise update the table with the new count
        if self.counts[word]==1:
             cur.execute("SELECT count from Tweetwordcount WHERE word=%s;",[word])
             conn.commit()
             number=cur.fetchone()
             if number==None:
                  cur.execute("INSERT INTO tweetwordcount(word, count) VALUES(%s,%s)", (word, 1))
                  conn.commit()
        else:
            cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (self.counts[word], word));
            conn.commit()
        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
