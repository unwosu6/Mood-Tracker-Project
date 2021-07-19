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
#     sumbission_id = submission.id
#     sumbission_url = BASE_URL + subreddit_name + "/comments/" + sumbission_id
#     print("Take a look at " + submission.title + ": " + sumbission_url)

def generate(mood):
    BASE_URL = "https://www.reddit.com/r/"
    happy = ["crochet", "recipes", "crafts", "Shoestring", "Advice", "dadjokes", "Funny"]
    sad = ["MadeMeSmile", "Advice"]
    angry = ["MadeMeSmile", "Advice"]
    choices = []
    if mood == 'happy':
        choices = happy
    elif mood == 'sad':
        choices = sad
    else:
        choices = angry
    rand_num = random.randint(0, len(choices) - 1)
    subreddit_name = choices[rand_num]
    subreddit = reddit.subreddit(subreddit_name)
    submissions = subreddit.hot(limit=10)
    rand_num = random.randint(0, 9)
    for submission in submissions:
        sumbission_id = submission.id
        rand_num -= 1
        if rand_num == 0:
            break    
    sumbission_url = BASE_URL + subreddit_name + "/comments/" + sumbission_id
    print("Take a look at \"" + submission.title + "\": " + sumbission_url)
    # return sumbission_url

if __name__ == '__main__':
    generate('happy')
    