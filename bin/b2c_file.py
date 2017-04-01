import os
import sys

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from conf import main

#城区图示 /traffic/graphics_traffic.service 提取
def persion():
    result={}
    resultv={}
    with open(main.B2C_PORT,encoding='utf-8') as e:
        for line in e.readlines():
                #print('服务名称:%s,访问地址:%s' %(line.split(',')[0],line.split(',')[1]))
                #ceshi=re.sub('http|tc|\d|/|','',line.split(',')[1].split('?')[0])
            result_1=line.split(',')[1].split('?')[0].split('/')[-2:]
            result_2='/'+result_1[0]+'/'+result_1[1]
            result.update({line.split(',')[0]:result_2})
            resultv.update({result_2:line.split(',')[0]})
    return result,resultv