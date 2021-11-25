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

Here is a [thread!](https://old.reddit.com/r/BotTownGarden/comments/r1irrt/rbottowngarden_lounge/hlywdy2/) of some of my bots in action. I've also included a photo below. 


<img width="1128" alt="Screen Shot 2021-11-24 at 6 00 12 PM" src="https://user-images.githubusercontent.com/89934020/143364665-8f8c081e-3987-4eaf-a56b-cea200ba772a.png">

I like this thread because it shows a couple of my bots communicating with each other. While this example is a bit more obvious that the bots were created by the same person, it does a good job of showing the possibility of how you can program bots to impersonate real people.

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

