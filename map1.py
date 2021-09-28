import folium
import pandas

vdata = pandas.read_csv('Volcanoes.txt')
vlat = list(vdata['LAT'])
vlon = list(vdata['LON'])
velev = list(vdata['ELEV'])
vname = list(vdata['NAME'])

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

map = folium.Map(location=[vlat[1], vlon[1]], zoom_start=6, tiles='Stamen Terrain')
folium.TileLayer('Open Street Map').add_to(map)
folium.TileLayer('Stamen Toner').add_to(map)
folium.TileLayer('Stamen Water Color').add_to(map)
folium.TileLayer('cartodbpositron').add_to(map)
folium.TileLayer('cartodbdark_matter').add_to(map)

fgv = folium.FeatureGroup(name='Volcanoes')

# When iterating through two lists, need to use the zip fn
for lt, ln, el, nm in zip(vlat, vlon, velev, vname):
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(iframe), color=color_producer(el), fill_opacity=0.7, fill=True))
    # fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.CustomIcon(icon_image='volcano.png', icon_size=(20,20))))

fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),  
style_function=lambda x: {'fillColor':'red' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'yellow'}))

#=> line breaks are allowed in python if within brackets

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")