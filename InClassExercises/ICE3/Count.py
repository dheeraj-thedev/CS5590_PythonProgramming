from collections import OrderedDict


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

def sortDic(dict):
    newdic = (sorted(dict.items()))
    print(newdic)
    for key in sorted(dict):
        print("%s: %s" % (key, dict[key]))



sentence = input('Please enter a sentence: ')
counted = word_count(sentence)
sortDic(counted)
