from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

d = word_count("test.txt")
print("Number of words in the file :",d)

with open("out.txt", "w") as myfile:
    for key in sorted(d):
        ##myfile.write(key + "," + ",".join(d[key]) + "\n")
        myfile.write(key + "," + str(d[key]) + "\n")
