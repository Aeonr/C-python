import geopandas as gpd

shapefile_path = '/Volumes/Aeon_HDD/地级市POI兴趣点/2014POI/2014/生活服务.shp'
gdf = gpd.read_file(shapefile_path, engine='fiona', encoding='utf-8')
print(gdf.head())  # 显示前几行数据

gdf.to_csv(
    '/Users/aeon/Downloads/生活服务.csv', encoding='utf-8')

print('done')
