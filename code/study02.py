# 绘制气温练习
from matplotlib import pyplot as plt
import random
x = range(121)
y = [random.randint(20,35) for i in range(121)]

x_label = ["{}:{}".format(10+i//60,i%60)for i in range(121)]

plt.figure(figsize=(20,8),dpi=80)
# x_label 对坐标轴的修饰 rotation 旋转角度
plt.xticks(list(x)[::5],x_label[::5],rotation=30)
plt.yticks(range(20,36),["{}℃".format(i) for i in range(20,36)])
# fontproperties 设置字体以显示中文
plt.xlabel("时间(分)",fontproperties="SimHei",fontsize = 15)
plt.ylabel("温度(摄氏度)",fontproperties="SimHei",fontsize = 15)
plt.title("10点到12点气温变化情况",fontproperties="SimHei",fontsize = 20)
# 网格
plt.grid()
plt.plot(x,y)
plt.savefig("../pictures/study02.png")
plt.show()