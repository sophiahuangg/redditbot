import praw
from textblob import TextBlob


reddit = praw.Reddit('bot5',user_agent='cs40')

goodphrase='biden' or 'joe'
numsubupvoted=0
numcommentupvoted=0
numsubdownvoted=0
numcommentdownvoted=0
subred = reddit.subreddit("BotTownGarden").hot(limit=None)

for post in subred:
    #print('post=',post)
    if goodphrase in post.title.lower():
        subcontent=TextBlob(str(post.title))
        #print('text.sentiment.polarity=',text.sentiment.polarity)
        if subcontent.sentiment.polarity > 0.1:
            post.upvote()
            numsubupvoted+=1
            print('submission upvoted=',post.title)
            print('numsubupvoted=',numsubupvoted)
        elif subcontent.sentiment.polarity < -0.1:
            post.downvote()
            numsubdownvoted+=1
            print('submission downvoted=',post.title)
            print('numsubdownvoted=',numsubdownvoted)
    post.comments.replace_more(limit=None)
    for reply in post.comments.list():
        text=TextBlob(str(reply.body))
        if goodphrase in reply.body.lower() and text.sentiment.polarity > 0.1:
            reply.upvote()
            print('comment upvoted=',reply.body)
            numcommentupvoted+=1
            print('numcommentupvoted=',numcommentupvoted)
        elif goodphrase in reply.body.lower() and text.sentiment.polarity < -0.1:
            reply.downvote()
            print('comment downvoted=',reply.body)
            numcommentdownvoted+=1
            print('numcommentdownvoted=',numcommentdownvoted)
        '''
        for comments in list(reply.replies):
            if goodphrase in comments.body.lower():
                text=TextBlob(str(comments.body))
                #print('text.sentiment.polarity=',text.sentiment.polarity)
                if text.sentiment.polarity > 0.05:
                    comments.upvote()
                    numupvoted+=1
                    #print('comment upvoted=',comments.body)
                    print('numupvoted=',numupvoted)
                elif text.sentiment.polarity <-0.05:
                    comments.downvote()
                    numdownvoted+=1
                    #print('comment downvoted=',comments.body)
                    print('numdownvoted=',numdownvoted)
        '''   
print('========================================')
print('========================================')
print("numsubupvoted=",numsubupvoted)
print('========================================')
print('numcommentupvoted=', numcommentupvoted)
print('========================================')
print('numsubdownvoted=', numsubdownvoted)
print('========================================')
print('numcommentdownvoted=', numcommentdownvoted)
print('========================================')
print('========================================')







'''
blob = TextBlob(text)
print(blob.sentiment.polarity)
'''



