import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id="XQpDA5IIwO8aBT31lLbtYQ",		 # your client id
							client_secret="sokOef6x-Irex_AfCMRC6XVbJB07jQ",	 # your client secret
							user_agent="CypherScraping")	 # your user agent


topics_dict = { "title":[], "score":[], "id":[], "url":[], "comms_num": [], "created": [], "body":[]}
for submission in reddit.subreddit('programming').hot(limit=None):
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)
#Creating a dataframe

df=pd.DataFrame(topics_dict)
print("The columns created are :  ",topics_dict.__len__())
#Fixing the date column
def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = df["created"].apply(get_date)
df = df.assign(timestamp = _timestamp)

# printing the dataframe in the console

print(df)

#saving the data in a csv file
#csvfile = df.to_csv("InvestingPosts.csv", index=False)
#print(csvfile)
