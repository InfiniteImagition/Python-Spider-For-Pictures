from get_firstpage_url import *
from download_a_page_pic import *


url = "https://www.6222n.com/htm/Picture1/6.htm"
# 第一页里所有的url
urls = get_url(url)
category = 0
for v in urls:
    category += 1
    print("----------"+str(category)+"----------")
    url_temp = "https://www.6222n.com"+v
    down_one_page(url_temp)

