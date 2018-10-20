from googletrans import Translator


def translate_back(inp, number, output):
    t = Translator()
    a = t.translate(inp, src="en", dest="ja")
    b = t.translate(a.text, src="ja", dest="en").text
    output.append(number)
    output.append(b)
    print(number)


# threads = [None] * len(sentences)
# results = [[] for _ in range(len(sentences))]
# for i, s in enumerate(sentences):
#     threads[i] = Thread(target=translate_back, args=(s, i, results[i]))
#     threads[i].start()
#     sleep(0.1)

# for i in range(len(threads)):
#     threads[i].join()

# print(len(results))
# for r in results:
#     print(r)
#     print("\n")
