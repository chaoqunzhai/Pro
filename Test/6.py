
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
data = ((3, 5), (10, 3), (100, 30), (500, 800), (50, 1))
# data=(('车友互联',), ('优途',), ('科达讯飞',), ('G4',), ('G5',))

plt.xlabel("客户名称")
plt.ylabel("访问数")
plt.title("B2C")
plt.plot()
# plt.yscale('log')

dim = len(data[0])
w = 0.75
dimw = w / dim

x = np.arange(len(data))

for i in range(len(data[0])):
   # print(i,(d[i] for d in data))
   #  x = [d for d in data]
    y = [d[i] for d in data]
    b = plt.bar(x + int(i) * dimw, y, dimw, bottom=0.1)

plt.xticks(x + dimw / 2, map(str, x))

plt.show()