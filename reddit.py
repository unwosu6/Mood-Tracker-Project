import praw
import random

reddit = praw.Reddit(
    client_id="8362eGvzJWKAjATcybac_w",
    client_secret="T-Lp0nn_iTaXryQ9-FKnXYDXvm5rjA",
    user_agent="windows:mood-tracker:v1.0.0 (by /u/QueenProtista)",
)
BASE_URL = "https://www.reddit.com/r/"
happy = ["crochet", "recipes", "crafts", "Shoestring", "Advice", "dadjokes", "Funny"]
rand_num = random.randint(0,len(happy) - 1)
subreddit_name = happy[rand_num]

subreddit = reddit.subreddit(subreddit_name)

for submission in subreddit.hot(limit=10):
    sumbission_id = submission.id
    sumbission_url = BASE_URL + subreddit_name + "/comments/" + sumbission_id
    print("Take a look at " + submission.title + ": " + sumbission_url)
    