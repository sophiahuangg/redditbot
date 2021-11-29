# Overview

In this homework assignment, I created six Reddit bots to spread information (true and false, but all nice information) about **Joe Biden**. I worked with madlibs to generate texts about Biden, and I learned how to use the PRAW library. I also created a sixth bot to play with the Markovify library. I posted in the subreddits /r/BotTown2, /r/BotTownFriends, and /r/BotTownGarden.

### Bot Names

My bot names are as follows:

- botanicalgarden7
- botanist77
- notbluebottlecoffee
- dropitlikeitsbot7
- notcmcrobotics
- botinayacht

#### Some of My Bots in Action!

Here is a [thread](https://old.reddit.com/r/BotTownGarden/comments/r3lsou/found_this_picture_in_a_usb_i_found/hmdiuhg/) of some of my bots in action using the Markovify library to generate texts.

<img width="1104" alt="Screen Shot 2021-11-28 at 12 00 28 PM" src="https://user-images.githubusercontent.com/89934020/143783953-f69edb6b-48d2-4a81-b6d1-2386852f2cdb.png">


I like this thread because it shows two of my bots communicating with each other. I also find it interesting that through using Markovify, sometimes you can tell that these aren't real people. But, to some outsider who isn't aware that we're completing this project for our computer science class, they could just think it's someone who made a lot of grammatical errors.

### Valid Comments

botanicalgarden7

    len(comments)= 804
    len(top_level_comments)= 49
    len(replies)= 755
    len(valid_top_level_comments)= 30
    len(not_self_replies)= 755
    len(valid_replies)= 622
    ========================================
    valid_comments= 652
    ========================================
    
botanist77

    len(comments)= 862
    len(top_level_comments)= 72
    len(replies)= 790
    len(valid_top_level_comments)= 72
    len(not_self_replies)= 790
    len(valid_replies)= 770
    ========================================
    valid_comments= 842
    ========================================

notbluebottlecoffee

    len(comments)= 795
    len(top_level_comments)= 29
    len(replies)= 766
    len(valid_top_level_comments)= 29
    len(not_self_replies)= 766
    len(valid_replies)= 764
    ========================================
    valid_comments= 793
    ========================================

dropitlikeitsbot7 (with Markovify)

    len(comments)= 997
    len(top_level_comments)= 41
    len(replies)= 956
    len(valid_top_level_comments)= 41
    len(not_self_replies)= 956
    len(valid_replies)= 952
    ========================================
    valid_comments= 993
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

botinayacht (with Markovify)

    len(comments)= 724
    len(top_level_comments)= 29
    len(replies)= 695
    len(valid_top_level_comments)= 29
    len(not_self_replies)= 695
    len(valid_replies)= 691
    ========================================
    valid_comments= 720
    ========================================

### Number of upvotes/downvotes

**I only upvoted if the polarity was >0.1 and downvoted if the polarity was <-0.1** I noticed that the Textblob sentiment analysis doesn't always behave ideally. By this, I mean that some comments that I expected to get downvoted were upvoted and vice versa. I decided to increase the threshold for downvoting/upvoting to account for some of this discrepancy. My thought was that if a post/comment has a polarity very close to zero, it is very hard to distinguish whether it is truly a negative, positive, or neutral sentiment. Therefore, I didn't want my bot to perform actions on posts/comments that had a polarity close to zero.

This is a tid bit of what I saw in my terminal to help me keep track of the upvoting/downvoting in /r/BotTownGarden:

    comment upvoted= Once Joe Biden becomes the president, he promises to give out complimentary ice cream sandwiches to everyone. He will deliver them to your house, so you don't have to wait in a line like you do at Collins. Who doesn't love Joe!
    numcommentupvoted= 1580
    ========================================
    ========================================
    numsubupvoted= 6
    ========================================
    numcommentupvoted= 1580
    ========================================
    numsubdownvoted= 4
    ========================================
    numcommentdownvoted= 44
    ========================================
    ========================================
    sophia@Sophias-MBP redditbot % 

### Markovify Examples

`state_size=2`

    mark= Now we must be with us to get them out if they so choose. We can join forces, stop the work ahead of us, we will get through this, together The world is watching today. And together, we shall write an American story of our servicemembers and dozens of innocent Afghans. Over the past few weeks — I had authorized 6,000 troops on the nation we know we can and we are this way, our country will be a cause for total war. We no longer in the shocking and stunning statistic that should have ended long ago.
    
`state_size=3`

    mark=  We face threats from al-Shabaab in Somalia; al Qaeda affiliates in Syria and Iraq, and establishing affiliates across Africa and Asia. I have just taken the sacred oath each of these moments, enough of us came together to carry all of us forward. We will honor them by becoming the people and nation we know we can and we must complete this mission, and we will. For weeks, they risked their lives to get American citizens, Afghans who helped us, and others taken to safety in the last 12 hours or so, another 7,000 have gotten out. For weeks, they risked their lives to get American citizens, Afghans who helped us, and others taken to safety in the last 11 days.
    
As I increased the state size, I also increased the number of tries it took to generate a sentence. I wanted my bot to imitate how Biden talks during his speeches.

I used these two resources to learn more about Markovify:

1. [Markovify Library](https://github.com/jsvine/markovify)
2. [Generating Text with Markov Chains by Zach Whalen](https://www.youtube.com/watch?v=9TsuQz9lXis)

I used [Biden's inaugural address](https://www.whitehouse.gov/briefing-room/speeches-remarks/2021/01/20/inaugural-address-by-president-joseph-r-biden-jr/), [Biden's remarks on Afghanistan](https://www.whitehouse.gov/briefing-room/speeches-remarks/2021/08/31/remarks-by-president-biden-on-the-end-of-the-war-in-afghanistan/), and [Biden's remarks on the terror attack at Hamid Karzai International Airport](https://www.whitehouse.gov/briefing-room/speeches-remarks/2021/08/26/remarks-by-president-biden-on-the-terror-attack-at-hamid-karzai-international-airport/) for the Markovify portion of the homework.

## Score

I believe my score should be a 39/30

### Completed:

1. **+18 Points**: Completing each task in `bot.py` (6 tasks, 3 points each)
2. **+2 Points**: Creating this Github Repository
3. **+2 Points**: Getting at least 100 valid comments posted.
4. **+2 Points**: Getting at least 500 valid comments posted.
5. **+2 Points**: Created an "army" of 5 bots that are all posting similar comments. Each bot posted at least 500 valid comments to get this extra credit.
6. **+2 Points**: Making my bot create 200+ new submission posts instead of just new comments. I scanned the /r/liberal, /r/sharks, /r/peppapig, and /r/conspiracies subreddits. These submission posts were posted into the /r/BotTown2, /r/BotTownGarden, and /r/BotTownFriends subreddits.
7. **+2 Points**: My bot replies to the most highly upvoted comment in a thread that it hasn't already replied to.
8. **+4 Points**: I used the TextBlob sentiment analysis library to determine the sentiment of all posts that mentions my favorite candidate. If the comment/submission has positive sentiment, then I upvote it; if the comment/submission has a negative sentiment, then I downvote it. 
9. **+5 Points**: I used the Markovify library to generate the texts of my comments for some of my bots. I generated five sentences per comment/reply.

### Not Completed

1.  Getting at least 1000 valid comments posted.
2.  Using GPT-2-Simple to generate text.

