import codecs

with open("C:\\Users\\ASIA-14\Desktop\\negative_words_self.txt",encoding='utf-8') as neg:
    negative=neg.readlines()
negative=[neg.replace("\n","") for neg in negative]

with