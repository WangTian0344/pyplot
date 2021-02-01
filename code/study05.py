# 条形图
import matplotlib.pyplot as plt

x = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
y = range(10,20)
font = {"family":"SimHei","size":"10"}
plt.figure(figsize=(10,8),dpi=80)
# rc设置全局字体
plt.rc("font",**font)
plt.rc("axes",unicode_minus=False)      # 坐标轴负号显示
plt.xticks(range(len(x)),x)
# 设置width绘制垂直条形图
plt.bar(range(len(x)),y,width=0.5)
# 设置height绘制垂直条形图
# plt.bar(range(len(x)),y,height=0.5)
for i in range(len(x)):
    plt.text(i,y[i],y[i])
plt.grid()
plt.savefig("../pictures/study05.png")
plt.show()