import twitter
import sqlite3
import json
import os,sys
import MeCab
sys.path.append(os.pardir)
from name import ACCESS_TOKEN
from name import ACCESS_SECRET
from name import CONSUMER_KEY
from name import CONSUMER_SECRET

if __name__ == "__main__":
	#データベースアクセス
	dbname = "../../bot_lib.db"
	conn = sqlite3.connect(dbname)
	c = conn.cursor()

	#twitter認証キーの設定
	auth = twitter.OAuth(ACCESS_TOKEN,ACCESS_SECRET,CONSUMER_KEY,CONSUMER_SECRET)

	#restにも認証を飛ばす
	t_rest = twitter.Twitter(auth = auth)

	#streming apiに認証を飛ばす
	t_stream = twitter.TwitterStream(auth = auth)

	#userstreamを取ってくる
	tweets = t_stream.userstream.user()

	for tweet in tweets:
    	#jsonをdictに変更
            texts = json.dumps(tweet)
            text_p = json.loads(texts)
            if text_p.get("text"):
                if text_p.find("さの先輩") and text_p["user_id"] != "自分のID": #さの先輩を含むツイートかどうか調べる
    			#以下ツイートした人にリプを返す
    			c.execute("select * from Library")
    			lst = c.fetchall()
    			reply = "@" + str(text_p["usr"]["screen_name"]) + " " + str(lst[random.random(0,len(lst))]) + "さの先輩"
    			t_rest.statuses.update(status = reply)
                else:
                    #ここに名詞を取り出してその中から一つ選ぶ処理を入れる

                    # choice_nouns #選ばれた名詞

                    #特徴ベクトルを基にNGワードかどうかをチェックする処理入れて

                    sql = "insert into Test_table values(?)"
                    c.execute(sql,choice_nouns)
                    conn.commit()
