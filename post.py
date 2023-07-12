
import praw
import pandas as pd
from praw.models import MoreComments
reddit_authorized = praw.Reddit(client_id="XQpDA5IIwO8aBT31lLbtYQ",		 # your client id
							client_secret="sokOef6x-Irex_AfCMRC6XVbJB07jQ",	 # your client secret
							user_agent="CypherScraping")	 # your user agent

name_subreddit = input("Enter the name of Sub-reddit : ")

subreddit = reddit_authorized.subreddit(name_subreddit)

#posts = subreddit.top(time_filter ="week")
#posts = subreddit.top(time_filter ="month")
posts = subreddit.top(time_filter ="year")
 
posts_dict = {"Title": [],
              "Total Comments": [],
              "Post URL": []}
 
for post in posts:
    posts_dict["Title"].append(post.title)
    posts_dict["Total Comments"].append(post.num_comments)
    posts_dict["Post URL"].append(post.url)
 
top_posts = pd.DataFrame(posts_dict)
 
print("Number of posts extracted : ",top_posts.shape[0])
print(top_posts.head())

#extract the best comments from the initial post 
url = top_posts['Post URL'][0]
submission = reddit_authorized.submission(url=url)
 
post_comments = []
for comment in submission.comments:
    if type(comment) == MoreComments:
        continue
    post_comments.append(comment.body)
 
comments_df = pd.DataFrame(post_comments, columns=['comment'])
 
print("Number of Comments : ",comments_df.shape[0])
comments_df.head()
