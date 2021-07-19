import wiki
import reddit
import youtube
# import spotify
import random

def generate(mood):
    content_types = ['reddit', 'wiki', 'youtube', 'spotify']
    rand_num = random.randint(0, len(content_types) - 1)
    content = content_types[rand_num]
    msg_url_tuple = ()
    if content == 'reddit':
        msg_url_tuple = reddit.generate(mood)
    if content == 'wiki':
        msg_url_tuple = wiki.generate(mood)
    if content == 'youtube':
        msg_url_tuple = youtube.generate(mood)
#     else:
#         msg_url_tuple = spotify.generate(mood)
    return msg_url_tuple

if __name__ == '__main__':
    print(generate('happy'))