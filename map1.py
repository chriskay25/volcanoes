import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])

html = '''
<h4>Volcano: %s</h4>
Height: %s m
'''

map = folium.Map(location=[lat[1], lon[1]], zoom_start=7, tiles='Stamen Terrain')
fg = folium.FeatureGroup(name='My Map')

# When iterating through two lists, need to use the zip fn
for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nm, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='blue')))
map.add_child(fg)

map.save("Map1.html")