import praw
import random
import datetime
import time

madlibs = [
    "Biden deemed '[READY] to successfully execute the [DUTIES] of the president' after first physical in office. Biden is now ready to [ROCK AND ROLL] and continue [SERVING] as the [PRESIDENT].",
    "Joe Biden is the [BEST] president because he can [COOK] an amazing [DINNER]. I heard that he tried out for [THIS TV SHOW] and is best friends with [A CELEBRITY]. For that reason, everyone should vote for Joe Biden. ",
    "Once Joe Biden becomes the president, he promises to give out [FREE] [FOOD] to [EVERYONE]. He will deliver them to your [DOORSTEP], so you don't have to wait in a line like you do at Collins. Who doesn't love [HIM]!",
    "Joe Biden is husband to [DR. JILL BIDEN], a proud father, and a [PROUD] grandfather. He [SAYS] that he is ready to build back better for all [PEOPLE]. His official [SOCIAL MEDIA] account is [POTUS].",
    "Joe Biden is [AMAZING]. Biden was born and raised in [STATE], moving with his family to New Castle County, Delaware in 1953 when he was [CHARACTERISTIC]. He studied at the University of Delaware before earning his [MAJOR] degree from [SCHOOL] University in 1968.",
    "Joe Biden is going to appoint [PERSON] as his [ROLE]. Together, they will implement great policies on [THIS] and [THAT]. They will improve our relations with different nations such as [COUNTRY]."
    ]

replacements = {
    'READY' : ['ready', 'excited', 'healthy','back and better','prepared'],
    'DUTIES': ['duties','responsibilities','burdens','job','role'],
    'ROCK AND ROLL':['rock and roll','kick butt','sit back','get back to business','go business mode'],
    'SERVING':['serving','fulfilling duties','petting dogs','creating memes','learning ballroom dancing'],
    'PRESIDENT':['president','46th president','president of the USA','husband of the First Lady','leader for the American people'],
    'BEST':['best','supreme','most wonderful','most iconic','greatest'],
    'COOK':['cook','whip up','chef up','concoct','create'],
    'DINNER':['dinner','meal','lunch without using Hello Fresh','homemade ratatouille'],
    'THIS TV SHOW':['The Bachelor','Bachelor in Paradise','Dancing With the Stars','Survivor','Too Hot to Handle'],
    'A CELEBRITY':['Tim Duncan','Gordon Ramsay','Awkwafina','Henry Golding','Jojo Siwa'],
    'FREE':['free','unlimited','discounted','tax free','complimentary'],
    'FOOD':['ice cream sandwiches','Goldfish crackers','pretzels','nacho cheese','guacamole'],
    'EVERYONE':['everyone','every single person','everybody','all of us','everyone, even people who love socks and sandals together'],
    'DOORSTEP':['doorstep','house','front porch','computer science professor','choice of destination'],
    'HIM':['him','Joe','Biden','Joe Biden','President Joe'],
    'DR. JILL BIDEN':['Dr. Jill Biden', 'Jill Biden', 'The First Lady','a wonderful woman','his high school sweetheart'],
    'PROUD':['proud','grateful','thankful','loving','funny'],
    'SAYS':['says','claims','promises','guarantees','writes in his senior thesis statement'],
    'SOCIAL MEDIA': ['social media','Instagram','Twitter','Facebook','LinkedIn'],
    'POTUS':['@POTUS','@dudewithsign','@officialpeppa','@houseofhighlights','@masterchefonfox'],
    'PEOPLE':['individuals','people','pets','iguanas','lovers of Peppa Pig'],
    'AMAZING':['amazing','fabulous','wonderful','magnificent','the best'],
    'STATE':['California','a pineapple under the sea','Hogwarts','Pennsylvania','the East Coast'],
    'CHARACTERISTIC':['seven','four','three','two','nine'],
    'MAJOR':['law','Bachelor\'s','Master\'s','PhD','Doctoral'],
    'SCHOOL':['Hogwarts','Stanford','Columbia','Harvard','Cornell'],
    'PERSON': ['Mike Izbicki','Kamala Harris','Jill Biden','Ash the Pokémon Trainer','Bill Nye the Science Guy'],
    'ROLE':['Vice President','yoga instructor','strategist','Press Secretary','Treasurer'],
    'THIS':['foreign relations','sustainability','urgent matters','important matters','pressing issues'],
    'THAT':['Fortnite','gaming','COVID','Coronavirus','COVID-19'],
    'COUNTRY':['New Zealand','China','South Korea','Costa Rica','The Fire Nation']

    
    }


def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.
    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.
    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''

    s=random.choice(madlibs)
    for k in replacements.keys():
        s=s.replace('['+k+']',random.choice(replacements[k]))
    return s

#bot replies to most highly upvoted comment
#need a function that inputs a comment and returns a comment’s score

def score(comment):
    scores=comment.score
    #print('comment.score=',comment.score)
    return scores

#upvoted=sorted(key=score,reverse=True)



# connect to reddit 
reddit = praw.Reddit('bot2',user_agent='cs40')


# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://old.reddit.com/r/BotTownGarden/comments/r3gaqm/chris_murphy_pence_walkout_a_multi_million_dollar/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    
    submission.comments.replace_more(limit=None)
    #all_comments = []
    all_comments=submission.comments.list()
    
    
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if str(comment.author)!='notbluebottlecoffee':
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented=', has_not_commented)
    

    
    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message

        text=generate_comment()
        submission.reply(text)
        time.sleep(1)
        pass
    
    
    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
       
        comments_without_replies = []
        for comment in not_my_comments:
            replied=False
            for reply in comment.replies:
                if str(reply.author)=='notbluebottlecoffee':
                    replied=True
            if replied==False:
                comments_without_replies.append(comment)
                
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        
        print('len(comments_without_replies)=',len(comments_without_replies))


        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message

        if len(comments_without_replies)>0:

            #comment=sorted(scores,key=score,reverse=True)
            try:
                #comment=random.choice(comments_without_replies)
                comment=sorted(comments_without_replies,key=lambda comments: comments.score,reverse=True)[0]
                comment.reply(generate_comment())
            except praw.exceptions.APIException:
                pass
            time.sleep(10)


    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    subreddit = reddit.subreddit("BotTownGarden")
    hot= list(subreddit.hot(limit=5))
    submission=random.choice(hot)
   
    
    pass

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(10)
