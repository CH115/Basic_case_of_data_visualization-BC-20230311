"""
动态GDP柱状图绘制
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import *

# 打开文件
f = open('1960-2019全球GDP数据.csv', 'r', encoding='GB2312')
data_lines = f.readlines()
# 关闭文件
f.close()

# 删除第一天数据
data_lines = data_lines[1:]
# 将数据转换为字典，格式为：
# {年份:[[国家,gdp],[国家,gdp],[国家,gdp]...],年份:[[国家,gdp],[国家,gdp],[国家,gdp]...],......}
data_dict = dict()
for line in data_lines:
    line = line.split(',')
    year = int(line[0])
    country = line[1]
    gdp = float(line[2])

    # try:
    #     data_dict[year].append([country, gdp])
    # except KeyError:
    #     data_dict[year] = []
    #     data_dict[year].append([country, gdp])

    if year not in data_dict.keys():
        data_dict[year] = []
    data_dict[year].append([country, gdp])


# 排序年份
year_list = data_dict.keys()
year_list = sorted(year_list)    # 把年份排序
for year in year_list:        # 将每一年gdp排名前八的数据取出来
    data_year = data_dict[year]     # 取出这一年的数据来，即[[国家,gdp],[国家,gdp],[国家,gdp]...]
    data_year.sort(key=lambda element: element[1], reverse=True)   # 将取出的数据按照gdp排名
    data_dict[year] = data_year[:8]      # 切片取出gdp排名前八的数据

# 创建时间线对象
timeline = Timeline({'theme': ThemeType.LIGHT})

# for循环每一年的数据，基于每一年的数据，创建每一年的bar对象
# 在for中，将每一年的bar对象都添加到时间线中
for year in year_list:      # 这个for循环可以并到上面那个for循环中去，这里是为了将数据排序和创建bar及时间线分开来
    bar = Bar()
    lx = list()
    ly = list()
    for line in data_dict[year]:      # 对每一年中的数据进行处理
        lx.append(line[0])            # x轴的数据为年份
        ly.append(line[1]/100000000)   # y轴的数据为gdp，要以亿为单位
    bar.add_xaxis(lx[::-1])
    bar.add_yaxis('GDP(亿)', ly[::-1], label_opts=LabelOpts(position='right'))
    bar.reversal_axis()
    # 设置每一年的图表的标题，全局配置选项
    bar.set_global_opts(
        title_opts=TitleOpts(title=f'{year}年全球前8GDP数据'),  # 标题配置项
    )
    timeline.add(bar, str(year))    # 时间轴上为年份


# 设置时间线自动播放
timeline.add_schema(
    play_interval=1000,  # 自动播放的时间间隔，单位毫秒
    is_timeline_show=True,  # 是否在自动播放的时候，显示时间线
    is_auto_play=True,      # 是否自动播放
    is_loop_play=True       # 是否循环自动播放
)

# 绘图
timeline.render('动态GDP柱状图绘制.html')

