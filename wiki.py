import wikipedia
import random

# for title in wiki:
#     rand_page = wikipedia.page(title)
#     print(rand_page.url)

def generate(mood):
    wiki = wikipedia.random(pages=10)
    rand_num = random.randint(0,9)
    title = wiki[rand_num]
    rand_page = wikipedia.page(title)
    rand_page_url = rand_page.url
    msg = ""
    if mood == 'happy':
        # choices = happy
        msg += "glad to hear you're feeling happy! ~expand your mind~ by learning about "
    elif mood == 'sad':
        # choices = sad
        msg += "sorry to hear you're feeling down. it could help you to "
        msg += "distract yourself by learning about "
    else:
        # choices = angry
        msg += "anger can be difficult to deal with. it could help calm you down to"
        msg += " distract yourself by learning about "
    msg += title + "."
    return (msg, rand_page_url)

if __name__ == '__main__':
    print(generate('happy'))