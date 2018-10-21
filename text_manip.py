import re
import pyphen
from nltk.tokenize import word_tokenize, sent_tokenize

DIC = pyphen.Pyphen(lang="en")


def clean_article(article):
    article = re.sub(r"\(.+\)", "", article)
    article = re.sub(r"\[.+\]", "", article)
    article = re.sub(r":\d+\s", "", article)
    article = article.replace('"', "")
    article = re.sub(r"\<\w+\>", "", article)
    article = re.sub(r"\<\/\w+\>", "", article)

    return article


def count_syllables(string):
    return DIC.inserted(string).count("-")


# 0 - 8 = short
# 8 - 16 = med


def delete_duplicates(couplets):
    for i, c1 in enumerate(couplets):
        same = set()
        for c2 in couplets[i:]:
            if c1[0] == c2[0]:
                same.add(tuple(c1))
                same.add(tuple(c2))
        if len(same) > 1:
            same = list(same)
            same.sort(key=lambda x: abs(len(x[0]) - len(x[1])))
            for s in same[1:]:
                couplets.remove(s)
    return couplets
