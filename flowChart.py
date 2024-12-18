import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取 CSV 文件并提取特定列
data = pd.read_csv('preprocessed_data_Benign.csv')
flow_packets = data['Flow Packets/s'][:10000]  # 将 'Flow Packets/s' 列的数据提取到数组

print(np.var(flow_packets))
# 绘制折线图
# plt.plot(flow_packets, marker='o', linestyle='-')  # 使用 'o' 标记点，'-' 为实线
# plt.title('Flow Packets per Second')
# plt.xlabel('Index')
# plt.ylabel('Flow Packets/s')
#
# # 显示图表
# plt.show()
