#=====importing libraries===========
import spacy #NLP library

#====Format Section====
UNDERLINE = "\033[4m"
BOLD = "\033[1m"
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[33m"

#loading the language model and assign it to a variable.
nlp = spacy.load( 'en_core_web_md' )

def watch_next(movie_watched,movie_watched_desc,movie_store):
    score = 0
    movie_to_watch = ""
    #passing the string through the language model
    movie_watched_desc_nlp = nlp(movie_watched_desc)
    print(f"{UNDERLINE}{BOLD}Similarity score:{RESET}")
    for key, value in movie_store.items():
        score_check = movie_watched_desc_nlp.similarity(nlp(value))
        print(f"{key} - {score_check}")
        if score < score_check:
            score = score_check
            movie_to_watch = key
    print("-"*100)
    print(f"As you watched {BOLD}{BLUE}{movie_watched}{RESET}, you should chose next: {BOLD}{GREEN}{movie_to_watch}{RESET}\n\n{UNDERLINE}{BOLD}Description:{RESET} {movie_store[movie_to_watch]}")


#User watched Planet Hulk with the description below
movie_watched = "Planet Hulk"
movie_watched_desc = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

#passing the string through the language model
movie_watched_nlp = nlp(movie_watched)

file = open("movies.txt", "r",encoding="utf-8")

#dictionary store for the movies
movie_store = {}

#loading the movies to the dictionary
for i in file:
    movie_store[i[:7]] = i[9:].strip("\n")

file.close()
#print(movie_store)

watch_next(movie_watched,movie_watched_desc,movie_store)