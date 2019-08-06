import re
import requests
from bs4 import BeautifulSoup


# 获取一个页面所有套图的链接 并下载
def get_url(url):
    # url = "https://www.6222n.com/htm/Picture1/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    expression = r'(?<=a href=")/htm/Pic\d+.+?.htm'
    urls_one_page = re.findall(expression, soup.decode(), flags=re.M)
    return urls_one_page
    # print(urls_one_page)
    # while urls_one_page:
    #     del urls_one_page[0]
