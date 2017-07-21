import os
import twitter
import sqlite3
import os,sys
sys.path.append(os.pardir)
from name import ACTION_TOKEN
from name import ACTION_SECRET
from name import CONSUMER_KEY
from name import CONSUMER_SECRET

auth = twitter.OAuth(ACTION_TOKEN,ACTION_SECRET,CONSUMER_KEY,CONSUMER_SECRET)

t_rest = twitter.Twitter(auth = auth)

dbname = '../../bot_lib.db'
conn = sqlite3.connect(dbname)
c = conn.cursor()

c.execute('select * from Library')
list = c.fetchall()

tweet = str(list[random.random(0,len(list))]) + "さの先輩"
t_rest.statuses.update(status = tweet)
