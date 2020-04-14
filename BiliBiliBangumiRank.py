import requests
import json
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


class Spider:
    def __init__(self, rank):
        self.rankList = []
        self.rank = rank
        self.page = rank // 20 + 1
        self.rest = rank % 20
        self.url = [
            'https://api.bilibili.com/pgc/season/index/result?season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page=',
            '&season_type=1&pagesize=20&type=1']

    def GetHtmlText(self, url):
        try:
            r = requests.get(url, timeout=30, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'})
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except Exception as e:
            print("出现异常")
            return ""

    def GetOneInfo(self, pos, text):
        info = json.loads(text)
        info = info['data']['list']
        for i in range(pos):
            self.rankList.append({info[i]['title']: info[i]['order']})

    def Run(self):
        for i in range(1, self.page + 1):
            url = self.url[0] + str(i) + self.url[1]
            text = self.GetHtmlText(url)
            if i == self.page:
                self.GetOneInfo(self.rest, text)
            else:
                self.GetOneInfo(20, text)

    def ShowBars(self):
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False
        plt.figure(figsize=(20, 8), dpi=100)
        names, y, x = [], [], []
        new_yticks = 1
        for i in list(range(0, self.rank))[::-1]:
            names.append(list(self.rankList[i].keys())[0])
            x.append(self.rank - 1 - i)
            y.append(eval(list(self.rankList[i].values())[0][:-3]))
            plt.cla()
            plt.yticks(range(new_yticks), [str(x) for x in range(self.rank, 0, -1)], fontweight='bold')
            new_yticks += 1
            plt.barh(x, y, height=1.0,
                     color=['#61A5EB', '#7ECF51', '#EECB5F', '#9570E5', 'lightcoral', 'aqua', 'lightpink'])
            plt.title('BiliBili番剧订阅量 可视化排行', fontsize=20)
            for a, b, c in zip(x, y, names):
                plt.text(b + 3, a - 0.2, "%.1f万" % b, fontsize=12 * 20 / (20 + 3 * np.log(self.rank + 1 - i)))
                plt.text(0.35 * b, a - 0.4, c, color='k', fontweight='bold',
                         fontsize=14 * 20 / (20 + 4 * np.log(self.rank + 1 - i)))
            plt.pause(0.5)
        plt.show()


if __name__ == '__main__':
    d = Spider(30)  # 此处填写要看的多少位排名
    d.Run()
    d.ShowBars()
