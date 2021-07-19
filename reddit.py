import praw
import random

reddit = praw.Reddit(
    client_id="8362eGvzJWKAjATcybac_w",
    client_secret="T-Lp0nn_iTaXryQ9-FKnXYDXvm5rjA",
    user_agent="windows:mood-tracker:v1.0.0 (by /u/QueenProtista)",
)
# BASE_URL = "https://www.reddit.com/r/"
# happy = ["crochet", "recipes", "crafts", "Shoestring", "Advice", "dadjokes", "Funny"]
# sad = ["MadeMeSmile"]
# rand_num = random.randint(0,len(happy) - 1)
# subreddit_name = happy[rand_num]

# subreddit = reddit.subreddit(subreddit_name)

# for submission in subreddit.hot(limit=10):
#     submission_id = submission.id
#     submission_url = BASE_URL + subreddit_name + "/comments/" + submission_id
#     print("Take a look at " + submission.title + ": " + submission_url)

def generate(mood):
    BASE_URL = "https://www.reddit.com/r/"
    happy = ["crochet", "recipes", "crafts", "Shoestring", "Advice", "dadjokes", "Funny"]
    sad = ["MadeMeSmile", "Advice"]
    angry = ["MadeMeSmile", "Advice"]
    choices = []
    msg = ""
    if mood == 'happy':
        choices = happy
        msg += "glad to hear you're feeling happy! you might like this post from "
    elif mood == 'sad':
        choices = sad
        msg += "sorry to hear you're feeling down. it could help you to look at this post from "
    else:
        choices = angry
        msg += "anger can be difficult to deal with. it could help calm you down to"
        msg += " distract yourself with a post from "
    rand_num = random.randint(0, len(choices) - 1)
    subreddit_name = choices[rand_num]
    msg += "r/" + subreddit_name + ". click the button below to be redirected."
    subreddit = reddit.subreddit(subreddit_name)
    submissions = subreddit.hot(limit=10)
    rand_num = random.randint(0, 9)
    for submission in submissions:
        submission_id = submission.id
        rand_num -= 1
        if rand_num == 0:
            break    
    submission_url = BASE_URL + subreddit_name + "/comments/" + submission_id
    # print("Take a look at \"" + submission.title + "\": " + submission_url)
    # print(msg)
    # print(submission_url)
    return (msg, submission_url)

if __name__ == '__main__':
    print(generate('happy'))
    