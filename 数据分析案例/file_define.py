"""
和文件相关的类定义
"""
import json
from data_define import Record


# 先定义一个抽象类，用来做顶层设计，确定有哪些功能需要实现
class FileReader:
    def read_data(self) -> list[Record]:
        """读取文件的数据，将读到的每一条数据都转换为Record对象，并通过list封装他们并返回"""

    pass


# 读取文本文件的类
class TextFileReader(FileReader):
    def __init__(self, path: str):
        self.path = path  # 文件路径

    # 实现抽象方法
    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding='UTF-8')
        data = f.readlines()
        f.close()
        data_list = list()
        for line in data:
            line = line.strip()
            line = line.split(',')
            record = Record(line[0], line[1], int(line[2]), line[3])
            data_list.append(record)
        return data_list


# 读取json文件
class JsonFileReader(FileReader):
    def __init__(self, path: str):
        self.path = path  # 文件路径

    # 实现抽象方法
    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding='UTF-8')
        data = f.readlines()  # 读取文件，读出的格式为json
        f.close()
        data_list = list()
        for line in data:
            line = json.loads(line)   # 将读出的json文件转化为python的列表
            record = Record(line['date'], line['order_id'], line['money'], line['province'])
            data_list.append(record)
        return data_list


if __name__ == '__main__':
    txt = TextFileReader('2011年1月销售数据.txt')
    js = JsonFileReader('2011年2月销售数据JSON.txt')
    list1 = txt.read_data()
    list2 = js.read_data()
    for line in list1:
        print(line)
    for line in list2:
        print(line)
