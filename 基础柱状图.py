from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

# 使用Bar构建基础柱状图
bar = Bar()
# 添加x轴数据
bar.add_xaxis(['中国', '美国', '英国'])
# 添加y轴数据,设置数值标签在右侧
bar.add_yaxis('GDP', [30, 20, 10], label_opts=LabelOpts(position='right'))
# 反转x轴和y轴
bar.reversal_axis()


# 生成柱状图
bar.render('基础柱状图.html')