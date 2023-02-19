
import snscrape.modules.twitter as sntwitter
import sys
import json

from datetime import datetime

now = datetime.now() # current date and time

# Setting variables to be used belowmaxTweets = 1000000
# Creating list to append tweet data to
maxTweets=100
tweets_list2 = []


for i,tweet in enumerate(sntwitter.TwitterSearchScraper('@JadiJago OR #BersamaKitaJago OR #SemuaJadiJago OR Bank Jago lang:id since:2022-09-01 until:2022-09-30').get_items()):
    if i>maxTweets:
    
      #print(tweets_list2) 
       # for x in tweets_list2:
        # print(x[0])
         #print(tweets_list2)    #print(tweets_list2)   
         break
    #tweet_elem = {"Tweet": tweet.id}
    
    if(tweet.inReplyToUser is None ) :
      replyuser='null'
    else:
      replyuser=tweet.inReplyToUser.username 
    tweet_elem = {"Tweet": tweet.rawContent,
              "Username": tweet.user.username,
              "Followers": tweet.user.followersCount,
              "Following": tweet.user.friendsCount,
              "Reply": replyuser,
              "Date":  tweet.date.strftime("%Y/%d/%m, %H:%M:%S")
              
              }
    #tweets_list2.append([tweet.content, tweet.user.username, tweet.user.followersCount, tweet.user.friendsCount,tweet.inReplyToUser, tweet.date])#
    tweets_list2.append(tweet_elem) 
    
    #print(type(tweet.inReplyToUser)) 

       # print(x)
     #   split = x.split("/")
     #   u = split[-1]
     #   print(u)
        #for list in x:#
                 #print(list[list])#
   
#x = tweets_list2[-1][2]
#print(type(x))
#print(x.username)
data = {"Data":tweets_list2
              }
jsondata = json.dumps(data, indent=4, sort_keys=True, default=str)
print(jsondata)
    


 