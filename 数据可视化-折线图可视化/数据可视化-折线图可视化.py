
"""
数据可视化-折线图可视化
1.查看json数据，发现数据不规范，首先需要处理数据
2.利用json可视化网站，查看json数据中的层级关系，将json转换为python字典后，获取所需要的数据部分
"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts, ToolboxOpts

# 处理数据
f_us = open('美国.txt', 'r', encoding='UTF-8')
us_data = f_us.read()
f_jp = open('日本.txt', 'r', encoding='UTF-8')
jp_data = f_jp.read()
f_in = open('印度.txt', 'r', encoding='UTF-8')
in_data = f_in.read()
# 去掉不合json规范的开头
us_data = us_data.replace('jsonp_1629344292311_69436(', '')
jp_data = jp_data.replace('jsonp_1629350871167_29498(', '')
in_data = in_data.replace('jsonp_1629350745930_63180(', '')
# 去掉不合json规范的结尾(也可以使用切片[:-2])
us_data = us_data.replace(');', '')
jp_data = jp_data.replace(');', '')
in_data = in_data.replace(');', '')
# json 转python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
# 获取trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']
# 获取日期数据，用于x轴，取2020年（到314下标结束）
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]
# 获取确认数据，用于y轴，取2020年（到314下标结束）
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 得到折线图对象
line = Line()   # 构建折线图对象

# 添加x轴数据
line.add_xaxis(us_x_data)   # x轴共用，只添加一个国家的即可
# 添加y轴数据
line.add_yaxis('美国确诊人数', us_y_data, label_opts=LabelOpts(is_show=False))  # 添加美国的y轴数据,不显示各个点的数据
line.add_yaxis('日本确诊人数', jp_y_data, label_opts=LabelOpts(is_show=False))  # 添加日本的y轴数据,不显示各个点的数据
line.add_yaxis('印度确诊人数', in_y_data, label_opts=LabelOpts(is_show=False))  # 添加印度的y轴数据,不显示各个点的数据

# 全局配置选项
line.set_global_opts(
    title_opts=TitleOpts(title='2020年美日印三国确诊人数对比折线图', pos_left='center', pos_bottom='1%'),  # 标题配置项
    toolbox_opts=ToolboxOpts(is_show=True),   # 工具箱配置项
)

# 生成图表
line.render()

# 关闭文件
f_us.close()
f_jp.close()
f_in.close()



