# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/16 0016 上午 9:33'
# AQI计算
# 读取json文件


import json
import csv


def process_json_file(filepath):
    """
    解码json文件
    :param filepath:
    :return:
    """
    f = open(filepath, mode='r', encoding='utf-8')
    city_list = json.load(f)
    return city_list


def main():
    """
    主函数
    :return:
    """
    filepath = input("请输入json文件名称：")
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])

    lines = []
    # 列名
    lines.append(list(city_list[0].keys()))
    for city in city_list:
        lines.append(list(city.values()))

    f = open('aqi.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()


if __name__ == '__main__':
    main()
