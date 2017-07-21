import os
import twitter
import sqlite3
import os,sys
sys.path.append(os.pardir)
from name import ACCESS_TOKEN
from name import ACCESS_SECRET
from name import CONSUMER_KEY
from name import CONSUMER_SECRET

auth = twitter.OAuth(ACCESS_TOKEN,ACCESS_SECRET,CONSUMER_KEY,CONSUMER_SECRET)

t_rest = twitter.Twitter(auth = auth)

dbname = "../../bot_lib.db"
conn = sqlite3.connect(dbname)
c = conn.cursor()

c.execute("select * from Library")
lst = c.fetchall()

tweet = str(lst[random.random(0,len(lst))]) + "さの先輩"
t_rest.statuses.update(status = tweet)
