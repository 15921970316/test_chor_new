import multiprocessing
import socket
import unit
from api.sk import xintiao, zhuce, CCPTX_Report, CCPRX_Report, BLINK_Report
import threading
import time

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
import cou

s = 0
filename = unit.BASE_DIR + "\data\Data.json"
anchor_cfg_list = unit.read_name_data2(filename, "anchor_cfg")
list = []
for i in anchor_cfg_list:
    list.append(i)

# 分类接受打印引擎返回信息
def Recv_info(ms):
    # print('分类接收打印引擎返回信息', ms)
    global bs

    try:
        if ms == b'':
            ...
        elif ms == 0 or ms == None:
            print("连接失败")
        elif ms[0] == 0x21:
            ...
            # print("基站心跳包1：",ms)
        elif ms[0] == 0x43:
            print("配置基站1定位参数：", hex(ms[0]), hex(ms[1]), hex(ms[2]))
        elif ms[0] == 0x44:
            print("配置基站1射频参数：", hex(ms[0]))
        elif ms[0] == 0x57:
            print('1定位开始：', hex(ms[0]), ms[1])
            cou.rtls = 1

            if ms[1] == 1:
                bs = 1
            elif ms[1] == 0:
                bs = 0
            else:
                bs = 3
        elif ms[0] == 0x45:
            print("配置基站1天线延迟参数：", hex(ms[0]))
        else:
            print(" 其他参数：", hex(ms[0]))
            # ms.hex().encode(encoding="utf-8"))
    except Exception as e:
        print('服务器连接失败--1', e)


# 标签信息 无返回值
def Blink_info():
    x = 0
    # print(datetime.datetime.now(), 'Blink_info')
    # 读取标签的addr文件
    filename = unit.BASE_DIR + "\data\Data.json"

    json1 = unit.read_name_data2(filename, "Tag_Addr_XYZ")

    json2 = unit.read_name_data(filename, "Blik_time")
    Blink_time = 1 / float(json2[0][0])
    # print('Blink发送频率为:{}HZ'.format(json2[0][0]))
    t = 0
    sep = 0
    while True:
        try:
            if sep > 255:
                sep = 0

            time2 = cou.time

            def blink():
                n = 0
                for Tag_Addr in json1:
                    # tt = cou.BINK(Tag_Addr[1][0], Tag_Addr[1][1], 1)
                    # t = time2 + tt
                    # print(BLINK_Report(sep, Tag_Addr[0], time2))
                    sk.send(BLINK_Report(sep, Tag_Addr[0], time2))
                    # print(Tag_Addr[0],Tag_Addr[1][0], Tag_Addr[1][1])
                    n += 1

            def s():


                def ad(id):
                    st = xinxi8.chor()
                    st.Blink_seq = sep
                    st.Blink_seq = sep
                    st.Blink_seq = sep
                    st.Blink_seq = sep
                    st.Blink_tts = time2
                    st.Blink_tts = time2
                    st.Blink_tts = time2
                    st.Blink_tts = time2
                    st.start(id)
                t7 = threading.Thread(target=ad, args=(4,))
                t8 = threading.Thread(target=ad, args=(3,))
                t9 = threading.Thread(target=ad, args=(2,))
                t8.start()
                t7.start()
                t9.start()
            t1 = threading.Thread(target=blink)
            t2 = threading.Thread(target=s)
            t1.start()
            t2.start()
            sep += 1
            if sep == 256:
                sep = 0
            time.sleep(Blink_time)

        except    Exception as e:
            print('服务器连接失败--1111', e)


# 在启动TDOA定位后，所有的基站都会向定位引擎发送时间同步包接收报告
def CCPTX_Report1():
    t = 0 + cou.time
    Txseq = 0
    while True:
        try:
            if Txseq > 255:
                Txseq = 0
                # print('我到了255了 ccp1')
            t = cou.time
            if t > 1099511627775:
                cou.time = 0

            def ccp():
                sk.send(CCPTX_Report(Txseq, t))
                # print('主基站CCPTX：', Txseq, t)

            def s():

                def ad(id):

                    st = xinxi8.CCPRX_Report3()
                    st.Rx_seq = Txseq
                    st.Rx_seq = Txseq
                    st.Rx_seq = Txseq
                    st.Rx_seq = Txseq
                    st.tts = t
                    st.tts = t
                    st.tts = t
                    st.tts = t
                    st.start(id)
                t7 = threading.Thread(target=ad, args=(4,))
                t8 = threading.Thread(target=ad, args=(3,))
                t9 = threading.Thread(target=ad, args=(2,))
                t8.start()
                t7.start()
                t9.start()


            t1 = threading.Thread(target=s)
            t2 = threading.Thread(target=ccp)
            t2.start()
            t1.start()
            # cou.time=t
            # print('CCPTX_Report1----', Txseq, t )
            time.sleep(0.15)
            Txseq += 1
            if Txseq == 256:
                Txseq = 0
        except Exception as e:
            print('CCPTX_Report1', e)


