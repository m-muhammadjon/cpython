import requests
import time
from requests_html import HTMLSession
from collections import Counter
from bs4 import BeautifulSoup

start = time.time()
ai = []
ss=0
for page in range(1, 15):
    print(page)
    url = f'http://cpython.uz/competitions/contests?page={page}'
    try:
        print(f'Page: {page}')
        session = HTMLSession()
        response = session.get(url)
        # print(response.html.find('#past-contests tbody tr td a'))
        # new_url = 'http://cpython.uz/competitions/contest/82/standings/'
        # print(new_url)
        # res2 = session.get(new_url)
        # print(res2.html.find('#standings tbody tr', first=True).text.split('\n')[:3])
        for xd in response.html.find('#past-contests tbody tr td.text-center a'):
            new_url = 'http://cpython.uz' + xd.attrs['href'] + 'standings/'
            print(new_url)
            res2 = session.get(new_url)
            try:
                qq = res2.html.find('#standings tbody tr', first=True).text.split('\n')[:3]

                try:
                    num = int(qq[-1])
                    print(qq[1])
                    ai.append(qq[1])
                except:
                    users = qq[-1].split(',')
                    print(users)
                    print(len(ai))
                    for i in users:
                        print(i.strip())
                        ai.append(i.strip())
                    print(len(ai))
                    pass
            except :
                ss+=1

    except requests.exceptions.RequestException as e:
        print(e)
print(ss)
end = time.time()
print(ai.count('Shoxzod'))
print(Counter(ai))
print(int((end - start) * 1000), 'ms')

# iya = {'Madaminov0888': 13, 'Shoxzod': 12, 'kharezmi': 11, 'Quvonchbek': 8, 'The_Samurai': 7, 'admin': 7, 'MDSPro': 6,
#        'Zohidbek': 5, 'Ibrohim': 5, 'Husayn_Hasanov': 5, 'ogabek8433': 5, 'OtabekJurabekov': 4, 'p1ke': 4,
#        'Rasulbek07': 4, 'AZD_creation': 4, 'bagbanpir': 4, 'Narzullayev.S_': 3, 'Sunnat': 3, 'temur.dusenbaev': 3,
#        'Alibek': 3, 'dxz05': 2, 'Lazizbek': 2, 'Mansurbek': 2, 'hojinazar_otaxonov': 2, 'doniyor_samandarov': 2,
#        'umidbek_raximberganov': 2, 'mercurial': 1, 'FillerSeries': 1, 'Dasturchi': 1, 'cosmosc': 1, 'dusenbaev': 1,
#        'ThA': 1, 'ОбидСиндаров': 1, 'JavohirXoldorov': 1, 'alimurodov': 1, 'muhammadjon': 1, 'genemator': 1,
#        'olimboy': 1, 'timurruzmetov': 1, 'Siroj': 1, 'Dilbar': 1, 'anonymous': 1, 'zakam1999': 1, 'sapaevruzmat': 1,
#        'maftuna_karimboyeva': 1, 'karim': 1, 'xursand_saydmurotov': 1, 'timur_rahimquliyev': 1}
# for key, val in iya.items():
#     print(f'{key} - {val}')
