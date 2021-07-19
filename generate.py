import wiki
import reddit
import random

def genreate(mood):
    content_types = ['reddit', 'wiki']
    rand_num = random.randint(0, len(content_types) - 1)
    content = content_types[rand_num]
    url = ""
    if content == 'reddit':
        url = reddit.generate(mood)
    
    if content == 'wiki':
        url = wiki.generate(mood)
    return url