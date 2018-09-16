import numpy as np
import os
import matplotlib.pyplot as plt

data_path = './data/bikeshare'
data_filenames = ['temp.csv']


def collect_data():
    """
        数据收集
    """
    data_arr_list = []
    for data_filename in data_filenames:
        data_file = os.path.join(data_path, data_filename)
        data_arr = np.loadtxt(data_file, delimiter='，', dtype='str', skiprows=1)
        data_arr_list.append(data_arr)
    return data_arr_list


def process_data(data_arr_list):
    """
        数据处理
    """
    duration_F_str_list = []
    for data_arr in data_arr_list:
        duration_C_str = data_arr[:, 1]
        # 批量化处理C
        duration_Cln_str = np.core.defchararray.replace(duration_C_str, 'C', '')
        # 数据转化
        duration_F_str = 1.8*duration_Cln_str.astype('float')+32
        duration_F_str_list.append(duration_F_str)
        return duration_F_str_list


def analyze_data(duration_list):
    duration_mean_list = []
    for i, duration in enumerate(duration_list):
        duration_mean = np.mean(duration)
        print("华氏度：{}".format(duration_mean))
        duration_mean_list.append(duration_mean)
    return duration_mean_list


def show_data(duration_mean_list):
    plt.figure()
    plt.bar(range(len(duration_mean_list),duration_mean_list))
    plt.show()


def main():
    data_arr_list = collect_data()
    duration_list = process_data(data_arr_list)
    duration_mean_list = analyze_data(duration_list)
    show_data(duration_mean_list)


if __name__ == '__main__':
    main()
