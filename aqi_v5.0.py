# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/16 0016 上午 9:33'
# AQI计算
# 爬去pm25.in网站来获取数据

import requests


def get_html_text(url):
    """
    返回url的文本
    :param url:
    :return:
    """
    r = requests.get(url, timeout = 30)
    # print(r.status_code)
    return r.text


def main():
    """
    主函数
    :return:
    """
    city_pinyin = input("请输入城市拼音：")
    url = 'http://pm25.in/' + city_pinyin
    url_text = get_html_text(url)
    aqi_div = '''    <div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 2
    aqi_val = url_text[begin_index: end_index]
    print("空气质量为："+aqi_val)


if __name__ == '__main__':
    main()
