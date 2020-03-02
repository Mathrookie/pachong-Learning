import requests
import re

def getHtmlText(url):
    try:
        r = requests.get('https://new.qq.com/ch/antip',headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        rest = requests.get('https://i.match.qq.com/tubdhotinterface?site=aiotwf&num=100&type=img&app=aio&child=news_news_antip&expIds=20200302A0G814|20200208V0ONIX|20200202008374|20200302A08VXJ|20200302A06QBT|20200302A08FFB|20200302A09FWE|20200302A0E2L3|20200302A05OBO|20200302A04IXD|20200302A0AG5E|20200221004605|20200302A0497S|20200131009129|20200302A0EEAF|20200302A0C7VA|20200302A07C8Q|20200302A03TU7|20200302A0COY8|20200302A06D68&callback=callbackZW').text
        return r.text,rest
    except Exception as e:
        print("网络错误!!!")
        return "", ""

def getInfo(html, rest):
    merge = html+rest
    info = re.findall(r'"title":"(.*?)"', merge)
    for i in range(len(info)):
        info[i] = eval("u" + "\"" + info[i] + "\"")
    return info

def printInfo(data):
    for i in range(len(data)):
        print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t'+data[i]+'\n')

def main():
    url = 'https://new.qq.com/ch/antip'
    while True:
        try:
            num = eval(input("输入1以刷新(输入0退出): "))
        except Exception as e:
            print("输入错误！！")
            continue
        if num == 0:
            break
        elif num == 1:
            html,rest = getHtmlText(url)
            if html == "" or rest == "":
                continue
            printInfo(getInfo(html,rest))


main()

