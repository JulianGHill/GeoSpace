import pandas as pd
import numpy as np
import folium
from folium.plugins import HeatMap

# Step 1: Generate random latitude and longitude points
num_points = 100
lats = np.random.uniform(low=-90.0, high=90.0, size=num_points)
lons = np.random.uniform(low=-180.0, high=180.0, size=num_points)

# Create a DataFrame
data = {'latitude': lats, 'longitude': lons}
df = pd.DataFrame(data)

# Save to a CSV file
df.to_csv('data.csv', index=False)

# Step 2: Create the heatmap using folium
# Load your data
df = pd.read_csv('data.csv')

# Create a list of locations for the heatmap
locations = df[['latitude', 'longitude']].values.tolist()

# Create a map centered around the mean latitude and longitude
center = [0, 0]  # Centering at (0, 0) for a global view
m = folium.Map(location=center, zoom_start=2)  # Zoom level for a world map

# Create and add the heatmap layer
HeatMap(locations).add_to(m)

# Example polygon coordinates (you can define your own polygon)
polygon_coords = [
    (45.5236, -122.6750),
    (45.5347, -122.7085),
    (45.5304, -122.6780),
    (45.5268, -122.6695)
]

# Add polygon to map
folium.Polygon(locations=polygon_coords, color='blue', fill=True, fill_color='blue', fill_opacity=0.2).add_to(m)

# Save the map to an HTML file
map_path = 'world_heatmap_with_polygon.html'
m.save(map_path)

# Open the map in the default web browser
import webbrowser
webbrowser.open(map_path)
