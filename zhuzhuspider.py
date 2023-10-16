import json
import re
import requests
import datetime
from bs4 import BeautifulSoup
import os

headers = { 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
url='https://baike.baidu.com/item/%E6%9C%B1%E7%8F%A0/6720'  
save_path = "D:\\git-repo\\image\\"
i = 1

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text,'html.parser')
image_urls = soup.find_all("img", {"class": "picture"})
for image_url in image_urls:
    try:
        url = image_url["src"]
        responseImg = requests.get(url)
        string = 'zhuzhu' + str(i) + '.jpg'
        with open(save_path + string, 'wb') as f:  # 以二进制写入文件保存
            f.write(responseImg.content)
        i += 1
    except Exception as e:
        print(e)
        continue

    
