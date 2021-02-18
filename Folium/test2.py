# =============================================================================
# # -*- coding: utf-8 -*-
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
ex = {'경도' : [127.061026,128.047883],
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
    
loc = [(127.061026,37.493922), 
       (128.047883,37.505675)]
    
folium.PolyLine(loc,
                color='red',
                weight = 15,
                ).add_to(m)

m.save('path2.html')
