from dotenv import load_dotenv
from streamlit_option_menu import option_menu
from newsapi import NewsApiClient
from urllib.request import urlopen, Request
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import date
from datetime import timedelta
import pandas as pd


#API Key for newsAPIs
newsapi = NewsApiClient(api_key='INSERT API KEY HERE')

#NewsAPI funtion 
def sentiment(input):
            articles = []
            today = date.today()
            yesterday = today - timedelta(days = 10)
            for i in range(1,4,1):
                articles_page = newsapi.get_everything(
                        q=input,
                        #sources='abc-news-au, news-com-au',
                        sources='cnn, the-washington-post, fox-news,abc-news-au, news-com-au',
                        #domains='http://www.cnn.com,
                        from_param=yesterday,
                        to= today,
                        language='en',
                        sort_by='popularity')
                articles.extend(articles_page['articles'])
            df= pd.DataFrame(articles)
            df2=df.drop(["source","author","title","description","url","urlToImage"], axis=1)
            vader = SentimentIntensityAnalyzer()
            scores = df2['content'].apply(vader.polarity_scores).tolist()
            scores_df = pd.DataFrame(scores)
            df2 = df2.join(scores_df, rsuffix='_right')
            df2.rename(columns= {'publishedAt': 'Date'}, inplace = True)
            df2.rename(columns= {'content': 'News'}, inplace = True)
            df2['Date'] = pd.to_datetime(df2.Date).dt.date
            df3 = df2.sort_values(by='Date', ascending=True)
            sentiment_score_apple=df3['compound'].mean()
            return round(sentiment_score_apple,3)

#string manipulation for user interaction for news sentiment
def generate_sentiment(prompt):
            if "sentiment" in prompt.lower():
                if "apple" in prompt.lower():
                    message = "News sentiment score for Apple is " + str(sentiment("Apple"))
                elif "appl" in prompt.lower():
                    message = "News sentiment score for Apple is " + str(sentiment("Apple"))
            if "sentiment" in prompt.lower():
                if "conocoPhillips" in prompt.lower():
                    message = "News sentiment score for ConocoPhillips is " + str(sentiment("ConocoPhillips"))
            elif "cop" in prompt.lower():
                message = "News sentiment score for ConocoPhillips is " + str(sentiment("ConocoPhillips"))
            if "sentiment" in prompt.lower():
                if "google" in prompt.lower():
                    message = "News sentiment score for Google is " + str(sentiment("Google"))
            elif "googl" in prompt.lower():
                message = "News sentiment score for Google is " + str(sentiment("Google"))
            if "sentiment" in prompt.lower():
                if "bitcoin" in prompt.lower():
                    message = "News sentiment score for Bitcoin is " + str(sentiment("Bitcoin"))
            elif "BTC" in prompt.lower():
                message = "News sentiment score for Bitcoin is " + str(sentiment("Bitcoin"))
            if "sentiment" in prompt.lower():
                if "ether" in prompt.lower():
                    message = "News sentiment score for Ether is " + str(sentiment("Ethereum"))
            elif "ETH" in prompt.lower():
                message = "News sentiment score for Ether is " + str(sentiment("Ethereum"))
            else:
                message = "I didn't catch your command please try the correct command"
            return message
