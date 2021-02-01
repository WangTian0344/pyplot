# 散点图
import matplotlib.pyplot as plt
x1 = range(1,32)
x2 = range(41,72)
y1 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,27,16,17,20,14,15,15,15,19,21,22,22,22,23]
y2 = [26,26,28,19,28,19,21,17,16,19,18,20,19,22,23,17,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
font = {"family":"SimHei","size":"10"}
plt.figure(figsize=(20,8),dpi=80)
# rc设置全局字体
plt.rc("font",**font)
plt.rc("axes",unicode_minus=False)      # 坐标轴负号显示
_x = list(x1)+list(x2)
x_label = ["3月{}日".format(i) for i in range(1,32)]
x_label += ["10月{}日".format(i) for i in range(1,32)]
plt.xticks(_x,x_label,rotation=90)
plt.yticks(range(min(min(y1),min(y2)),max(max(y1),max(y2))),["{}℃".format(i) for i in range(min(min(y1),min(y2)),max(max(y1),max(y2)))])
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("某年北京3月和10月的最高气温")
plt.scatter(x1,y1,color="red",label="3月")
plt.scatter(x2,y2,color="blue",label="10月")
# 散点图连线
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.legend()
plt.savefig("../pictures/study04.png")
plt.show()