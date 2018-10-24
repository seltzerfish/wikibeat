MAX_LINE_LENGTH = 105
USE_MORE_MAX = 50
NUM_PERFECT = 500
NUM_IMPERFECT = 500
THREAD_WAIT = 0.03
from time import sleep
from datamuse import datamuse
from nltk.tokenize import sent_tokenize, word_tokenize
from threading import Thread


def get_end_words(sentences):
    ending_words = []
    for s in sentences:
        words = word_tokenize(s)
        a = words.pop()
        if words:
            end = words.pop()
            ending_words.append(end.lower())
        else:
            ending_words.append(a)
    return ending_words


def thread_perf(word1, x, ending_words, output, seen, api, used, max=NUM_PERFECT):
    if word1 in seen:
        print("SAVED")
        return
    perf = api.words(rel_rhy=word1, max=NUM_PERFECT)
    rhymes_here = []
    for entry in perf:
        w = entry["word"]
        for y, e in enumerate(ending_words[x:]):
            if w == e:
                rhymes_here.append((w, y + x))
                if (word1, w) not in used and (w, word1) not in used:
                    print(word1, w, entry["score"])
                    used.add((word1, w))
                    output.append((word1, w, x, y + x))
                    seen.add(word1)
                    seen.add(w)
    for j in range(len(rhymes_here)):
        for k in range(j + 1, len(rhymes_here)):
            if (rhymes_here[j][0], rhymes_here[k][0]) not in used and rhymes_here[j][
                0
            ] != rhymes_here[k][0]:
                used.add((rhymes_here[j][0], rhymes_here[k][0]))
                output.append(
                    (
                        rhymes_here[j][0],
                        rhymes_here[k][0],
                        rhymes_here[j][1],
                        rhymes_here[k][1],
                    )
                )
                print((rhymes_here[j][0], rhymes_here[k][0]))


def thread_almost(word1, x, ending_words, output, seen2, api, used, max=NUM_IMPERFECT):
    if word1 in seen2:
        print("SAVED")
        return
    almost = api.words(rel_nry=word1, max=NUM_IMPERFECT)
    # rhymes_here = []

    for entry in almost:
        w = entry["word"]
        for y, e in enumerate(ending_words[x:]):
            if w == e:
                # rhymes_here.append((w, y + x))
                if (word1, w) not in used and (w, word1) not in used:
                    print(word1, w, entry["score"])
                    used.add((word1, w))
                    output.append((word1, w, x, y + x))
                    seen2.add(word1)
                    seen2.add(w)


def rap(sentences):
    used = set()
    rhymes = []
    api = datamuse.Datamuse()
    for s in sentences:
        if not s:
            sentences.remove(s)
    ending_words = get_end_words(sentences)
    seen = set()
    threads = [None] * len(ending_words)
    results = [[] for _ in range(len(ending_words))]
    for x, word1 in enumerate(ending_words):
        threads[x] = Thread(
            target=thread_perf,
            args=(word1, x, ending_words, results[x], seen, api, used),
        )
        threads[x].start()
        sleep(THREAD_WAIT)

    for i in range(len(threads)):
        threads[i].join()
    for r in results:
        if r:
            for e in r:
                rhymes.append(e)
    print(rhymes)

    seen2 = set()
    if len(rhymes) < USE_MORE_MAX:
        print("USING MORE")
        threads2 = [None] * len(ending_words)
        results2 = [[] for _ in range(len(ending_words))]
        for x, word1 in enumerate(ending_words):
            threads2[x] = Thread(
                target=thread_almost,
                args=(word1, x, ending_words, results2[x], seen2, api, used),
            )
            threads2[x].start()
            sleep(THREAD_WAIT)

        for i in range(len(threads2)):
            threads2[i].join()
        for r in results2:
            if r:
                for e in r:
                    rhymes.append(e)

    print(rhymes)

    rhymes.sort(key=lambda x: abs(x[2] - x[3]))
    rhymes.sort(key=lambda x: x[2])

    couplets = []

    for r in rhymes:
        couplets.append((sentences[r[2]].replace(u'\xa0', u' '), sentences[r[3]].replace(u'\xa0', u' ')))

    # couplets.sort(key=lambda x: abs(len(x[0]) - len(x[1])))
    # couplets.sort(key=lambda x: len(x[0]))
    couplets = [
        c
        for c in couplets
        if len(c[0]) < MAX_LINE_LENGTH and len(c[1]) < MAX_LINE_LENGTH
    ]
    return couplets
