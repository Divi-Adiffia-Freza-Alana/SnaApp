import tweepy
import sys

# Key & access tokens
api_key = '9pAXoBjMcZEcUGYJ2CtBehWwj'
apikey_secret = '8LLiGMBSGvC7a67DSchYOwC1gDLbyJz4yif5GCZn4T5x1LJrIB'
access_token = '1287879462038560768-bdl6HkZbL94gYz6oZmT8r3I3tFOMWX'
access_token_secret = 'sbJSnNwPPUaDa5rHgFvNietH6DtSrblwL2Lnfea9m2FyJ'

auth = tweepy.OAuthHandler(api_key, apikey_secret)
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth)

#ids=[1,2,3,4]
#users_count = len(sys.argv)
#id_ = sys.argv[1]
id_ = [1575631142719344645, 1575628337023631361, 1575520363261227008] 
#print(users_count)

  
statuses = api.lookup_statuses(id_, trim_user = True)

#for status in tweepy.Cursor(statuses,count=100).items(250):
#    print(status.id)
keywords = ['Tweepy', 'Tweeter']
listtweet=[]
for status in tweepy.Cursor(api.search_tweets,'@JadiJago Bank Jago',count=100 ).items(100):
    tweet_elem = {"Tweet": status.text,
              "Username": status.user.screen_name,
              "Jumlah Status": status.user.statuses_count,
              "Username Target": status.in_reply_to_screen_name,
              "Date": status.created_at,
              "Followers": status.user.followers_count,
              "Following": status.user.friends_count,
              "retweet": status.retweet_count,
              "fav": status.favorite_count
              }                      
    listtweet.append(tweet_elem)
print(listtweet)
  
# printing the statuses
#for status in statuses:
  #  print(status.user.id)
    
#def subNumbers(x, y):
  #  return (x-y)
 
# main code
#a = 90
#b = 50
 
# finding subtraction
#result = subNumbers(a, b)
 
# print statement
#print("subtraction of ", a, " and ", b, " is = ", result)