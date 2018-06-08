from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.readlines())

d = word_count("test2.txt")
print("Number of words in the file :",d)


def rowCount(eachRow):
    listtemp = eachRow.read()
    return len(listtemp)
    """count = 0
    for a in eachRow:
        count = count + 1
    return len(eachRow)"""



with open("out.txt", "w") as myfile:
    for key in sorted(d):
        ##myfile.write(key + "," + ",".join(d[key]) + "\n")
        myfile.write(key + "," + str(len(key.split())) + "\n")
