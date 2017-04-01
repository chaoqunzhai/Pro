import os
import sys
import pymysql
import csv
import time,re


BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
time1=time.strftime('%Y-%m-%d-%M')

from conf import main
from conf import file_path
from bin import b2c_file
from png import parameter

class Hander(object):
    def __init__(self,username,number,userid,b2c_port):
        self.username=username
        self.number=number
        self.userid=userid
        self.b2c_port = b2c_port
        self.clean_core()
        time.sleep(0.5)
        self.file()
        self.connct_mysql()
        file_path.file_rename()
    def connct_mysql(self):
        self.conn = pymysql.connect(host=main.DB_HOST,
                                    port=3306,
                                    user=main.DB_USER,
                                    passwd=main.DB_PASSWD, db=main.DB_NAME,charset='utf8')
        self.cursor = self.conn.cursor()
        self.conn_sql=main.conn_sql
        self.db_sql(self.conn_sql)
        self.conn_close()
    def conn_close(self):
        self.cursor.close()
        self.conn.close()
    def file(self):
        self.DB_number=len(main.DB_list)
        if self.DB_number==0:exit()
        self.DBfile_number=0
        conn = 0
        for i in main.DB_list:
            core=main.DB_DIR + '\\'+i
            # print(''.join(main.DB_DIR,i))
            if os.path.isdir(core) == True:
                print('yes',i)
                self.DB_list2 = '%s\%s' % (main.DB_DIR, i)
                self.DB_file=os.listdir(self.DB_list2)
                if len(self.DB_file) > self.DBfile_number:
                    for e in range(len(self.DB_file)):
                        conn +=1
                        #print('file:文件目录%s,文件%s,个数为%s'%(i,self.DB_file[e],conn))
                        self.file_all='%s\%s' %(self.DB_list2,self.DB_file[e])
                        self.open_file(self.file_all,conn)
    def open_file(self,file_all,conn,*args):
        self.filelist = {}
        self.filelist[conn]=file_all
        count = 0
        for v in self.filelist:
            count += 1
            with open(main.DB_APPKEY,'a') as appkey,\
                    open(self.filelist.get(v),'r') as f,\
                    open(main.B2C_USER,'a') as b2c_user,\
                    open(main.B2C_MULU,'a')as e:                 #a+
                while 1:
                    line=f.readlines()
                    for j,x in enumerate(line):
                        j +=1
                        # print('目录:%s，当前文件为:%s,文件行数:%s,APPKKEY:%s,用户:%s,访问目录:%s'
                        #           %(self.filelist.get(v).split('\\')[-2],
                        #             self.filelist.get(v).split('\\')[-1],
                        #             j, x.split(',')[2],x.split(',')[3],x.split(',')[5]))
                        appkey.write(x.split(',')[2]+'\n')
                        b2c_user.write(x.split(',')[2]+'#'+x.split(',')[3]+'\n')
                        e.write(x.split(',')[2] +'#'+ x.split(',')[5])
                    if not line:break
    def b2c_user(self,row):
        with open(main.B2C_USER) as e:
            line=e.readlines()
            line=list(set(line))
            klist=[]
            dict01={}
            dict02 = {}
            for i in line:
                for k, v in enumerate(row):
                    #(appkey,user,mulu)=(i.split('-')[0],i.split('-')[1],i.split('-')[2])
                    (appkey, user)=(i.split('#')[0], i.split('#')[1])
                    if appkey == v[0]:
                        klist.append(k)
                        print('K:{},APPKEY:{},UserID:{}'.format(k,appkey,user))
                        break
            setklist=set(klist)
            for i in setklist:
                dict01.update({i:klist.count(i)})
                dict02.update({row[i][1]:str(klist.count(i))})
            return dict02
    def db_sql(self,conn_sql):
        self.DB_dict = {}
        results={}
        self.a=''
        self.cursor.execute(conn_sql)
        row = self.cursor.fetchall()
        if os.path.isfile(main.DB_APPKEY):
            with open(main.DB_APPKEY) as f:
                line = f.readlines()
                self.a=self.b2c_user(row)
                for k, v in enumerate(row):
                    v = list(v)
                    self.DB_dict[v[1]] = v[0]
                    for i in line:
                        if self.DB_dict[v[1]] in i:
                            number= line.count(i)
                           # print('显示数据库appkey，项目对应关系，以及number计算出的访问次数',v[1],self.DB_dict[v[1]],number)
                            results[v[1]]=[self.DB_dict[v[1]],number]
                            break
        self.sever_item(row)
        if results is not None:self.csv_handle(results,self.DB_dict)
    def sever_item(self,connect):
        ceshi_values=[]
        b2c_port_1,b2c_port_2= b2c_file.persion()
        for y in b2c_port_1:
            ceshi_values.append(b2c_port_1[y])
        if os.path.exists(main.B2C_MULU):
            with open(main.B2C_MULU) as f, open(main.B2C_ALL, 'w') as e:
                line=f.readlines()
                for k,v in enumerate(connect):
                    v=list(v)
                    for i in line:
                        (appkey,mulu)=(i.split('#')[0],i.split('#')[1])
                        if appkey == v[0]:
                            pattern=re.compile('|'.join(ceshi_values))
                            if pattern.findall(mulu):
                                for q in pattern.findall(mulu):
                                    port=b2c_port_2.get(q)
                                    #print('port',port)
                                    e.write(v[1] + '#' + port + '\n')  #写入用户+接口地址
                            else:
                                #e.write(v[1]+'None'+'\n')   # not mulu
                                e.write('None'+ v[1] + '\n')
                                with open(main.B2C_none,'a+') as q:
                                    q.write(v[1] +'#'+ mulu + '\n')
    def b2c_port_handle(self,*args):
        dict_handle={}
        start=time.clock()
        all_list=[]
        if os.path.exists(main.B2C_ALL):
            with open(main.B2C_ALL) as f:
                line=f.readlines()
                for i in line:
                    for z in i.split(','):
                        all_list.append(z)
            set_all=set(all_list)
            for i in set_all:
                dict_handle.update({i:all_list.count(i)})
        end=time.clock()
        print('计算时间为',end - start)
        return dict_handle

    def csv_handle(self,result,db_dict):
        ceshi_2=self.b2c_port_handle()
        print('计算目录访问次数结果',ceshi_2)
        ceshi = self.a
        notuser={}
        self.none_port()
        try:
            with open(main.DB_CSV, mode='w', newline='') as f:
                headers = [self.username, self.number, self.userid,self.b2c_port]
                writer = csv.DictWriter(f, headers)
                writer.writeheader()
                for i,k in enumerate(result):
                    for line in ceshi:
                        if line == k:
                            del db_dict[k]
                            notuser.update({k:{result[k][1]:ceshi[line]}})
                for i in db_dict:
                    notuser.update({i:{0:'0'}})
                #print('csv写入内容:',notuser)
                @parameter('png')
                def func(arg):
                    return arg
                func(notuser)
                for l in notuser:
                    for k in notuser[l]:
                        rok=[{self.username:l,
                                    self.number:k,
                                    self.userid:notuser[l][k]}]
                        writer.writerows(rok)
                        for port in ceshi_2:
                            if l in port:
                                port1=re.sub('{','',port.split(':')[0])
                                port2=port1.split('#')[-1].replace('\n','')
                                ror=[{self.b2c_port:str(port2) + str(ceshi_2[port])}]
                                writer.writerows(ror)
        except PermissionError as e:exit('请关闭excel')
        # for port in ceshi_2:
        #     print('test-2',re.sub('{','',port.split(':')[0]),re.sub('{','',port.split(':')[1]),ceshi_2[port])
    def clean_core(self):
        os.chdir(main.DB_CORE)
        for i in main.DB_core:
            os.remove(i)
    def none_port(self):
        none_list = []
        with open(main.B2C_none) as q:
            with open(main.B2C_NONE, 'w') as f:
                NONE = q.readlines()
                for z_1 in NONE:
                    none_list.append(z_1)
                set_none = set(none_list)
                for z_2 in set_none:
                    (a,b)=(z_2.split('#')[0],z_2.split('#')[-1])
                    numbers=none_list.count((z_2))
                    f.write(a +'#'+ str(numbers) +'#'+ b+'\n')

if __name__ == '__main__':
    Hander('客户名称', '访问次数', '访问客户个数','b2c接口访问次数',)







