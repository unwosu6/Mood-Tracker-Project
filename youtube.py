from apiclient.discovery import build
import requests
# import pprint
import random


def generate(mood):
    YOUTUBE_KEY = 'AIzaSyAGWidFWjvejleMBAKxrWt8e1-zQ3X9Trg'
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_KEY)
    happy = ['try not to laugh', 'comedy central',
             'i think you should leave with tim robinson', 'jake and amir:',
             'rip vine compilation']
    sad = ['cute animals']
    bored = ['scenic videos', 'kurzgesagt', 'numberphile',
             'brain games national geographic', 'brainpop tim and moby']
    bored.extend(happy)
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
    msg += (" this video from the search term: \"" +
            search_term + "\". click the button below to be redirected.")
    r = youtube.search().list(q=search_term,
                              part='snippet', type='video', maxResults=10)
    res = r.execute()

    rand_index = random.randint(0, 9)
    BASE_URL = "https://www.youtube.com/watch?v="
    video_id = res['items'][rand_index]['id']['videoId']
    video_url = BASE_URL + video_id
    return (msg, video_url, search_term)


if __name__ == '__main__':
    print(generate('sad'))
