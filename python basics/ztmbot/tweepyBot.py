''' tweepy
'''
import tweepy
#consumer API keys and tokens from API keys and toekns section on developer.twitter
#access keys and token

auth=tweepy.OAuthHandler('ddS2W1DLjufyBgMCFrow7c5BP','ZXzFHzPcqALOYzhskblpWwPnBYmjz2zInvubOWG7NYp8SggZbY')
auth.set_access_token('730709785641803777-pOKLWVCcRLFqnntfRTsYWShpsnJ0amX','JySv2wzCP8Ku4zBGD4zCZLQ8gRhKRE78N8acTOy7HKf17')

api=tweepy.API(auth)
public_tweets=api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


#data