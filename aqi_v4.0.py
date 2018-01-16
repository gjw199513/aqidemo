# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/16 0016 上午 9:33'
# AQI计算
# 读取json文件
# 判断文件类型+用with打开文件

import json
import csv
import os


def process_json_file(filepath):
    """
    解码json文件
    :param filepath:
    :return:
    """
    # f = open(filepath, mode='r', encoding='utf-8')
    # city_list = json.load(f)
    # return city_list
    with open(filepath, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)


def process_csv_file(filepath):
    """
    处理csv文件
    :param filepath:
    :return:
    """
    with open(filepath, mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(','.join(row))


def main():
    """
    主函数
    :return:
    """
    filepath = input("请输入文件名称：")
    filename, file_ext = os.path.splitext(filepath)

    if file_ext == '.json':
        # json文件
        process_json_file(filepath)
    elif file_ext == '.csv':
        # csv文件
        process_csv_file(filepath)
    else:
        print("不支持的文件格式！")


if __name__ == '__main__':
    main()
