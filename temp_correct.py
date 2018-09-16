import numpy as np

# 1.读取文件
data_arr = np.loadtxt('./data/bikeshare/temp.csv', dtype='str', delimiter=',', skiprows=1)

# 2. 获取temperature列的记录，即所有行的第1列数据
c_temp_str_col = data_arr[:, 1]
# 3. 批量化替换字符串中的特殊字符
clin_temp_str_col = np.core.defchararray.replace(c_temp_str_col, 'C', '')
# 4. 类型转换
c_temp_col = clin_temp_str_col.astype('float')
# 5.实现公式进行批量化操作
f_temp_col = 1.8*c_temp_col+32
print('摄氏度：')
print(c_temp_col)
print('华氏度：')
print(f_temp_col)
