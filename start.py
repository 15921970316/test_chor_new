import random
import os
import json
from imp import reload

import unit

filename = unit.BASE_DIR + "\data\Bilk_data.json"
json2 = unit.read_name_data(filename, "Blik_time")

#
# # 函数调用
filename = unit.os.path.dirname(os.path.abspath(__file__)) +  "\data\Bilk_data.json"

file_new=os.path.dirname(os.path.abspath(__file__)) + "\\data\\xyz1.json"
# with open(filename, 'r') as f:
#     data = json.load(f)
    # data[0]['a'] = 'rect'
import sys
import argparse
reload(sys)
data={}

for i in range(10):
    a="a000000000000{}".format(i)
    x=random.randrange(1,100,1) #随机产生1-100，间隔为2随机整数
    y=random.randrange(1,100,1) #随机产生1-100，间隔为2随机整数
    xx='"{}",[{},{},0]'.format(a,x,y)
    data[a]=[x,y,0]
with open(file_new, 'r') as f:
    json_data = json.load(f)
    print(json_data['Tag_Addr_XYZ'])
    json_data['Tag_Addr_XYZ']=data
    print(json_data)
with open(file_new, 'w') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)
