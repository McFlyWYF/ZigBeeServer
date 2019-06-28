# coding=gb18030

import serial  # ����serial��
import time  # ����time��
import pymysql  # ����pymysql��

log = 0  # ��һ��log�������ڼ�¼���ν��մ���
# s = serial.Serial('COM3', 115200, bytesize=8, parity='N', stopbits=1, timeout=1)

s = serial.Serial('COM2', 9600, timeout=2)  # �򿪴��ڣ����ô���
db = pymysql.connect("localhost", "root", "12345", "zigbee")  # �����ݿ⣬�������ݿ�
cursor = db.cursor()  # ���ݿ����
# cursor.execute("DROP TABLE IF EXISTS Monitor_Data")  # ������ڱ������´���
# creatTab = """CREATE TABLE Monitor_Data( # ������
#     LOG_ID INT NOT NULL,
#     D_ID CHAR(20) NOT NULL,
#     TIME CHAR(50),
#     T_DATA INT ,
#     H_DATA INT ,
#     L_DATA FLOAT )"""
# cursor.execute(creatTab)  # ִ�����ݿ����

while True:  # ����ѭ����ȡ����
    localtime = time.asctime(time.localtime(time.time()))  # time����������ӡ����ʱ��
    print(localtime)
    n = s.readline()  # ��ȡ����һ������
    # print(n)
    log += 1  # ���������¼+1
    print(log)
    data_pre = str(n)  # ǿ�����ַ�����ʽ

    # print(data_pre[0:3])
    data = data_pre[2:]  # ȡ��������
    # print(data)
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # ��������ʱ��ĸ�ʽ
    did = int(data[0:4])  # ����ȡ��Ч����
    td = float(data[4:6])
    hd = int(data[6:7])
    print(local_time, did, td, hd)  # ��ӡ����ڿ���̨

    sql = "INSERT INTO message(Person_ID,TIME,T_DATA,H_DATA)VALUES('%d','%s','%f','%d')" % (
    did, local_time, td, hd)  # �������ݿ�
    cursor.execute(sql)  # ִ�����ݿ����
    db.commit()  # �ύ

cursor.close()
db.close()