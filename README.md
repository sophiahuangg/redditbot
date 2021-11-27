# Overview

In this homework assignment, I created five Reddit bots to spread information (true and false, but all nice information) about **Joe Biden**. I worked with madlibs to generate texts about Biden, and I learned how to use the PRAW library. I also created a sixth bot to play with the Markovify library. 

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

    len(comments)= 803
    len(top_level_comments)= 49
    len(replies)= 754
    len(valid_top_level_comments)= 30
    len(not_self_replies)= 754
    len(valid_replies)= 621
    ========================================
    valid_comments= 651
    ========================================
    
botanist77

    len(comments)= 545
    len(top_level_comments)= 59
    len(replies)= 486
    len(valid_top_level_comments)= 59
    len(not_self_replies)= 486
    len(valid_replies)= 486
    ========================================
    valid_comments= 545
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

    len(comments)= 774
    len(top_level_comments)= 8
    len(replies)= 766
    len(valid_top_level_comments)= 8
    len(not_self_replies)= 766
    len(valid_replies)= 766
    ========================================
    valid_comments= 774
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

**I only upvoted if the polarity was >0.1 and downvoted if the polarity was <-0.1**

This is a tid bit of what I saw in my terminal to help me keep track of the upvoting/downvoting:
    
    ========================================
    numsubupvoted= 25
    ========================================
    numcommentupvoted= 1943
    ========================================
    numsubdownvoted= 16
    ========================================
    numcommentdownvoted= 451
    ========================================

### Markovify Example 
    mark= That is the cynical attempt by political hacks like Karl Roves to distract us from corporate scandals and a homeland security program that involves more than double what most experts thought were possible.Most of those crowds.So, when I look out over this crowd today, I know that Saddam poses no imminent and direct threat to the emergence of the previous administration and extend it to have — or very few, if needed.We succeeded in what we set the date of August 31st — as well as overland routes, allowing for continued departure to those who want to come out.I’m the fourth President who has faced the issue of whether and when I look out over this crowd today, I know there is no deadline.

I used these two resources to learn more about Markovify:

1. [Library](https://github.com/jsvine/markovify)
2. [Generating Text with Markov Chains by Zach Whalen](https://www.youtube.com/watch?v=9TsuQz9lXis)

I used this [article](https://www.cnn.com/2021/11/26/politics/travel-restrictions-south-africa/index.html), this [article](https://www.whitehouse.gov/administration/president-biden/), this [speech](https://www.whitehouse.gov/briefing-room/speeches-remarks/2021/08/31/remarks-by-president-biden-on-the-end-of-the-war-in-afghanistan/), and this [transcript](https://www.npr.org/templates/story/story.php?storyId=99591469) for the Markovify portion of the homework.

## Score

I believe my score should be a 39/30

1. **+18 Points**: Completing each task in `bot.py` (6 tasks, 3 points each)
2. **+2 Points**: Creating this Github Repository
3. **+2 Points**: Getting at least 100 valid comments posted.
4. **+2 Points**: Getting at least 500 valid comments posted.
5. **+2 Points**: Created an "army" of 5 bots that are all posting similar comments. Each bot posted at least 500 valid comments to get this extra credit.
6. **+2 Points**: Making my bot create 200+ new submission posts instead of just new comments. I scanned the /r/liberal, /r/sharks, /r/peppapig, and /r/conspiracies subreddits.
7. **+2 Points**: My bot replies to the most highly upvoted comment in a thread that it hasn't already replied to.
8. **+4 Points**: I used the TextBlob sentiment analysis library to determine the sentiment of all posts that mentions my favorite candidate. If the comment/submission has positive sentiment, then I upvote it; if the comment/submission has a negative sentiment, then I downvote it. 
9. **+5 Points**: I used the Markovify library to generate the texts of my comments for my sixth bot. I set the `state_size=2` and generated five sentences per comment/reply.

