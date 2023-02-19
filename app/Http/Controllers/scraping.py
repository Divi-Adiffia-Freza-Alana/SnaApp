# Import libraries
import pandas as pda
import tweepy


# Key & access tokens
api_key = '9pAXoBjMcZEcUGYJ2CtBehWwj'
apikey_secret = '8LLiGMBSGvC7a67DSchYOwC1gDLbyJz4yif5GCZn4T5x1LJrIB'
access_token = '1287879462038560768-bdl6HkZbL94gYz6oZmT8r3I3tFOMWX'
access_token_secret = 'sbJSnNwPPUaDa5rHgFvNietH6DtSrblwL2Lnfea9m2FyJ'

auth = tweepy.OAuthHandler(api_key, apikey_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

ids= [1575631142719344645, 1575628337023631361, 1575520363261227008]

#Process the ids by batch or chunks.
total_count = len(ids)
chunks = (total_count - 1) // 100 + 1

def fetch_tw(ids):
    list_of_tw_status = api.lookup_statuses(ids, tweet_mode="extended")
    empty_data = pda.DataFrame()
    for status in list_of_tw_status:
        tweet_elem = {"Tweet": status.full_text,
                      "Username": status.user.screen_name,
                      "Jumlah Status": status.user.statuses_count,
                      "Username Target": status.in_reply_to_screen_name,
                      "Date": status.created_at,
                      "Followers": status.user.followers_count,
                      "Following": status.user.friends_count,
                      "retweet": status.retweet_count,
                      "fav": status.favorite_count
                      }
        empty_data = empty_data.append(tweet_elem, ignore_index=True)
    empty_data.to_csv("cobacoba.csv", mode="a")


# Create another for loop to loop into our batches while processing 100 entries every loop
for i in range(chunks):
    batch = ids[i*100:(i+1)*100]
    result = fetch_tw(batch)
