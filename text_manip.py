import re
import pyphen
from nltk.tokenize import word_tokenize, sent_tokenize

DIC = pyphen.Pyphen(lang='en')
def clean_article(article):
    article = re.sub(r'\(.+\)', '', article)
    article = re.sub(r'\[\d+\]', '', article)
    return article


def count_syllables(string):
    return DIC.inserted(string).count("-")

# 0 - 8 = short
# 8 - 16 = med