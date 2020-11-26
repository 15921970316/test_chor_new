import socket

import cou

import unit
from api.sk3 import xintiao, zhuce, CCPTX_Report, CCPRX_Report, BLINK_Report
from datetime import datetime
import threading
import time

class chor:
    def __init__(self):

        self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.Rx_seq = 0
        self.tts = 0
        self.Blink_seq = 0
        self.Blink_tts = 0
        self.filename = unit.BASE_DIR + "\data\Data.json"
        self.anchor_cfg_list = unit.read_name_data2(self.filename, "anchor_cfg")
        self.list = []
        for i in self.anchor_cfg_list:
            self.list.append(i)
        self.id=0
        print(self.id)

    # 分类接受打印引擎返回信息
    def Recv_info(self,ms):
        # print('分类接收打印引擎返回信息', ms)
        global bs

        try:
            if ms == b'':
                ...
            elif ms == 0 or ms == None:
                print("基站{}连接失败".format(self.id))
            elif ms[0] == 0x21:
                ...

                # print("基站心跳包3：",hex(ms[0]))
            elif ms[0] == 0x43:
                print("基站{}配置基站定位参数：".format(self.id), hex(ms[0]), hex(ms[1]), hex(ms[2]))
            elif ms[0] == 0x44:
                print("基站{}配置基站射频参数：".format(self.id), hex(ms[0]))
            elif ms[0] == 0x57:
                cou.rtls = 1
                print('基站{}定位开始：'.format(self.id), hex(ms[0]), ms[1])

                if ms[1] == 1:
                    bs = 1
                elif ms[1] == 0:
                    bs = 0
                else:
                    bs = 3
            elif ms[0] == 0x45:
                print("基站{}配置基站天线延迟参数：".format(self.id), hex(ms[0]))
            else:
                print(" 基站{}其他参数：".format(self.id), hex(ms[0]))
                # ms.hex().encode(encoding="utf-8"))
        except Exception as e:
            print('基站{}服务器连接失败--'.format(self.id), e)


    # 标签信息 无返回值
    def Blink_info(self):
        # 读取标签的addr文件
        filename = unit.BASE_DIR + "\data\Data.json"
        json1 = unit.read_name_data2(filename, "Tag_Addr_XYZ")
        # json2 = unit.read_name_data(filename, "Blik_time")
        # Blink_time = 1 / float(json2[0][0])
        # print('3基站Blink发送频率为:{}HZ'.format(json2[0][0]))
        #
        X = -1
        while True:
            sep_c = self.Blink_seq
            if X != sep_c:
                time1 = self.Blink_tts
                # time1 = cou.time3
                try:
                    n=0
                    for Tag_Addr in json1:
                        tt =  time1 + cou.BINK(Tag_Addr[1][0], Tag_Addr[1][1], self.id) - cou.BINK(Tag_Addr[1][0], Tag_Addr[1][1], 1)
                        self.sk.send(BLINK_Report(sep_c, Tag_Addr[0], tt))
                        n += 1
                    X = sep_c
                except Exception as e:
                    print('服务器连接失败-- ', e)
                ...


    # 在启动TDOA定位后，所有的基站都会向定位引擎发送时间同步包接收报告
    def CCPRX_Report3(self):
        X = -1
        print(self.id)

        while True:
            while True:
                # print(list[0][0])
                sep_c = self.Rx_seq
                if sep_c != X:
                    try:
                        t = self.tts + cou.BINK(self.list[self.id-1][1][0], self.list[self.id-1][1][1], 0)
                        self.sk.send(CCPRX_Report(sep_c, t, self.list[0][0]))
                        # sk.send(CCPRX_Report(sep_c, t))
                        # print('次基站CCPRX：', CCPRX_Report(sep_c, t))

                        cou.time3 = t
                        # t = cou.time3 + int(0.15 * 499.2e6 * 128.0)
                        X = sep_c
                        break
                    except Exception as e:
                        print('CCPRX_Report3', e)
                else:
                    ...
        # 计时器


    def time_x(self):
        t = 0b0000000000000000000000000000000000100110
        while True:
            if t >= 1099511627775:
                t = 0b0000000000000000000000000000000000000000
                cou.time3 = 0
            # report_name = os.path.dirname(os.path.abspath(__file__)) + "/report/test_info.html"
            # time.sleep(0.1)
            cou.time3 = cou.time3 + 1
            t += 1


    # 心跳间隔是2秒 2秒发送一个心跳包并且收到引擎一个心跳回访 一旦超时未收到双方连接立即中断
    def xintiao2(self):
        i = 0
        while True:
            try:
                # print(cou.time3)
                self.sk.send(xintiao())
                ms = self.sk.recv(1024)
                self.Recv_info(ms)
                i += 1
                time.sleep(2)
            except Exception as e:
                print('服务器连接失败--3', e)
                break

    def start(self,id):
        self.id = id
        while True:
            try:

                filename = unit.BASE_DIR + "\data\Data.json"
                json = unit.get_json_data(filename)
                self.sk.connect((json["ip"], json['port']))
                # sk.connect(('10.14.1.88', 59336))
                self.sk.send(zhuce(self.list[self.id-1][0]))
                # print('次基站3注册信息包:', zhuce())

                ms = self.sk.recv(1024)
                self.Recv_info(ms)
                ## 属于线程t的部分
                t1 = threading.Thread(target=self.xintiao2)
                t2 = threading.Thread(target=self.Blink_info)
                t3 = threading.Thread(target=self.CCPRX_Report3)
                # t4= threading.Thread(target=time_x)
                t1.start()
                # t4.start()
                while True:
                    if cou.rtls == 1:
                        t3.start()
                        t2.start()
                        break
                break
            except Exception as e:
                print('服务器连接失败33--', e)


