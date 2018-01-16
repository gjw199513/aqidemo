# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/16 0016 上午 9:33'
# AQI计算
# 爬去pm25.in网站来获取数据
# 使用beautifulsoup4来爬去网页
# 获取所有城市
# 获取的aqi放入csv文件中
# 用pandas处理数据
# 数据过滤及可视化
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
    主函数
    :return:
    """
    aqi_date = pd.read_csv('china_city_aqi.csv')
    print("基本信息：")
    print(aqi_date.info())

    print("数据预览：")
    print(aqi_date.head())

    # 数据清洗
    # 只保留AQI>0的数据
    # filter_condition = aqi_date["AQI"] > 0
    # clean_aqi_data = aqi_date[filter_condition]

    clean_aqi_data = aqi_date[aqi_date["AQI"] > 0]

    # 基本统计
    print("AQI最大值：", clean_aqi_data["AQI"].max())
    print("AQI最大值：", clean_aqi_data["AQI"].min())
    print("AQI均值：", clean_aqi_data["AQI"].mean())

    # top10
    top10_cities = clean_aqi_data.sort_values(by=["AQI"]).head(10)
    print("空气质量最好的10个城市：")
    print(top10_cities)
    # 数据可视化
    top10_cities.plot(kind='bar', x='City', y='AQI', title="空气质量最好的10个城市",
                      figsize=(20, 10))
    plt.savefig('top10_aqi_bar.png')
    plt.show()


    # bottom10
    # bottom10_cities = clean_aqi_data.sort_values(by=["AQI"]).tail(10)
    bottom10_cities = clean_aqi_data.sort_values(by=["AQI"], ascending=False).head(10)
    print("空气质量最差的10个城市：")
    print(bottom10_cities)

    # 保存csv文件
    top10_cities.to_csv('top10_aqi.csv', index=False)
    bottom10_cities.to_csv('top10_aqi.csv', index=False)


if __name__ == '__main__':
    main()
