import matplotlib.pyplot as plt
import numpy as np

def plot_parallel_lines(x, scale2):
    # 將 x 陣列的元素都乘上 0.01
    x = [element * 0.01 for element in x]

    # 計算 scale1，為 x 陣列的累加和
    scale1 = np.cumsum(x)

    # 設定圖表
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.set_ylim(-1, 2)  # 限制y軸範圍，讓兩條線在0和1的位置

    # 畫第一條線（在 y=1 的位置）
    ax.hlines(1, min(scale1), max(scale1), color='blue', linewidth=2, label='Line 1')
    for i, val in enumerate(scale1):
        ax.plot(val, 1, 'bo')  # 畫刻度
        ax.text(val, 1.1, f'{val:.2f}', ha='center')  # 標記刻度值

    # 畫第二條線（在 y=0 的位置）
    ax.hlines(0, min(scale2), max(scale2), color='green', linewidth=2, label='Line 2')
    for x in scale2:
        ax.plot(x, 0, 'go')  # 畫刻度
        ax.text(x, -0.1, str(x), ha='center')  # 標記刻度值

    # 隱藏x軸和y軸
    ax.axis('off')

    # 顯示圖表
    plt.show()

# 定義 x 陣列和 scale2
x = [171.52658662092622, 702.7406886858749, 202.75750202757501, 242.48302618816683,
     333.66700033366703, 175.07002801120447, 214.5002145002145, 103.59473738734071,
     1025.6410256410256, 261.5746795710175, 892.0606601248885, 2320.185614849188,
     334.67202141900935, 2040.8163265306125]
# 定義 x 陣列和 scale2
x = [0, 171.52658662092622, 702.7406886858749, 202.75750202757501, 242.48302618816683,
     333.66700033366703, 175.07002801120447, 214.5002145002145, 103.59473738734071,
     1025.6410256410256, 261.5746795710175]
scale2 = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40]  # 測試用的第二條線刻度
plot_parallel_lines(x, scale2)
