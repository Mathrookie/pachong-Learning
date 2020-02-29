import requests
from bs4 import BeautifulSoup

def getHtmlText(url):
    try:
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
        r = requests.get(url, timeout=30, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print("网络错误!!!")
        return ""

def getInfo(html, data):
    soup = BeautifulSoup(html, "html.parser")
    for i in range(17):
        data.append(soup('div',attrs={'class':'lazyload-placeholder'})[i].string)

def printInfo(data):
    for i in range(len(data)):
        print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t'+data[i]+'\n')

def main():
    url = 'https://new.qq.com/ch/antip'
    while True:
        data = []
        try:
            num = eval(input("输入1以刷新(输入0退出): "))
        except Exception as e:
            print("输入错误！！")
            continue
        if num == 0:
            break
        elif num == 1:
            html = getHtmlText(url)
            if html == "":
                continue
            getInfo(html,data)
            printInfo(data)

main()

