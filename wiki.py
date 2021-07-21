import wikipedia
import random
from bs4 import BeautifulSoup

def generate(mood):
    BeautifulSoup(features="html.parser")
    wiki = wikipedia.random(pages=1)
    title = wiki
    rand_page = wikipedia.page(title)
    rand_page_url = rand_page.url
    msg = ""
    if mood == 'happy':
        # choices = happy
        msg += "glad to hear you\'re feeling happy! ~expand your mind~ by learning about "
    elif mood == 'sad':
        # choices = sad
        msg += "sorry to hear you\'re feeling down. it could help you to "
        msg += "distract yourself by learning about "
    else:
        # choices = bored
        msg += "boredom can be difficult to deal with. ~expand your mind~ by learning about "
    msg += title + "."
    return (msg, rand_page_url)

if __name__ == '__main__':
    print(generate('happy'))