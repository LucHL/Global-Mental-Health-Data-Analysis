import worldmap as wm
from random import randint

county_names = wm.list_county_names(map_name='usa')

print(county_names)





region = ["Alabama"]

opacity = [0.1]

results = wm.plot(region, opacity=opacity, cmap='Set1', map_name='usa')
