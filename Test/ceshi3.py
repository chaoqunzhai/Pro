# -*- coding: gbk -*-
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
N = 9
menMeans = [142, 504, 129, 622, 48, 541, 339, 2544, 17]
ind = np.arange(N)
width = 0.6

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='b')
womenMeans = [2,1, 49, 3,2,6,5,10,11]
rects2 = ax.bar(ind+width, womenMeans, width, color='r')
ax.set_title('B2C')
date={'车旺大卡': {129: '49'}, '乐行汽车': {0: '0'}, 'testzhang': {0: '0'}, '斯润天朗-众泰': {0: '0'}, '汽车小子': {0: '0'}, '车音网': {0: '0'}, '四维TSP': {0: '0'}, '美行-吉利项目': {0: '0'}, '东风裕隆': {622: '14'}, '美行-赛格': {0: '0'}, '迪恩杰': {0: '0'}, '测试': {48: '1'}, '机场达人(航旅纵横)': {504: '1'}, '前海智云谷': {0: '0'}, '美行-路畅': {0: '0'}, '优途': {0: '0'}, '美行-马自达': {541: '42'}, '中交兴路': {0: '0'}, '飞驰镁物': {0: '0'}, '四海万联': {0: '0'}, '美赛达': {0: '0'}, 'Android路况通': {339: '38'}, '众泰汽车': {17: '2'}, '车友互联': {0: '0'}, '科达讯飞': {0: '0'}, '梦擎2': {0: '0'}, 'testwrq': {0: '0'}, '福信福通': {0: '0'}, '美行-后装': {0: '0'}, '车托帮': {0: '0'}, '远特科技': {0: '0'}, '车联天下': {0: '0'}, '悦驾科技': {0: '0'}, '美行马自达测试': {0: '0'}, 'iphone路况通': {142: '17'}, '拨测': {2544: '3'}, '上海梦擎': {0: '0'}, '美行-航盛东风裕隆': {0: '0'}}


xlist = []
temp=()
for i in date:
    for d in date[i]:
        x,x_1,x_2 = i,d ,date[i][d]
        print(x,x_1,x_2)
        if int(x_1) and int(x_2) >0:
            xlist.append(x)
            tupe1=temp + (x_1,)
            tupe2=temp + (x_2,)
            print(xlist,len(xlist),tupe1,tupe2)
            ax.set_xticklabels((xlist))

# def test(tupe1,tupe2):

# N = 6
# menMeans = (21, 2, 13, 44, 55,6)
# ind = np.arange(N)
# width = 0.6
#
# fig, ax = plt.subplots()
# rects1 = ax.bar(ind, menMeans, width, color='b')
# womenMeans = (5000, 132, 34, 220, 125,610)
# rects2 = ax.bar(ind+width, womenMeans, width, color='r')

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width(), height, '%d' % int(height),)

autolabel(rects1)
autolabel(rects2)
ax.legend( (rects1[0],rects2[0]), ('访问量', '客户量') )
plt.show()