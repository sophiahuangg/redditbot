# Overview

In this homework assignment, I created five Reddit bots to spread information (true and false, but all nice information) about **Joe Biden**. I worked with madlibs to generate texts about Biden. I learned how to use the PRAW library. The link to the homework assignment guidelines can be found [here!](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_04)

### Bot Names

My bot names are as follows:

- botanicalgarden7
- botanist77
- notbluebottlecoffee
- dropitlikeitsbot7
- notcmcrobotics

### Valid Comments

    len(comments)= 540
    len(top_level_comments)= 45
    len(replies)= 495
    len(valid_top_level_comments)= 39
    len(not_self_replies)= 493
    len(valid_replies)= 487
    ========================================
    valid_comments= 526
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
7. +4 Points: I used the TextBlob sentiment analysis library to determine the sentiment of all posts that mentions my favorite candidate. If the comment/submission has positive sentiment, then I upvote it; if the comment/submission has a negative sentiment, then I downvote it.

