import json

infile = open('US_fires_9_14.json','r')

firedata = json.load(infile)

bright, lats, lons = [],[],[]


for fire in firedata:
    if fire["brightness"] > 450:
        bri = fire["brightness"]
        lat = fire["latitude"]
        lon = fire["longitude"]
        bright.append(bri)
        lats.append(lat)
        lons.append(lon)

print(bright[:5])
print(lats[:5])
print(lons[:5])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':bright,
    'marker':{
        'size':[.03*b for b in bright],
        'color':bright,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'}
    }
}]


my_layout = Layout(title="US Fires 9-14-20 to 9-20-20")

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='US_fires_9_14.html')