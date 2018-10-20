from pydub import AudioSegment
from wiki_fetch import fetch_page_content
from text_manip import clean_article, count_syllables
from nltk.tokenize import sent_tokenize, word_tokenize
from datamuse import datamuse

# with open("out.txt", 'r') as f:
#     page = " ".join(f.readlines())


page = fetch_page_content("https://en.wikipedia.org/wiki/Donald_Trump")
sentences = [clean_article(sent).strip() for sent in sent_tokenize(page)]
used = set()
rhymes = []
ending_words = []
api = datamuse.Datamuse()
for s in sentences:
    if not s:
        sentences.remove(s)
for s in sentences:
    words = word_tokenize(s)
    a = words.pop()
    if words:
        end = words.pop()
        ending_words.append(end.lower())
    else:
        ending_words.append(a)
seen = set()

for x, word1 in enumerate(ending_words):
    if word1 in seen:
        print("SAVED")
        continue
    perf = api.words(rel_rhy=word1, max=500)
    # almost = api.words(rel_nry=word1, max=50)
    rhymes_here = []
    for entry in perf:
        w = entry['word']
        for y, e in enumerate(ending_words[x:]):
            if w == e:
                rhymes_here.append((w, y + x))
                if (word1, w) not in used and (w, word1) not in used:
                    print(word1, w)
                    used.add((word1, w))
                    rhymes.append((word1, w, x, y + x))
                    seen.add(word1)
                    seen.add(w)
    for j in range(len(rhymes_here)):
        for k in range(j + 1, len(rhymes_here)):
            if (rhymes_here[j][0], rhymes_here[k][0]) not in used and rhymes_here[j][0] != rhymes_here[k][0]:
                used.add((rhymes_here[j][0], rhymes_here[k][0]))
                rhymes.append((rhymes_here[j][0], rhymes_here[k][0], rhymes_here[j][1], rhymes_here[k][1]))
                print((rhymes_here[j][0], rhymes_here[k][0]))

seen2 = set()
if len(rhymes) < 40: 
    print("USING MORE")
    for x, word1 in enumerate(ending_words):
        if word1 in seen2:
            print("SAVED")
            continue
        almost = api.words(rel_nry=word1, max=50)
        rhymes_here = []

        for entry in almost:
            w = entry['word']
            for y, e in enumerate(ending_words[x:]):
                if w == e:
                    rhymes_here.append((w, y + x))
                    if (word1, w) not in used and (w, word1) not in used:
                        print(word1, w)
                        used.add((word1, w))
                        rhymes.append((word1, w, x, y + x))
                        seen2.add(word1)
                        seen2.add(w)
        for j in range(len(rhymes_here)):
            for k in range(j + 1, len(rhymes_here)):
                if (rhymes_here[j][0], rhymes_here[k][0]) not in used and rhymes_here[j][0] != rhymes_here[k][0]:
                    used.add((rhymes_here[j][0], rhymes_here[k][0]))
                    rhymes.append((rhymes_here[j][0], rhymes_here[k][0], rhymes_here[j][1], rhymes_here[k][1]))
                    print((rhymes_here[j][0], rhymes_here[k][0]))
print(rhymes)

rhymes.sort(key=lambda x: abs(x[2] - x[3]))
rhymes.sort(key=lambda x: x[2])

couplets = []


for r in rhymes:
    couplets.append((sentences[r[2]], sentences[r[3]]))

# couplets.sort(key=lambda x: abs(len(x[0]) - len(x[1])))
# couplets.sort(key=lambda x: len(x[0]))

for c in couplets:
    if len(c[0]) <= 110 and len(c[1]) <= 110:
        print(c[0])
        print(c[1])
        print()

