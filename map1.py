import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])

map = folium.Map(location=[lat[1], lon[1]], zoom_start=10, tiles='Stamen Terrain')
fg = folium.FeatureGroup(name='My Map')

# When iterating through two lists, need to use the zip fn
for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup='This is a Marker', icon=folium.Icon(color='blue')))
map.add_child(fg)

map.save("Map1.html")