# 计时器
def time_x():
    t = 0b0000000000000000000000000000000000000000
    cou.time = 0
    while True:
        if t >= 1099511627775:
            t = 0b0000000000000000000000000000000000000000
            cou.time = 0

        cou.time += 1000
        # print(cou.time)
        t += 1


# 心跳间隔是2秒 2秒发送一个心跳包并且收到引擎一个心跳回访 一旦超时未收到双方连接立即中断
def xintiao2():
    i = 0
    while True:

            sk.send(xintiao())
            # print('心跳：', xintiao())
            ms = sk.recv(1024)
            Recv_info(ms)
            i += 1
            time.sleep(2)

def anchor():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    list1=[]
    j=0
    XML = ''
    for i in anchor_cfg_list:
        list1.append(i)
        if j==0:
            XML='<req type="anchor cfg"><anchor addr="{}" x="{}" y="{}" z="0" syncref="1" follow_addr="0" lag_delay="0"></anchor>'.format(list[0][0],list[0][1][0],list[0][1][1])
        else:
            XML2='<anchor addr="{}" x="{}" y="{}" z="0" ' \
              'syncref="0" follow_addr="0" lag_delay="0"><syncrefanchor ' \
              'addr="{}" rfdistance="0"/></anchor>'.format(list1[j][0],list1[j][1][0],list1[j][1][1],list1[0][0])
            XML=XML+XML2
        j+=1

    XML=XML+'</req>'
    print('基站数量为：{} \n对应的坐标值为：{}'.format(len(anchor_cfg_list),list1))
    json = unit.get_json_data(filename)
    sk.connect((json["ip"], json['chor_port']))
    # XML = '<req type="anchor cfg"><anchor addr="01aa6083cf111111" x="0"' \
    #       ' y="0" z="0" syncref="1" follow_addr="0" lag_delay="0"></anchor>' \
    #       '<anchor addr="01aa6083cf222222" x="100" y="0" z="0" ' \
    #       'syncref="0" follow_addr="0" lag_delay="0"><syncrefanchor ' \
    #       'addr="01aa6083cf111111" rfdistance="0"/></anchor>' \
    #       '<anchor addr="01aa6083cf333333" x="100" y="100" z="0" syncref="0" ' \
    #       'follow_addr="0" lag_delay="0"><syncrefanchor addr="01aa6083cf111111" ' \
    #       'rfdistance="0"/></anchor><anchor addr="01aa6083cf444444" x="0" y="100" z="0" ' \
    #       'syncref="0" follow_addr="0" lag_delay="0"><syncrefanchor addr="01aa6083cf111111" ' \
    #       'rfdistance="0"/></anchor></req>'


    # print(XML)
    sk.send(XML.encode('utf-8'))#发送基站坐标配置信息
    sk.recv(1024)

    time.sleep(0.5)
    xml2 = '<req type="rtls start"/>'
    sk.send(xml2.encode('utf-8'))#发送启动定位命令
    sk.recv(1024)
    # print("基站配置结果：", str(msg, 'utf8'))
try:
    filename = unit.BASE_DIR + "\data\Data.json"
    json = unit.get_json_data(filename)
    sk.connect((json["ip"], json['port']))
    t1 = threading.Thread(target=xintiao2)
    t1.start()

    x = input('服务器连接成功！\n请输入需要随机的标签数量【直接按回车键则使用文件里原数据 】：')
    rate = input('\n请输入标签频率HZ【直接按回车键则使用文件里原数据 】：')
    if x =="":
        x=0
    if rate =="":
        rate=0
    unit.rw_xyz(int(x),int(rate))  # x随机生成10个坐标 rate标签频率
    sk.send(zhuce(list[0][0]))
    # print('主基站注册信息包:', zhuce())
    ms = sk.recv(1024)
    Recv_info(ms)
    anchor()
    ## 属于线程t的部分
    t2 = threading.Thread(target=Blink_info)
    t3 = threading.Thread(target=CCPTX_Report1)
    t4 = threading.Thread(target=time_x)
    t4.start()

    import xinxi8
    def ad(id):

        st = xinxi8.chor()
        st.start(id)

    t7 = threading.Thread(target=ad, args=(4,))
    t8 = threading.Thread(target=ad, args=(3,))
    t9 = threading.Thread(target=ad, args=(2,))

    while True:
        if cou.rtls == 1:
            t3.start()
            t2.start()
            t8.start()
            t7.start()
            t9.start()
            break
except Exception as e:
    print(e)

## 属于线程t的部分
# t1.join() # join是阻塞当前线程(此处的当前线程时主线程) 主线程直到Thread-1结束之后才结束
# t2.join()
