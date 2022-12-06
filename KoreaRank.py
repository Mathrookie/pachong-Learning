# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:13:07 2020

@author: MathRookie
"""
import requests
import numpy
from bs4 import BeautifulSoup


def GetHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print("出现异常")
        return ""


def GetRankList(html, rank):
    soup = BeautifulSoup(html, "html.parser")
    for top5 in soup.find('ul', id='select_summoner_highest').children:
        rank.append([top5('div')[0].string, top5('a')[1].string])
    for rest in soup.find('tbody').children:
        rank.append([rest('td')[0].string, rest('td')[1].find('span').string])


def PrintRank(rank, num):
    for i in range(num):
        print("{}. {}".format(rank[i][0], rank[i][1]))


if __name__ == '__main__':
    url = 'http://www.op.gg/ranking/ladder'
    rank = []
    while True:
        html = GetHtmlText(url)
        if html == "":
            break
        GetRankList(html, rank)
        try:
            num = eval(input("请输入要查询的排名数(输入0退出): "))
        except Exception as e:
            print("输入错误！！")
            continue
        if num == 0:
            break
        if num < 0 or num > 100:
            print("只能查找前一百名！！")
            continue
        PrintRank(rank, num)

