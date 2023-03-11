"""
地图可视化开发
要注意，json中数据省市名称都没有后缀，我们在把数据添加到data中时要对其做出相应的修改
"""
import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 读取数据文件
f = open('../疫情.txt', 'r', encoding='UTF-8')
data = f.read()
# 关闭文件
f.close()

# 取到个省份数据
# 将字符串json转换为python字典
data_dict = json.loads(data)
# 从字典中取出省份数据
province_data_list = data_dict['areaTree'][0]['children']
# 组装每个省份和确诊人数为元组，并将各个省的数据都封装入列表中
data_list = []
for province_data in province_data_list:
    # 对数据中省市部分做出修改，只有加上省市等后缀，才能正确显示
    if province_data['name'] in ['北京', '天津', '上海', '重庆']:
        province_data['name'] = province_data['name'] + '市'
    elif province_data['name'] in ['香港', '澳门']:
        province_data['name'] = province_data['name'] + '特别行政区'
    elif province_data['name'] in ['内蒙古', '西藏']:
        province_data['name'] = province_data['name'] + '自治区'
    elif province_data['name'] == '新疆':
        province_data['name'] = province_data['name'] + '维吾尔自治区'
    elif province_data['name'] == '宁夏':
        province_data['name'] = province_data['name'] + '回族自治区'
    elif province_data['name'] == '广西':
        province_data['name'] = province_data['name'] + '壮族自治区'
    else:
        province_data['name'] = province_data['name'] + '省'
    # 将数据添加到列表中
    data_list.append((province_data['name'], province_data['total']['confirm']))

# 创建地图对象
map = Map()
# 添加数据
map.add('全国疫情地图', data_list, 'china')
# 设置全局配置，定制分段的视觉映射
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
