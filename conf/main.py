import os
import sys
import time
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)
time1=time.strftime('%Y-%m-%d-%M')

#windows
# os.chdir('f:/')
# DB_dir=os.getcwd()
# DB_DIR='%s\countdata' %DB_dir
# #DB_DIR='%s\countdata' %BASE_DIR
# DB_list=os.listdir(DB_DIR)
#DB_CSV='%s\countdata\%s.csv' %(DB_dir,time1)

#linux
DB_DIR='%s\DB' %BASE_DIR
DB_list=os.listdir(DB_DIR)




DB_CORE=r'%s\core' %BASE_DIR
DB_core=os.listdir(DB_CORE)

B2C_NONE=r'%s\DB\%s.txt' %(BASE_DIR,time1+'No')

B2C_none=r'%s\core\b2cnone'%BASE_DIR
DB_APPKEY=r'%s\core\Appkey' %BASE_DIR
B2C_USER=r'%s\core\b2cuser' %BASE_DIR
B2C_MULU=r'%s\core\b2cmulu' %BASE_DIR
B2C_ALL=r'%s\core\b2cport_all' %BASE_DIR
DB_CSV=r'%s\DB\%s.csv' %(BASE_DIR,time1)
B2C_PORT=r'%s\conf\b2c_new.txt' %BASE_DIR
DB_HOST='192.168.29.11'
DB_NAME='b2cplus'
DB_USER='palmb2c'
DB_PASSWD='palmb2c'
conn_sql='SELECT appkey,REMARK from appkey;'