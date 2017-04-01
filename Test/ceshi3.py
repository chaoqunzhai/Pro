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
date={'������': {129: '49'}, '��������': {0: '0'}, 'testzhang': {0: '0'}, '˹������-��̩': {0: '0'}, '����С��': {0: '0'}, '������': {0: '0'}, '��άTSP': {0: '0'}, '����-������Ŀ': {0: '0'}, '����ԣ¡': {622: '14'}, '����-����': {0: '0'}, '�϶���': {0: '0'}, '����': {48: '1'}, '��������(�����ݺ�)': {504: '1'}, 'ǰ�����ƹ�': {0: '0'}, '����-·��': {0: '0'}, '��;': {0: '0'}, '����-���Դ�': {541: '42'}, '�н���·': {0: '0'}, '�ɳ�þ��': {0: '0'}, '�ĺ�����': {0: '0'}, '������': {0: '0'}, 'Android·��ͨ': {339: '38'}, '��̩����': {17: '2'}, '���ѻ���': {0: '0'}, '�ƴ�Ѷ��': {0: '0'}, '����2': {0: '0'}, 'testwrq': {0: '0'}, '���Ÿ�ͨ': {0: '0'}, '����-��װ': {0: '0'}, '���а�': {0: '0'}, 'Զ�ؿƼ�': {0: '0'}, '��������': {0: '0'}, '�üݿƼ�': {0: '0'}, '�������Դ����': {0: '0'}, 'iphone·��ͨ': {142: '17'}, '����': {2544: '3'}, '�Ϻ�����': {0: '0'}, '����-��ʢ����ԣ¡': {0: '0'}}


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
ax.legend( (rects1[0],rects2[0]), ('������', '�ͻ���') )
plt.show()