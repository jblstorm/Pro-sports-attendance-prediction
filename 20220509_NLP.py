# from konlpy.tag import Okt
# okt = Okt()
# token = okt.morphs("나는 자연어 처리를 배운다")
# print(token)
# ['나', '는', '자연어', '처리', '를', '배운다']
#
# #형태소 토큰화
# word2index={}
# for voca in token:
#     if voca not in word2index.keys():
#         word2index[voca] = len(word2index)
#         print(word2index)
# {'나': 0, '는': 1, '자연어': 2, '처리': 3, '를': 4, '배운다': 5}
# #케라스 이용 원-핫인코딩
# text="오늘 저녁도 참치먹어야 하나 점심 메뉴도 참치먹었는데 참치는 이제 질려"
# from keras_preprocessing.text import Tokenizer
# t = Tokenizer()
# t.fit_on_texts([text])
# # 입력으로 [text]가 아닌 text 를 넣을 경우 한 글자 단위 인코딩이 되버린다.
# print(t.word_index)


import codecs
positive=[]
negative=[]
posneg=[]

pos=codecs.open("C:\\Users\\ASIA-14\\Desktop\\positive_words_self.txt",'rb', encoding='utf-8')
while True:
    line = pos.readline()
    line = line.replace('\n', '')
    positive.append(line)
    posneg.append(line)

    if not line: break
pos.close()



neg=codecs.open("C:\\Users\\ASIA-14\\Desktop\\negative_words_self.txt",'rb', encoding='utf-8')
while True:
    line = neg.readline()
    line = line.replace('\n', '')
    positive.append(line)
    posneg.append(line)

    if not line:
        break
neg.close()

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from tqdm import tqdm

labels = []
titles = []

j = 0
for k in tqdm(range(100)):
    num = k * 10 + 1
url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%B2%84%EA%B1%B0%ED%82%B9"
req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')
titles = soup.select("a.news_tit")

for title in titles:
    title_data = title.text
    clean_title = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…\"\“》]', '', title_data)
    negative_flag = False
    label = 0
for i in range(len(negative)):
    if negative[i] in clean_title:
        label = -1
        negative_flag = True
        print("negative 비교단어: ", negative[i], "clean_title:", clean_title)
        break
if negative_flag == False:
    for i in range(len(positive)):
        if positive[i] in clean_title:
            label = 1
            print("positive 비교단어: ", positive[i], "clean_title:", clean_title)
            break
titles.append(clean_title)
labels.append(label)
my_title_df = pd.DataFrame({"title": titles, "label": labels})

# from tqdm import tqdm
# import re
#
# labels = []
#
# title_data = list(my_title_df['title'])
#
# for title in tqdm(title_data):
#     clean_title = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…\"\“]', '', title)
#     negative_flag = False
#     label = 0
# for i in range(len(negative)):
#     if negative[i] in clean_title:
#         label = -1
#         negative_flag = True
#         print("negative 비교단어: ", negative[i], "clean_title:", clean_title)
#         break
#     if negative_flag == False:
#         for i in range(len(positive)):
#             if positive[i] in clean_title:
#                 label = 1
#                 print("positive 비교단어: ", positive[i], "clean_title:", clean_title)
#                 break
#         labels.append(label)
# my_title_df['label'] = labels
#
# import pandas as pd
#
# train_data = pd.read_csv = ("C:\\Users\\ASIA-14\\Downloads\\train_dataset_1007.csv")
# test_data = pd.read_csv = ("C:\\Users\\ASIA-14\\Downloads\\test_dataset_1007.csv")
#
# import matplotlib.pyplot as plt
#
# train_data['label'].value_counts().plot(kind='bar')
# test_data['label'].value_counts().plot(kind='bar')
#
# print(train_data.groupby('label').size().reset_index(name='count'))
# print(test_data.groupby('label').size().reset_index(name='count'))
#
# stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍']
#
# import konlpy
# from konlpy.tag import Okt
#
# okt = Okt()
# x_train = []
# for sentence in train_data['title']:
#     temp_X = []
#     temp_X = okt.morphs(sentence, stem=True)
#     temp_X = [word for word in temp_X if not word in stopwards]
#     X_train.append(temp_X)
#     X_test = []
# for sentence in test_data['title']:
#     temp_X = []
#     temp_X = okt.morphs(sentence, stem=True)
#     temp_X = [word for word in temp_X if not word in stopwords]
#     X_test.append(temp_X)