import numpy as np


# 1. 读取csv数据文件
load_arr = np.loadtxt('./data/bikeshare/temp.csv', dtype='str', delimiter=',', skiprows=1)
# 2. 去除“C”符号
clin_temp_str_col = np.core.defchararray.replace(load_arr, 'C', '')
# 3. 将str文件转化为float文件
data_arr = clin_temp_str_col.astype('float')


month_list = [1, 2, 3]
for month in month_list:
    # 4. 构造布尔型数组
    # data_arr[:, 0]表示月份列
    month_bool_arr = data_arr[:, 0] == month
    # 5. 使用布尔型数组进行数据过滤
    month_temp_arr = data_arr[month_bool_arr][:, 1]
    # 6. 统计最大值、最小值及平均值
    month_max_temp = np.max(month_temp_arr)
    month_min_temp = np.min(month_temp_arr)
    month_ave_temp = np.mean(month_temp_arr)
    # 7. 输出统计结果
    # :.2f表示保留小数点后2位输出
    print("第{}个月，温度最大{:.2f}摄氏度,最小{:.2f}摄氏度，平均{:.2f}摄氏度。".format(month, month_max_temp, month_min_temp, month_ave_temp))
