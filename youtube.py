from apiclient.discovery import build
import requests
import pprint
import random

def generate(mood):
#     happy = []
#     sad = []
#     bored = []
#     choices = []
#     msg = ""
#     if mood == 'happy':
#         choices = happy
#         # maybe choose a random search term from a predefined list of search terms like in reddit.py
#         pass
#     elif mood == 'sad':
#         choices = sad
#         pass
#     else:
#         choices = bored
#         pass
#     rand_num = random.randint(0, len(choices) - 1)
#     search_term = choices[rand_num]
#     video_url = "" # make api calls to search youtube here.
#     return (msg, video_url)


    YOUTUBE_KEY = 'AIzaSyAGWidFWjvejleMBAKxrWt8e1-zQ3X9Trg'
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_KEY)
    # mood = 'sad'
    happy = ['try not to laugh']
    sad = ['cute animals']
    bored = ['scenic videos', 'try not to laugh']
    choices = []
    msg = ""
    r = None
    if mood == 'happy':
        choices = happy
        msg += "glad to hear you\'re feeling happy! you might like "
    elif mood == 'sad':
        choices = sad
        msg += "sorry to hear you\'re feeling down. it could help you to watch"
    else:
        choices = bored
        msg += "boredom can be difficult to deal with. check out "
    
    rand_num = random.randint(0, len(choices) - 1)
    search_term = choices[rand_num]
    msg += " this video from the search term: \"" + search_term + "\". click the button below to be redirected."
    r = youtube.search().list(q=search_term, part='snippet', type='video', maxResults=10)
    res = r.execute()
    #pprint.pprint(res)

#     list = [None] * 10
#     count = 0
#     for id in res['items']:
#         list[count]= id['id']['videoId']
#         count = count + 1
    #print(list)

    rand_index = random.randint(0, 9)
    # res['items'][rand_index]
    BASE_URL = "https://youtu.be/"
    video_id = res['items'][rand_index]['id']['videoId'] 
    video_url = BASE_URL + video_id
    return msg, video_url

if __name__ == '__main__':
    print(generate('sad'))