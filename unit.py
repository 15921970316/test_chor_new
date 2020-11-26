import os
import random

server_state = -10
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 通用断言函数
import json


def assert_common(scode, success, code, message, response, self):
    self.assertEqual(scode, response.status_code)  #
    self.assertEqual(success, response.json().get(""))  #
    self.assertEqual(scode, response.json().get(""))  #
    self.assertIn(message, response.json().get(""))  #


#
# 1 定义读取数据的函数，并从外界接收文件名
def read_data(filename):
    # 2 使用内置函数open打开外界传入的文件名
    with open(filename, mode='r', encoding='utf-8') as f:
        # 3 使用内置模块json加载文件
        jsonData = json.load(f)
        # 定义一个存放数据的空列表
        result_list = list()
        # 拼接数据成一个嵌套元组的形式
        for data in jsonData:
            result_list.append(tuple(data.values()))
        #   return 返回
        f.close()
    return result_list


def get_json_data(json_path):
    # 获取json里面数据

    with open(json_path, 'rb') as f:
        # 定义为只读模型，并定义名称为f
        params = json.load(f)
        # 加载json文件中的内容给params
    f.close()
    # 关闭json读模式
    return params


# 1 定义读取模块数据的函数，并从外界接收数据文件路径和要读取的接口模块
def read_name_data(filename, name):
    # 2 使用内置函数open打开外界传入的文件名
    with open(filename, mode='r', encoding='utf-8') as f:
        # 3 使用内置模块json加载文件
        jsonData = json.load(f)
        # 4 读取数据
        data = jsonData.get(name)
        # 定义存放数据的空列表
        result_list = list()
        # 讲数据转化为元组后添加到列表中
        result_list.append(tuple(data.values()))
        # 5 打印结果，并return返回
        f.close()
    return result_list

def read_name_data2(filename, name):
    # 2 使用内置函数open打开外界传入的文件名
    with open(filename, mode='r', encoding='utf-8') as f:
        # 3 使用内置模块json加载文件
        jsonData = json.load(f)
        # 4 读取数据
        data = jsonData.get(name)

        # 定义存放数据的空列表
        result_list = list()
        # 讲数据转化为元组后添加到列表中
        result_list.append(data)
        # 5 打印结果，并return返回
        f.close()
    return data.items()
def read_name_data3(filename, name):
    # 2 使用内置函数open打开外界传入的文件名
    with open(filename, mode='r', encoding='utf-8') as f:
        # 3 使用内置模块json加载文件
        jsonData = json.load(f)
        # 4 读取数据
        data = jsonData.get(name)

        # 5 打印结果，并return返回
        f.close()

    return data
#标签数量和坐标配置
def rw_xyz(count,rate):
    filename = os.path.dirname(os.path.abspath(__file__)) + "\data\Data.json"
    data = {}
    # data.values()
    w = 100000000000001
    if count!=0:
        for i in range(count):

            a = "a{}".format(w)
            w+=1
            x = random.randrange(0, 100, 1)  # 随机产生1-100，间隔为1随机整数
            y = random.randrange(0, 100, 1)  # 随机产生1-100，间隔为1随机整数
            data[a] = [x, y, 0]
        with open(filename, 'r') as f:
            json_data = json.load(f)
            json_data['Tag_Addr_XYZ'] = data
            json_data['Blik_time']["HZ"] = rate
        with open(filename, 'w') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
            dictList1 = []
            for key in data:
                dictList1.append('"{}":{}'.format(key, data[key]))

            print("\n设置的标签频率为：{} HZ.\n系统随机生成的 {} 个标签和坐标分别为：".format(rate, count), dictList1)
            f.close()
    elif count==0:
        if rate > 0:
            with open(filename, 'r') as f:
                json_data = json.load(f)

                json_data['Blik_time']["HZ"] = rate
            with open(filename, 'w') as f:
                json.dump(json_data, f, ensure_ascii=False, indent=4)
                dictList1 = []
                for key in data:
                    dictList1.append('"{}":{}'.format(key, data[key]))
                f.close()
                print("\n设置的标签频率为：{} HZ.\n已存在的 {} 个标签和坐标分别为：".format(rate ,len(json_data['Tag_Addr_XYZ'])), json_data['Tag_Addr_XYZ'])

        else:
            with open(filename, 'r') as f:
                json_data = json.load(f)

                rate=json_data['Blik_time']["HZ"]
                f.close()

                print("\n设置的标签频率为：{} HZ.\n已存在的 {} 个标签和坐标分别为：".format(rate ,len(json_data['Tag_Addr_XYZ'])), json_data['Tag_Addr_XYZ'])

#基站坐标配置
# def anchor_cfg(count,rate):
#     filename = os.path.dirname(os.path.abspath(__file__)) + "\data\Data.json"
#     data = {}
#     # data.values()
#     w = 100000000000001
#     if count!=0:
#         for i in range(count):
#
#             a = "a{}".format(w)
#             w+=1
#             x = random.randrange(0, 100, 1)  # 随机产生1-100，间隔为1随机整数
#             y = random.randrange(0, 100, 1)  # 随机产生1-100，间隔为1随机整数
#             data[a] = [x, y, 0]
#         with open(filename, 'r') as f:
#             json_data = json.load(f)
#             json_data['anchor_cfg'] = data
#         with open(filename, 'w') as f:
#             json.dump(json_data, f, ensure_ascii=False, indent=4)
#             dictList1 = []
#             for key in data:
#                 dictList1.append('"{}":{}'.format(key, data[key]))
#
#             print("设置的标签频率为：{} HZ.\n系统随机生成的 {} 个标签和坐标分别为：".format(rate, count), dictList1)
#             f.close()
#     elif count==0:
#         with open(filename, 'r') as f:
#             json_data = json.load(f)
#             json_data['Blik_time']["HZ"] = rate
#         with open(filename, 'w') as f:
#             json.dump(json_data, f, ensure_ascii=False, indent=4)
#             dictList1 = []
#             for key in data:
#                 dictList1.append('"{}":{}'.format(key, data[key]))
#
#             print("设置的标签频率为：{} HZ.\n已存在的 {} 个标签和坐标分别为：".format(rate ,len(json_data['Tag_Addr_XYZ'])), json_data['Tag_Addr_XYZ'])
#             f.close()
#

# #
# filename = os.path.dirname(os.path.abspath(__file__)) + "\data\Bilk_data.json"
# json1 =  read_name_data2(filename, "Tag_Addr_XYZ")
# #
# # # json1 = rw_xyz(filename, 5)
# # print(json1 )
# #
# for i in json1:
#     print(i,i[0],i[1][0].type())
