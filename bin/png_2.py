from pylab import *
import re
import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


mpl.rcParams['font.sans-serif'] = ['SimHei']

fig, ax = plt.subplots()
width=0.7
class Png(object):
    def core(self,data):
        xlist = []
        num1 = []
        num2 = []
        for i in data:
            for d in data[i]:
                x, x_1, x_2 = i, d, data[i][d]
                if int(x_1) and int(x_2) > 0:
                    xlist.append(x)
                    num1.append(x_1)
                    num2.append(x_2)

        N = (len(xlist))
        ax.set_xticklabels((xlist))
        ind = np.arange(N)
        #print(num1,num2,ind)
        nums2=[int(i) for i in num2]
        print(num1, num2,nums2,xlist)
        rects1 = ax.bar(ind,num1, width, color='b')
        rects2 = ax.bar(ind,nums2, width, color='y')
        self.rest(rects1)
        self.rest(rects2)
        ax.legend((rects1[0], rects2[0]), ('访问量', '客户量'))
        ax.set_title('B2C')
        plt.show()
        # plt.savefig(format='png', dpi=300)
    def rest(self,rests):
        for rect in rests:
            print('rect',rect)
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width(), height, '%d' % int(height), )
def run(data):
    a=Png()
    a.core(data)
# if __name__ == '__main__':
#     data = {'车旺大卡': {129: '49'}, '乐行汽车': {0: '0'}, 'testzhang': {0: '0'}, '斯润天朗-众泰': {0: '0'}, '汽车小子': {0: '0'},
#             '车音网': {0: '0'}, '四维TSP': {0: '0'}, '美行-吉利项目': {0: '0'}, '东风裕隆': {622: '14'}, '美行-赛格': {0: '0'},
#             '迪恩杰': {0: '0'}, '测试': {48: '1'}, '机场达人(航旅纵横)': {504: '1'}, '前海智云谷': {0: '0'}, '美行-路畅': {0: '0'},
#             '优途': {0: '0'}, '美行-马自达': {541: '42'}, '中交兴路': {0: '0'}, '飞驰镁物': {0: '0'}, '四海万联': {0: '0'},
#             '美赛达': {0: '0'}, 'Android路况通': {339: '38'}, '众泰汽车': {17: '2'}, '车友互联': {0: '0'}, '科达讯飞': {0: '0'},
#             '梦擎2': {0: '0'}, 'testwrq': {0: '0'}, '福信福通': {0: '0'}, '美行-后装': {0: '0'}, '车托帮': {0: '0'},
#             '远特科技': {0: '0'}, '车联天下': {0: '0'}, '悦驾科技': {0: '0'}, '美行马自达测试': {0: '0'}, 'iphone路况通': {142: '17'},
#             '拨测': {2544: '3'}, '上海梦擎': {0: '0'}, '美行-航盛东风裕隆': {0: '0'}}
#     p1=Png()
#     p1.core(data)
