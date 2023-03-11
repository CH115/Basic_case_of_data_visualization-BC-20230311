"""
河南省疫情地图构建
要注意，json中数据市名称都没有后缀，我们在把数据添加到data中时要对其做出相应的修改
数据来源中不包括济源市，要手动添加
"""
import json

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 读取数据文件
f = open('../疫情.txt', 'r', encoding='UTF-8')
data = f.read()
# 关闭文件
f.close()

# 获取河南省数据
# 先将数据转换为python字典
data_dict = json.loads(data)
# 取到河南省数据
cities_data = data_dict['areaTree'][0]['children'][3]['children']

# 准备数据为元组并放入list
data_list = list()
for city_data in cities_data:
    city_data['name'] = city_data['name'] + '市'
    data_list.append((city_data['name'], city_data['total']['confirm']))

# 手动添加济源市的数据
data_list.append(('济源市', 5))

# 构建地图
map = Map()
map.add('河南省疫情地图', data_list, '河南')

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,    # 是否显示
        is_piecewise=True,   # 是否分段
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
            {"min": 100, "max": 499, "label": "99-499人", "color": "#FF9966"},
            {"min": 500, "max": 999, "label": "499-999人", "color": "#FF6666"},
            {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#CC3333"},
            {"min": 10000, "label": "10000以上", "color": "#990033"}
        ]

    )
)

# 绘图
map.render()