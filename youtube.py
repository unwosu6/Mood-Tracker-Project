import random    

def generate(mood):
    happy = []
    sad = []
    bored = []
    choices = []
    msg = ""
    if mood == 'happy':
        choices = happy
        # maybe choose a random search term from a predefined list of search terms like in reddit.py
        pass
    elif mood == 'sad':
        choices = sad
        pass
    else:
        choices = bored
        pass
    rand_num = random.randint(0, len(choices) - 1)
    search_term = choices[rand_num]
    video_url = "" # make api calls to search youtube here.
    return (msg, video_url)


if __name__ == '__main__':
    print(generate())