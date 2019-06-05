import sys
import re # importing regex
import string
from viewer import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from textblob import TextBlob
from polyglot.text import Text as T
import indicoio
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import csv
from PyQt5.QtGui import QPixmap
import pickle as cPickle
from sklearn_deltatfidf import DeltaTfidfVectorizer
import json
import math
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas
from sklearn.model_selection import train_test_split
from operator import attrgetter
import MySQLdb
import string
import time


if sys.version_info[0] < 3:
    import got
else:
    import got3 as got



class MyWin(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		global vect_loaded
		global cls_loaded
		with open('my_vectorizer.pkl', 'rb') as vect:
			vect_loaded = cPickle.load(vect)
		with open('my_classifier.pkl', 'rb') as cls:
			cls_loaded = cPickle.load(cls)	
		self.ui.fromD.setDate(QtCore.QDate.currentDate());
		self.ui.toD.setDate(QtCore.QDate.currentDate());
		self.ui.tableRes.setColumnCount(4)
		self.ui.tableRes.setHorizontalHeaderLabels(('Лайки', 'RT','Тональность', 'Текст'))
		indicoio.config.api_key = '0e59207bf94b327fb89596fb721e3de3'
		self.ui.find.clicked.connect(self.analysis)
		
		db = MySQLdb.connect(host="localhost", user="Artem", passwd="123", db="contacts", charset='utf8')
		cursor = db.cursor()
		 

		f = open("log", "r")
		lines = f.readlines()
		 
		for line in lines:
			if string.find(line, "@") > -1:
				fname, fmail, fadres, ftel = unpack_line(line)
				sql = """INSERT INTO contacts(text, sentiment, like, rt)
				VALUES ('%(text)s', '%(sentiment)s', '%(like)s', '%(rt)s')
				"""%{"text":ftext, "sentiment":fsentiment, "like":flike, "rt":frt}
				cursor.execute(sql)
				db.commit()
		 
		db.close()
		f.close()
		
		
	def analysis(self):

		def clean_tweet(text):
			
			text = text.lower()
			#очистка текста от тегов, упоминаний, ссылок
			text = re.sub(r'^rt[\s]+', '', text)
			text = re.sub(r"(?:@\S*|#\S*|http(?=.*://)\S*)", "", text)
			#обработка смайлов
			text = re.sub(r"\)", " ) ", text)
			text = re.sub(r"\(", " ( ", text)
			
			text = re.sub(r"!", " ! ", text)
			text = re.sub(r"\?", " ? ", text)

			text =' '.join(text.split())
			
			cleaned_text = ''
			
			for char in text:
					if (char.isalpha()) or (char == ' ') or (char == '!') or (char == '?') or (char == '(') or (char == ')'):
						cleaned_text += char
			
			return cleaned_text
		
		def get_tweet_sentiment(tweet):
			texts = [clean_tweet(tweet)]
			vec = vect_loaded.transform(texts)
			pred = cls_loaded.predict(vec)
			
			# get sentiment
			if pred[0] == 1:
				sentiment = 'positive'
			else:
				sentiment = 'negative'

			return sentiment

		def get_tweets_sentiment(tweets):
			texts = list(map(clean_tweet, tweets))
			vec = vect_loaded.transform(texts)
			pred = cls_loaded.predict(vec)

			return pred
			
		def get_processed_tweets(tweets):
			tweets_text = []
			for tweet in tweets:
				tweets_text.append(tweet.text)
			tw=get_tweets_sentiment(tweets_text)
			processed_tweets = []
			count=0
			
			for tweet in tweets:
				tweet_dict = {}
				tweet_dict['favorites'] = tweet.favorites
				tweet_dict['retweets'] = tweet.retweets
				if tw[count] == 1:
					tweet_dict['sentiment']  = 'positive'
				else:
					tweet_dict['sentiment']  = 'negative'

				tweet_dict['text'] = tweet.text 
				count = count + 1
				
				if (tweet.retweets > 0):
					if tweet_dict not in processed_tweets:
						processed_tweets.append(tweet_dict)						
				else:
					processed_tweets.append(tweet_dict)
						
			return processed_tweets
		
		def fill_table(tweets_with_s):
			row = 0
			tweets_with_sentiment = sorted(tweets_with_s, key=lambda d: d['favorites'], reverse=True)
			for tup in tweets_with_sentiment:
				col = 0
	 
				for k, v in tup.items():
					cellinfo = QTableWidgetItem(str(v))
					self.ui.tableRes.setItem(row, col, cellinfo)
					col += 1
	 
				row += 1
				if row > 15:
					break
		
		def calculate_percent(tweets_with_sentiment):
			positive_tweets = 0
			negative_tweets = 0
			for tweet in tweets_with_sentiment:
				if tweet['sentiment'] == 'positive':
					positive_tweets = positive_tweets + 1
				else:
					negative_tweets = negative_tweets + 1
			
			if len(tweets_with_sentiment) != 0:			
				positive_percent = 100 * positive_tweets / len(tweets_with_sentiment)
				negative_percent = 100 * negative_tweets / len(tweets_with_sentiment)
			else:
				negative_percent = 50
				positive_percent = 50
			print ('Postive Tweets  | Count: {} , Percent: {} %' . format(positive_tweets, positive_percent))
			print ('Negative Tweets | Count: {} , Percent: {} %' . format(negative_tweets, negative_percent))
			
			data_names = ['Негативные мнения', 'Позитивные мнения']
			data_values = [negative_percent, positive_percent]
			
			plt.title('Распределение мнений (%)')
			
			dpi = 80
			fig = plt.figure(dpi = dpi, figsize = (280 / dpi, 220 / dpi) )
			mpl.rcParams.update({'font.size': 9})

			xs = range(len(data_names))

			plt.pie( 
				data_values, autopct='%.1f', radius = 1.1,
				explode = [0.15] + [0 for _ in range(len(data_names) - 1)] )
			plt.legend(
				bbox_to_anchor = (-0.38, -0.08, 0.25, 0.25),
				loc = 'lower left', labels = data_names )
				
			self.ui.graphic = fig.savefig('pie.png')
			pixmap = QPixmap("pie.png")
			self.ui.graph.setPixmap(pixmap)
		
		event = str(self.ui.theme.text())
		
		if (len(str(self.ui.countTweets.text())) == 0):
			countTweets=100
		else:
			countTweets = int(self.ui.countTweets.text())
		
		if (self.ui.isUseData.isChecked()):
			fromDate=self.ui.toD.date().toString("yyyy-MM-dd")
			toDate=self.ui.fromD.date().toString("yyyy-MM-dd")
		else:
			toDate=QtCore.QDate.currentDate().toString("yyyy-MM-dd")
			fromDate=QtCore.QDate.currentDate().addMonths(-1).toString("yyyy-MM-dd")
		
		start_time = time.time()
		tweetCriteria = got.manager.TweetCriteria().setQuerySearch(event).setSince(fromDate).setUntil(toDate).setMaxTweets(countTweets).setLang('ru')	 
		tweets = got.manager.TweetManager.getTweets(tweetCriteria)
		print("--- %s seconds to Get Tweets---" % (time.time() - start_time))	
		
		start_time = time.time()
		tweets_with_sentiment = get_processed_tweets(tweets)
		print("--- %s seconds to Processed Tweets---" % (time.time() - start_time))	

		calculate_percent(tweets_with_sentiment)
		fill_table(tweets_with_sentiment)

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myapp = MyWin()
	myapp.show()
	sys.exit(app.exec_())