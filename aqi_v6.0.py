# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/16 0016 上午 9:33'
# AQI计算
# 爬去pm25.in网站来获取数据
# 使用beautifulsoup4来爬去网页
import requests
from bs4 import BeautifulSoup


def get_city_aqi(city_pinyin):
    """
    获取城市的AQI
    :param url:
    :return:
    """
    url = 'http://pm25.in/' + city_pinyin
    r = requests.get(url, timeout = 30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', {'class': 'span1'})

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()

        city_aqi.append((caption, value))
    return city_aqi


def main():
    """
    主函数
    :return:
    """
    city_pinyin = input("请输入城市拼音：")
    city_aqi = get_city_aqi(city_pinyin)
    print(city_aqi)


if __name__ == '__main__':
    main()
