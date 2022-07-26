import requests 
import pandas as pd 
from pprint import pprint 
id = "K6aJY0X0HpPJ7c_5xZg_"
pwd = "**"
url = 'https://openapi.naver.com/v1/search/news.json?query={}'

keyword = "윤석열"
headers = {
    'X-Naver-Client-Id' : id, 
    'X-Naver-Client-Secret' : pwd 
}

res = requests.get(url.format(keyword), headers=headers)

if res.status_code == 200:
    datas = res.json() 
    print(datas)
