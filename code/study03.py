# 多条曲线
import matplotlib.pyplot as plt
import random
x = range(20,41)
y1 = [random.randint(0,5) for i in range(21)]
y2 = [random.randint(0,5) for i in range(21)]
font = {"family":"SimHei","size":"10"}
plt.figure(figsize=(20,8),dpi=80)
# rc设置全局字体
plt.rc("font",**font)
plt.rc("axes",unicode_minus=False)      # 坐标轴负号显示
plt.xticks(x,["{}岁".format(i) for i in range(20,41)])
plt.yticks(range(0,6),["{}个".format(i) for i in range(0,6)])
plt.xlabel("年龄(岁)")
plt.ylabel("数量(个)")
plt.plot(x,y1,label="one",color="red",linestyle="--")
plt.plot(x,y2,label="two",color="blue",linestyle="-.")
plt.legend()
plt.savefig("../pictures/study03.png")
plt.show()