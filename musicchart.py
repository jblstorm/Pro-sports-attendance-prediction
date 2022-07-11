# import requests
# from bs4 import BeautifulSoup
# import lxml
# url="https://music.bugs.co.kr/chart/track/week/total?chartdate=20220420"
# # url="https://music.bugs.co.kr/chart"
# # url="https://music.bugs.co.kr/chart/track/day/total"
# # url="https://music.bugs.co.kr/chart/track/week/total"
#
# html_music=requests.get(url).text
# soup_music=BeautifulSoup(html_music,"lxml")
#
#  #p 태그 요소에서 class 속성 값 "title"
#  #a 태그 요소 추출
#
# titles=soup_music.select('p.title a')
# titles[0:7]
# music_titles=[title.get_text() for title in titles]
# print(music_titles[0:7])
#
# artists=soup_music.select('p.artist a')
# print(artists[0:7])
#
# music_artists=[artist.get_text() for artist in artists]
# music_artists[0:7]



# print(music_titles_artists[1])
# print(music_titles_artists[2])

import requests
from bs4 import BeautifulSoup

def bugs_music_week_top100(year,month,day):
    month="{0:02d}".format(month)
    day="{0:02d}".format(day)
    base_url='https://music.bugs.co.kr/chart/track/week/total?'
    url=base_url+'chartdate={0}{1}{2}'.format(year,month,day)

    html_music=requests.get(url).text
    soup_music=BeautifulSoup(html_music,"lxml")

    titles=soup_music.select('p.title a')
    artists=soup_music.select('p.artist a:not(.more)')
    music_titles=[title.get_text() for title in titles]
    music_artists=[artist.get_text().strip() for artist in artists]
    return music_titles,music_artists

import glob
#날짜 지정 함수 호출
bugs_music_titles, bugs_music_artists= bugs_music_week_top100(2022,5,5)

file_name='C:\\Users\\ASIA-14\\PycharmProjects\\pythonProject2\\bugs_week_100.txt'

f=open(file_name,'w') #window창

for k in range(len(bugs_music_titles)):
    f.write("{0:2d}: {1}/{2}\n".format(k+1,bugs_music_titles[k],bugs_music_artists[k]))

f.close()
glob.glob(file_name)