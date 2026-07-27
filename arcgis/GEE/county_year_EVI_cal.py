import ee
import time


# ============================================================
# 1. 基本参数：需要根据你自己的 GEE 账号和区县矢量修改
# ============================================================
PROJECT_ID = 'county-data-cal'
COUNTY_ASSET = 'users/Aeon/countyshp_rename'

COUNTY_ID_FIELD = 'county_code'
COUNTY_NAME_FIELD = 'county'
PROVINCE_FIELD = 'province'

START_YEAR = 2001
END_YEAR = 2024

EXPORT_FOLDER = 'GEE_China_County_EVI'
INDEX_NAME = 'EVI'

try:
    ee.Initialize(project=PROJECT_ID)
except Exception:
    ee.Authenticate()
    ee.Initialize(project=PROJECT_ID)

# 中国大致范围，用于影像筛选，避免使用复杂区县边界筛选影像
CHINA_BOUNDS = ee.Geometry.Rectangle([73, 18, 135, 54])

# 导出字段
SELECTORS = [
    'county_code',
    'county',
    'province',
    'year',
    'month',
    'image_count',
    INDEX_NAME
]

# reduceRegions 参数
SCALE = 250
TILE_SCALE = 8

# 每提交一个任务暂停几秒，避免短时间提交过快
SLEEP_SECONDS = 1

# ============================================================
# 2. 初始化 GEE
# ============================================================

try:
    ee.Initialize(project=PROJECT_ID)
except Exception:
    ee.Authenticate()
    ee.Initialize(project=PROJECT_ID)

print('GEE initialized.')


# ============================================================
# 3. 读取区县边界
# ============================================================

counties = ee.FeatureCollection(COUNTY_ASSET)

# ============================================================
# 4. MOD13Q1 质量控制函数
#    DetailedQA bits 0-1:
#    0 = good quality
#    1 = check other QA
#    2 = probably cloudy
#    3 = not produced
#    这里保留 0 和 1，与 NDVI 脚本保持一致
# ============================================================

def mask_mod13q1(image):
    qa = image.select('DetailedQA')
    vi_quality = qa.bitwiseAnd(3)
    mask = vi_quality.lte(1)
    return image.updateMask(mask)


def prepare_evi(image):
    image = mask_mod13q1(image)
    evi = image.select('EVI').multiply(0.0001).rename(INDEX_NAME)
    evi = evi.updateMask(evi.gte(-1).And(evi.lte(1)))
    return evi.toFloat().copyProperties(image, ['system:time_start'])


# ============================================================
# 5. 构建某年某月的 EVI 月度合成影像
# ============================================================

def get_monthly_image(year, month):
    start_date = ee.Date.fromYMD(year, month, 1)
    end_date = start_date.advance(1, 'month')

    collection = (
        ee.ImageCollection('MODIS/061/MOD13Q1')
        .filterBounds(CHINA_BOUNDS)
        .filterDate(start_date, end_date)
        .map(prepare_evi)
    )

    image_count = collection.size()

    monthly_image = ee.Image(
        ee.Algorithms.If(
            image_count.gt(0),
            collection.mean().rename(INDEX_NAME).toFloat(),
            ee.Image.constant(-9999).rename(INDEX_NAME).toFloat()
        )
    )

    return monthly_image.set({
        'year': year,
        'month': month,
        'image_count': image_count
    })


# ============================================================
# 6. 计算区县均值并导出
# ============================================================

def export_one_month(year, month):
    image = get_monthly_image(year, month)
    image_count = image.get('image_count')

    stats = image.reduceRegions(
        collection=counties,
        reducer=ee.Reducer.mean(),
        scale=SCALE,
        tileScale=TILE_SCALE
    )

    def format_feature(f):
        return ee.Feature(None, {
            'county_code': f.get(COUNTY_ID_FIELD),
            'county': f.get(COUNTY_NAME_FIELD),
            'province': f.get(PROVINCE_FIELD),
            'year': year,
            'month': month,
            'image_count': image_count,
            INDEX_NAME: f.get('mean')
        })

    stats = stats.map(format_feature)

    task_name = f'{INDEX_NAME}_{year}_{month:02d}'

    task = ee.batch.Export.table.toDrive(
        collection=stats,
        description=task_name,
        folder=EXPORT_FOLDER,
        fileNamePrefix=task_name,
        fileFormat='CSV',
        selectors=SELECTORS
    )

    task.start()
    print(f'Started task: {task_name}')


# ============================================================
# 7. 批量逐月提交任务
# ============================================================

for year in range(START_YEAR, END_YEAR + 1):
    for month in range(1, 13):
        export_one_month(year, month)
        time.sleep(SLEEP_SECONDS)

print('All EVI monthly export tasks have been submitted.')
