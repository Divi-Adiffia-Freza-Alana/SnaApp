# Import libraries
import pandas as pda
import tweepy


# Key & access tokens
api_key = 'UbNgroGozzdORIHTPgPM6lsFA'
apikey_secret = 'jubXmREiLJOgsJ9OkH1xYugssxqhEO1g7H2uNG3gp4K5EA9NhW'
access_token = '1287879462038560768-AGePh1vkMPd5SovBWnfMOmke6SVajz'
access_token_secret = 'ru4tVeQnb3staMc0f0s64cI0hgfoxMl7XrrVk0krzzXij'

auth = tweepy.OAuthHandler(api_key, apikey_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open your text file/snscrape output
tweet_url = pda.read_csv("jago.txt",  encoding='utf-16',index_col=None, header=None, names=["links"])
tweet_url.head()


#Extract the tweet_id using .split function
af = lambda x: x["links"].split("/")[-1]
tweet_url['id'] = tweet_url.apply(af, axis=1)
tweet_url.head()

#convert our tweet_url Series into a list
ids = tweet_url['id'].tolist()

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
