
import snscrape.modules.twitter as sntwitter
import sys

# Setting variables to be used belowmaxTweets = 1000000
# Creating list to append tweet data to
maxTweets=1000
tweets_list2 = []


for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{sys.argv[1]} OR {sys.argv[2]} OR {sys.argv[3]} OR {sys.argv[4]} lang:id since:{sys.argv[5]} until:{sys.argv[6]}').get_items()):
    if i>maxTweets:
    
      #print(tweets_list2) 
       # for x in tweets_list2:
        # print(x[0])
         print(tweets_list2)    #print(tweets_list2)   
         break
    #tweet_elem = {"Tweet": tweet.id}
 

    #tweets_list2.append([tweet.content, tweet.user.username, tweet.user.followersCount, tweet.user.friendsCount,tweet.inReplyToUser, tweet.date])#
    tweets_list2.append(tweet.id)  
 
   
    #for x in tweets_list2:
       # print(x)
     #   split = x.split("/")
     #   u = split[-1]
     #   print(u)
        #for list in x:#
                 #print(list[list])#
  
    


 