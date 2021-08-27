import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])

map = folium.Map(location=[lat[1], lon[1]], zoom_start=10, tiles='Stamen Terrain')
fg = folium.FeatureGroup(name='My Map')

map.save("Map1.html")