import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm  # 引入 colormap 模組

def plot_3d_bar_chart(x_values, y_layers, z_values_list):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    yticks = list(range(len(y_layers)))
    xticks = list(range(len(x_values)))
    for k, z_values in zip(yticks, z_values_list):
        # 確保 x_values 和 z_values 長度一致
        if len(x_values) != len(z_values):
            raise ValueError("每層的 z_values 必須和 x_values 的長度一致。")
        
        # 根據 z 值計算顏色，使用從白到黑的 Greys 配色方案
        norm = plt.Normalize(1, 1.75)  # 標準化 z 值範圍
        colors = cm.viridis_r(norm(z_values))
        # 繪製 bar 圖，將 x_values 作為類別標籤
        ax.bar(np.arange(len(x_values)), z_values, zs=k, zdir='y', color=colors, alpha=0.8)

    # 設定軸標籤和刻度
    ax.set_xlabel('X $(10^-3)$')
    ax.set_ylabel('T')
    ax.set_zlabel('$\\frac{F_{max}}{F_{min}}$')
    ax.set_yticks(yticks)
    ax.set_xticks(xticks)
    ax.set_xticklabels(x_values)
    ax.set_yticklabels(y_layers)

    plt.show()

# 使用範例
x_values = np.arange(1e-3, 4e-3, 2e-4)
x_values = x_values[0:11]
print(len(x_values))
x_values = [round(x * (10 ** 3), 2) for x in x_values]
y_layers = np.arange(1, 21, 1)
z_values_list = []

for i in range(21):
    one_z_list = []
    for j in range(11):
        x, y, z = map(float, input().split(' '))
        one_z_list.append(z)
    z_values_list.append(one_z_list)

plot_3d_bar_chart(x_values, y_layers, z_values_list)