import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])

html = '''
<h4>Volcano Info:</h4>
Name: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
'''

def color_producer(elevation):
    if elevation < 1200:
        return 'green'
    elif 1200 <= elevation < 2000:
        return 'blue'
    elif 2000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[lat[1], lon[1]], zoom_start=7, tiles='Stamen Terrain')
fg = folium.FeatureGroup(name='My Map')

# When iterating through two lists, need to use the zip fn
for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color_producer(el))))
map.add_child(fg)

map.save("Map1.html")