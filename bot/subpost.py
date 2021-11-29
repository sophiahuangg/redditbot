import praw
import time


reddit = praw.Reddit('bot',user_agent='cs40')

subred = reddit.subreddit("conspiracies").top(limit=250)
for post in subred:
    print('post title=',post.title)
    reddit.subreddit("BotTownGarden").submit(title=post.title, url=post.url)
    time.sleep(40)
