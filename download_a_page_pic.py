import re
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import os

root = "D:\\MyTest\\pythonTest\\妹子图爬虫\\自拍偷拍\\第6页\\"


# 进入一个界面解析地址图片地址 并下载图片
# 主程序
def down_one_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    expression = '(?<=src=").+?.jpg(?=")'
    pic_links = re.findall(expression, soup.decode(), flags=re.M)
    # expression2 = r'(?<=alt=")(\w+)|(?<=alt="\[....\])(\w+)|(?<=alt="\[................\])(\w+)'
    expression2 = r'(?<=alt=")([\S\s]+?)(?=")'
    # try:
    pck_name = re.search(expression2, soup.decode(), flags=re.M).group(0)
    # 目的地址
    subroot = root+pck_name+"\\"
    # except AttributeError:
    #     print("'NoneType' object has no attribute 'group'")

    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(subroot):
            os.mkdir(subroot)
        count = 0
        for v in pic_links:
            count += 1
            print("第" + str(count) + "个:" + v)
            with open(subroot+str(count)+".jpg", 'wb') as f:
                f.write(get_pic(v))
                f.close()
    except FileNotFoundError:
        print("打开文件夹失败")
    except OSError:
        print("目录名不合法")
        pass


# 获得图片
def get_pic(pic_url):
    temp_pic = requests.get(pic_url)
    return temp_pic.content
    # i = Image.open(BytesIO(temp_pic.content))
    # return i
    # 显示图片
    # plt.imshow(i)
    # plt.show()


# down_one_page(url="https://www.6222n.com/htm/Pic1/138115.htm")
