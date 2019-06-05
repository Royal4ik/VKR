def text_cleaner(text):
        #к нижнему регистру
        text = text.lower()
		
        #очистка текста от тегов, упоминаний, ссылок
        text = re.sub(r\"(?:@\\S*|#\\S*|http(?=.*://)\\S*)\", \"\", text)
		
		#обработка вопросительного и восклицательно знака
		text = re.sub(r\"!\", \" ! \", text)
        text = re.sub(r\"\\?\", \" ? \", text)
		
        #обработка смайликов
        [' '.join(w for w in text.split() if w not in smile)]
        text = re.sub(r\"\\)\", \" ) \", text)
        text = re.sub(r\"\\(\", \" ( \", text)
     
        text =' '.join(text.split())
        cleaned_text = ''
		for char in text:\n",
				if (char.isalpha()) or (char == ' ') or (char == '!') or (char == '?') or (char == '(') or (char == ')'):\n",
					cleaned_text += char\n"

        return cleaned_text
		
		
tweetCriteria = got.manager.TweetCriteria().setQuerySearch(event).setSince(toDate).
				setUntil(fromDate).setMaxTweets(countTweets).setLang('ru')
tweets = got.manager.TweetManager.getTweets(tweetCriteria)