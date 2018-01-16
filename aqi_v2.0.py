# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/16 0016 上午 9:33'
# AQI计算
# 读取json文件


import json


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
    top5_list = city_list[:5]
    print(city_list)

    f = open('top5_aqi.json', mode='w', encoding='utf-8')
    json.dump(top5_list, f, ensure_ascii=False)
    f.close()


if __name__ == '__main__':
    main()
