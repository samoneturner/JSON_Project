import json

infile = open("eq_data_30_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")

eq_data = json.load(
    infile
)  # python recogonozes it as a dictionary and put it in the outfile as a dictionary

json.dump(
    eq_data, outfile, indent=5
)  # indient 4 means it indents 4 times in the outfile

# Print the type of object eq_data is and the number of earthquakes
# Create a list of mags, lats, and longs

list_of_eqs = eq_data["features"]

print(len(list_of_eqs))

mags, lats, lons, hover_text = [], [], [], []

for eq in list_of_eqs:
    if eq["properties"]["mag"] > 5:
        mag = eq["properties"]["mag"]
        lon = eq["geometry"]["coordinates"][0]
        lat = eq["geometry"]["coordinates"][1]
        title = eq["properties"]["title"]
        mags.append(mag)
        lats.append(lat)
        lons.append(lon)
        hover_text.append(title)

print(mags[:10])
print(lats[:10])
print(lons[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# data = Scattergeo(lon=lons, lat=lats)

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hover_text,
        "marker": {
            "size": [5 * mag for mag in mags],
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]


my_layout = Layout(title="Global Earthquake")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="global_earthquakes.html")
