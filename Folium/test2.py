# -*- coding: utf-8 -*-
# =============================================================================
# from pandas import DataFrame
# import folium
# m = folium.Map(location = [40.720, -73.993],
#                zoom_start = 15)
# 
# loc = [(40.720, -73.993),
#        (40.721, -73.996)]
# 
# folium.PolyLine(loc,
#                 color='red',
#                 weight = 15,
#                 opacity=0.8).add_to(m)
# 
# m.save('path.html')
# =============================================================================


##################################################################
from pandas import DataFrame
import folium
m = folium.Map([127.028726, 37.546718], zoom_start = 8)
ex = {'경도' : [127.061026,127.047883],
      '위도' : [37.493922,37.505675],
      '구분' : ['음식','음식']}

ex = DataFrame(ex)
lat = ex['위도'].mean()
long = ex['경도'].mean()

#지도 띄우기
m = folium.Map([lat,long],zoom_start=9)

for i in ex.index:
    sub_lat = ex.loc[i,'위도']
    sub_long = ex.loc[i, '경도']
    title = ex.loc[i,'구분']
    folium.Marker([sub_lat,sub_long], tooltip=title).add_to(m)
    
folium.PolyLine([(ex['경도'][0], ex['위도'][0]), (ex['경도'][1], ex['위도'][1])],
                color = 'red',
                weight = 15,
                opacity = 0.8).add_to(m)

m.save('path2.html')