import wikipedia
import random

wiki = wikipedia.random(pages=10)
rand_num = random.randint(0,9)
title = wiki[rand_num]
rand_page = wikipedia.page(title)
print(rand_page.url)

# for title in wiki:
#     rand_page = wikipedia.page(title)
#     print(rand_page.url)
