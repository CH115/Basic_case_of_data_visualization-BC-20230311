# 某公司，有2份数据文件，现需要对其进行分析处理，计算每日的销售额并以柱状图表的形式进行展示。
# 1月份数据是普通文本，使用逗号分割数据记录，从前到后分别是（日期，订单id，销售额，销售省份）
# 2月份数据是JSON数据，同样包含（日期，订单id，销售额，销售省份）

from file_define import TextFileReader, JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

txt = TextFileReader('2011年1月销售数据.txt')
js = JsonFileReader('2011年2月销售数据JSON.txt')
jan_data: list[Record] = txt.read_data()
feb_data: list[Record] = js.read_data()

# 将两个月份的数据合并为一个list
all_data: list[Record] = jan_data + feb_data

# 开始计算数据
# 计算后的数据为{日期：销售额，日期：销售额，...}
data_dict = {}  # 计算后的数据存储在这个字典中
for line in all_data:  # for循环遍历数据list，将每月的销售额累加，最后全部存储到字典中去
    if line.date in data_dict.keys():
        data_dict[line.date] += line.money
    else:
        data_dict[line.date] = line.money

# 数据可视化
# 得出每日的销售额，输出为列表，或则可以直接使用data_dict.values 输出字典中的全部的值，但是要使用list()将其格式化
money_list = list()
for key in data_dict:
    money_list.append(data_dict[key])

# 使用Bar构建基础柱状图
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
# 添加x轴数据
bar.add_xaxis(list(data_dict.keys()))
# 添加y轴数据,设置数值标签在右侧
bar.add_yaxis('销售额', money_list, label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title='每日销售额')
)
# 生成柱状图
bar.render('数据分析案例.html')