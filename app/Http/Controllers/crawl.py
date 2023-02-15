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
  
# printing the statuses
for status in statuses:
    print(status.user.id)
    
#def subNumbers(x, y):
  #  return (x-y)
 
# main code
#a = 90
#b = 50
 
# finding subtraction
#result = subNumbers(a, b)
 
# print statement
#print("subtraction of ", a, " and ", b, " is = ", result)