import pyecharts.options as opts
from pyecharts.charts import Map3D
from pyecharts.globals import ChartType

# 定义变量
data_pair = [
    ("广东", [113.2700, 23.1300, 995]), ("黑龙江", [127.9688, 45.368, 302]), ("内蒙古", [110.3467, 41.4899, 176]),
    ("吉林", [125.8154, 44.2584, 235]), ("辽宁", [123.1238, 42.1216, 469]), ("河北", [114.4995, 38.1006, 759]),
    ("天津", [117.4219, 39.4189, 356]), ("山西", [112.3352, 37.9413, 265]), ("陕西", [109.1162, 34.2004, 300]),
    ("甘肃", [103.5901, 36.3043, 204]), ("宁夏", [106.3586, 38.1775, 298]), ("青海", [101.4038, 36.8207, 186]),
    ("新疆", [87.9236, 43.5883, 57]), ("西藏", [91.1100, 29.9700, 38]), ("四川", [103.9526, 30.7617, 409]),
    ("重庆", [108.384366, 30.439702, 698]), ("山东", [117.1582, 36.8701, 797]), ("河南", [113.4668, 34.6234, 754]),
    ("江苏", [118.8062, 31.9208, 678]), ("安徽", [117.29, 32.0581, 897]), ("湖北", [114.3896, 30.6628, 698]),
    ("浙江", [119.5313, 29.8773, 783]), ("福建", [119.4543, 25.9222, 456]), ("江西", [116.0046, 28.6633, 853]),
    ("湖南", [113.0823, 28.2568, 661]), ("贵州", [106.6992, 26.7682, 145]), ("广西", [108.479, 23.1152, 509]),
    ("海南", [110.3893, 19.8516, 780]), ("上海", [121.4648, 31.2891, 856])
]

map3d = (
    # 3D地图
    Map3D(
        # 初始化配置项
        init_opts=opts.InitOpts(
            theme='white',  # 图表主题 white dark
            width='99vw',  # 图表画布宽度
            height='97vh',  # 图标画布长度
        )
    )
    # !!!!全局配置项!!!!
    .set_global_opts(
        # 标题配置项
        title_opts=opts.TitleOpts(
            title="3D地图+柱状图",  # 主标题
        ),
        # 视觉映射配置项
        visualmap_opts=opts.VisualMapOpts(
            is_show=True,  # 是否显示视觉映射配置
            max_=1000,  # 指定 visualMapPiecewise 组件的最大值
        ),
    )
    # !!!!系列配置项!!!!
    .set_series_opts(
        # 标签名称显示，默认为True
        label_opts=opts.LabelOpts(
            is_show=True  # 是否显示标签名字
        )
    )
    .add_schema(
        # 地图类型
        maptype='china',
        # 图元样式配置项
        itemstyle_opts=opts.ItemStyleOpts(
            # 图形的颜色
            color="#1661AB",
            # 描边宽度，默认不描边。
            border_width=0.8,
            # 图形的描边颜色。支持的颜色格式同 color，不支持回调函数。
            border_color="rgb(62,215,213)"
        ),
    )
    # 数据配置
    .add(
        # 系列名称，用于 tooltip 的显示，legend 的图例筛选
        series_name='人数',
        # 数据项 (坐标点名称，坐标点值)
        data_pair=data_pair,
        # 叠加图的类型（目前只支持 Bar3D，Line3D，Lines3D，Scatter3D）
        type_=ChartType.BAR3D,
        # 柱体大小
        bar_size=1,
    )
)
map3d.render("test4.html")