# Import libraries
import pandas as pda
import tweepy


# Key & access tokens
api_key = 'UbNgroGozzdORIHTPgPM6lsFA'
apikey_secret = 'jubXmREiLJOgsJ9OkH1xYugssxqhEO1g7H2uNG3gp4K5EA9NhW'
access_token = '1287879462038560768-AGePh1vkMPd5SovBWnfMOmke6SVajz'
access_token_secret = 'ru4tVeQnb3staMc0f0s64cI0hgfoxMl7XrrVk0krzzXij'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAAofhgEAAAAAn1NV8Er2dgYK1D7BLvOqG5Bq2A0%3DfmaHeWVxcE4zIBA0RKjB6nhIgcck2vpJbtUWQHMHARdSjb1aFt'

auth = tweepy.OAuthHandler(api_key, apikey_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open your text file/snscrape output
#tweet_url = pda.read_csv("Jago.txt",  encoding='utf-16',index_col=None, header=None, names=["links"])
#tweet_url.head()

#Extract the tweet_id using .split function
#af = lambda x: x["links"].split("/")[-1]
#tweet_url['id'] = tweet_url.apply(af, axis=1)
#tweet_url.head()

#convert our tweet_url Series into a list
#ids = tweet_url['id'].tolist()
ids=1575628337023631361


#Process the ids by batch or chunks.
#total_count = len(ids)
#chunks = (total_count - 1) // 100 + 1
newlist = []

for i,tweet in enumerate(api.lookup_statuses(ids, tweet_mode="extended")):
    
    print(list_of_tw_status)
exit
for status in list_of_tw_status:
    if status>list_of_tw_status.length():
        print(newlist)   
        break
    tweet_elem = {"Tweet": status.full_text,
                "Username": status.user.screen_name,
                    "Jumlah Status": status.user.statuses_count,
                    "Username Target": status.in_reply_to_screen_name,
                    "Date": status.created_at,
                    "Followers": status.user.followers_count,
                    "retweet": status.retweet_count,
                    "fav": status.favorite_count
                    }
    newlist.append([tweet_elem])


# Create another for loop to loop into our batches while processing 100 entries every loop
#for i in range(chunks):
 #   batch = ids[i*100:(i+1)*100]
  #  result = fetch_tw(batch)
