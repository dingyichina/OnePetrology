import  pandas as pd
from pyproj import CRS

import geopandas as gpd


if __name__ == '__main__':
    df = pd.read_excel("d:/北疆-精简的岩浆岩知识树.xlsx", header=2)
    gdf = gpd.GeoDataFrame(df,geometry=gpd.points_from_xy(df['longitude'],df['latitude']),crs=4326)
    print(gdf.head())
    # gdf.plot()

    m = gdf.explore(
        color='#40a9ff',
        #tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr=' ',
        width='100%',
        tooltip=False, # 关闭鼠标悬浮时的空白tooltip
        marker_type='circle_marker',


        style_kwds={
            'color': 'red',
            'fillOpacity': 0.4
        },
        highlight_kwds={
            'fillColor': 'white',
            'fillOpacity': 0.6
        },
        marker_kwds={
            'radius' : 6 # 点的半径，像素数，marker_type配合使用
           # 'icon': folium.map.Icon(icon='beer', prefix='fa')
        }
       )
    m.save('demo.html')
