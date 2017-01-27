import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'djUkLNr3VGLlalc1Lm2bhbvsX'
consumer_secret= '2x1BRkinuf5PYWFpMz6XNXTnyMPQkGDZGR5mEYR7deEvpR7iPw'

access_token='802421486707470336-pu4rKk8QjmmgpC8A2QdvFaNqpvRF6kb'
access_token_secret='TeJqNRzCa4jXS7NsOliCrIoIh2NOQsFIArGERLPCjRSh4'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
search = input("Enter topic/event/person/interest: ")
public_tweets = api.search(search)
print("Results:")
print("Number of Tweets: " + str(len(public_tweets)))

for tweet in public_tweets: 
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    if  analysis.sentiment.polarity < 0:
        with open(search + '- Negative' +'.txt', 'a') as n:
            n.write(tweet.text)
    elif analysis.sentiment.polarity == 0:
        with open(search +'-Nuetral'+'.txt', 'a') as nn:
            nn.write(tweet.text)
    else:
        with open(search + '-Positive' + '.txt', 'a') as p:
            p.write(tweet.text)
            
