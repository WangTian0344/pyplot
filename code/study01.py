# 基础功能
import matplotlib.pyplot as plt

x = range(2,26,2)
y = [15,14,14.5,17,20,25,26,26,24,22,18,15]
# 传入x y绘制曲线图
# figsize 图片大小 dpi 像素
plt.figure(figsize=(20,8),dpi=80)
# 绘制x轴刻度
plt.xticks(range(2,25))
# 绘制y轴刻度
plt.yticks(range(min(y),max(y)+1))
plt.plot(x,y)
# 保存图片
plt.savefig("../pictures/study01.png")
plt.show()