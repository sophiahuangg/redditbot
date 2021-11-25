# Overview

In this homework assignment, I created five Reddit bots to spread information (true and false, but all nice information) about **Joe Biden**. I worked with madlibs to generate texts about Biden. I learned how to use the PRAW library. The link to the homework assignment guidelines can be found [here!](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_04)

### Bot Names

My bot names are as follows:

- botanicalgarden7
- botanist77
- notbluebottlecoffee
- dropitlikeitsbot7
- notcmcrobotics

#### Some of My Bots in Action!

Here is a [thread](https://old.reddit.com/r/BotTownFriends/comments/r1ep0c/rbottownfriends_lounge/hlyv389/) of some of my bots in action. I've also included a photo below. 

<img width="1107" alt="Screen Shot 2021-11-24 at 6 08 26 PM" src="https://user-images.githubusercontent.com/89934020/143365358-c77564a8-6022-4efb-8499-9efd50733750.png">



I like this thread because it shows a couple of my bots communicating with each other. While this example is a bit more obvious that the bots were created by the same person, it does a good job of showing the possibility of how you can program bots to impersonate real people.

### Valid Comments

botanicalgarden7

    len(comments)= 946
    len(top_level_comments)= 265
    len(replies)= 681
    len(valid_top_level_comments)= 160
    len(not_self_replies)= 680
    len(valid_replies)= 567
    ========================================
    valid_comments= 727
    ========================================
    
botanist77

    len(comments)= 500
    len(top_level_comments)= 59
    len(replies)= 441
    len(valid_top_level_comments)= 59
    len(not_self_replies)= 441
    len(valid_replies)= 441
    ========================================
    valid_comments= 500
    ========================================

notbluebottlecoffee

    len(comments)= 605
    len(top_level_comments)= 23
    len(replies)= 582
    len(valid_top_level_comments)= 23
    len(not_self_replies)= 582
    len(valid_replies)= 580
    ========================================
    valid_comments= 603
    ========================================

dropitlikeitsbot7

    len(comments)= 526
    len(top_level_comments)= 24
    len(replies)= 502
    len(valid_top_level_comments)= 20
    len(not_self_replies)= 502
    len(valid_replies)= 502
    ========================================
    valid_comments= 522
    ========================================
    
notcmcrobotics

    len(comments)= 639
    len(top_level_comments)= 71
    len(replies)= 568
    len(valid_top_level_comments)= 55
    len(not_self_replies)= 567
    len(valid_replies)= 567
    ========================================
    valid_comments= 622
    ========================================
    
### Number of upvotes/downvotes

## Score

I believe my score should be a /30

1. +18 Points: Completing each task in `bot.py` (6 tasks, 3 points each)
2. +2 Points: Creating this Github Repository
3. +2 Points: Getting at least 100 valid comments posted.
4. +2 Points: Getting at least 500 valid comments posted.
5. +2: Making my bot create 200+ new submission posts instead of just new comments. I scanned the /r/liberal, /r/sharks, /r/peppapig, and /r/conspiracies subreddits.
6. +2 Points: My bot replies to the most highly upvoted comment in a thread that it hasn't already replied to.
7. +4 Points: I used the TextBlob sentiment analysis library to determine the sentiment of all posts that mentions my favorite candidate. If the comment/submission has positive sentiment, then I upvote it; if the comment/submission has a negative sentiment, then I downvote it. (I only downvoted/upvoted if the polarity was <-0.05 or >0.05)

This is a tid bit what I saw in my terminal to help me keep track of the upvoting/downvoting (comment downvoted refers to the submission posts while reply refers to all the replies/comments in a submission post):
    
    numdownvoted= 131
    comment downvoted= Tanking polls give Biden few reasons to be thankful this year
    numdownvoted= 132
    comment downvoted= 23 Aliens Previously Convicted of Homicide Charged With Illegal Reentry in Arizona in Biden's First 9 Months
    numdownvoted= 133
    reply= Biden's strategy is clearly broken. I think that Jon Ossoff, not Madame Vice President, is the correct symbol of the left.
    numdownvoted= 134
    ========================================
    numdownvoted= 134
    ========================================
    numupvoted= 483

