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
    mood = 'sad'

    r = None
    if mood == 'happy':
        r = youtube.search().list(q='try not to laugh', part='snippet', type='video', maxResults=10)
    if mood == 'sad':
        r = youtube.search().list(q='cute animals', part='snippet', type='video', maxResults=10)
    if mood == 'angry':
        r = youtube.search().list(q='scenic videos', part='snippet', type='video', maxResults=10)

    res = r.execute()
    pprint.pprint(res)

    list = [None] * 10
    count = 0
    for id in res['items']:
        list[count]= id['id']['videoId']
        count = count + 1
    print(list)

    index = random.randint(0, 9)
    #baseUrl = 'https://www.youtube.com/watch?v=' + index


if __name__ == '__main__':
    print(generate())