# -*- coding: utf-8 -*-
import folium
m = folium.Map(location = [40.720, -73.993],
               zoom_start = 15)

loc = [(40.720, -73.993),
       (40.721, -73.996)]

folium.PolyLine(loc,
                color='red',
                weight = 15,
                opacity=0.8).add_to(m)

m.save('path.html')
