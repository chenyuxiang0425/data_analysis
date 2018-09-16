"""
    明确目的：比较全年共享单车的用户类别（会员和非会员的比例）
"""

import os
import numpy as np
import matplotlib.pyplot as plt

data_path = './data/bikeshare'
data_filenames = ['2017-q1_trip_history_data.csv', '2017-q2_trip_history_data.csv',
                  '2017-q3_trip_history_data.csv', '2017-q4_trip_history_data.csv']


def collect_and_process_data():
    """
        Step 1: 数据收集和处理
    """
    member_type_list = []
    for data_filename in data_filenames:
        data_file = os.path.join(data_path, data_filename)
        data_arr = np.loadtxt(data_file, delimiter=',', dtype='str', skiprows=1)
        # 去掉双引号
        member_type_col = np.core.defchararray.replace(data_arr[:, -1], '"', '')
        member_type_col = member_type_col.reshape(-1, 1) # -1指自动计算
        member_type_list.append(member_type_col)
    # 数据拼接,list拼接
    year_member_type = np.concatenate(member_type_list)
    return year_member_type


def analyze_data(year_member_type):
    """
        数据分析
    """
    n_member = year_member_type[year_member_type == 'Member'].shape[0]
    # shape[0]返回行数
    # shape函数是numpy.core.fromnumeric中的函数，它的功能是查看矩阵或者数组的维数。
    n_casual = year_member_type[year_member_type == 'Casual'].shape[0]
    n_users = [n_member, n_casual]
    return n_users


def save_and_show_results(n_users):
    """
        结果展示
    """
    plt.figure()
    plt.pie(n_users, labels=['Member', 'Casual'], autopct='%.2f%%', shadow=True)
    # .2f表示输出浮点数并保留两位小数。 % % 表示直接输出一个 %。

def main():
    year_member_type = collect_and_process_data()
    n_users =  analyze_data(year_member_type)
    save_and_show_results(n_users)


if __name__ == '__main__':
    main()