from pydub import AudioSegment
from os import system
from wiki_fetch import fetch_page_content
from text_manip import clean_article, count_syllables
from rap import rap
from nltk.tokenize import sent_tokenize
from translate_back import translate_back
from threading import Thread
from time import sleep

# with open("out.txt", 'r') as f:
#     page = " ".join(f.readlines())


page = fetch_page_content(
    "https://en.wikipedia.org/wiki/Bob_Ross"
)
sentences = [clean_article(sent).strip() for sent in sent_tokenize(page)]

couplets = rap(sentences)

for c in couplets:
    print(c[0])
    print(c[1])
    print()
