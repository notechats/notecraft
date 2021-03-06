import numpy as np
import pandas as pd
from plyfile import PlyData


def t2():
    file_dir = '/Users/liangtaoniu/workspace/dataset/ply/data_qinghuamen/groundtruth data/qinghuamenG.ply'  # 文件的路径
    plydata = PlyData.read(file_dir)  # 读取文件
    data = plydata.elements[0].data  # 读取数据
    data_pd = pd.DataFrame(data)  # 转换成DataFrame, 因为DataFrame可以解析结构化的数据
    data_np = np.zeros(data_pd.shape, dtype=np.float)  # 初始化储存数据的array
    property_names = data[0].dtype.names  # 读取property的名字
    for i, name in enumerate(property_names):  # 按property读取数据，这样可以保证读出的数据是同样的数据类型。
        print(name)
        data_np[:, i] = data_pd[name]
    return data_pd


t2()
