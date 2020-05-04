"""
Crawler for videos on Bilibili
"""
import pprint
import requests
import time

def download(url, name):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    response = requests.get(url, headers=headers)
    print(response)
    file = open(f'{name}.mp4', mode='wb')
    file.write(response.content)
    file.close()

#url1 = 'https://upos-sz-mirrorkodo.bilivideo.com/dspxcode/m190708ws2hdf7opu4ag442ybwt94hsv-1-56.mp4?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1588596871&gen=playurl&os=kodobv&oi=1942073786&trid=07620ac1d15a43f08634f4612513edaes&platform=html5&upsig=b323830a3615855bac701a7d21544e2a&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&logo=00000000&wsTime=1588596871'
#download(url1, 'name1')
def get_one_page(index_url):
    response = requests.get(index_url)
    data = response.json()
    items = data['data']['items']
    for item in items:
        video_playurl = item['item']['video_playurl']
        video_name = item['user']['name'] + "_" + item['item']['description'][:5]
        download(video_playurl, video_name)

for page in range(0,5):
    index_url = f'https://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset={page*10+1}&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc'
    time.sleep(1)
    get_one_page(index_url)