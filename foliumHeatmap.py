import pandas as pd
import numpy as np
import folium
from folium.plugins import HeatMap
import webbrowser

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

# URL template for the local map tiles (adjust this according to your tile structure)
tiles_url = 'http://localhost:8000/{z}/{x}/{y}.png'

# Create a map centered around the mean latitude and longitude
center = [0, 0]  # Centering at (0, 0) for a global view
m = folium.Map(location=center, zoom_start=2, tiles=tiles_url, attr='Local Map')

# Create and add the heatmap layer
HeatMap(locations).add_to(m)

# Save the map to an HTML file
map_path = 'world_heatmap.html'
m.save(map_path)

# Automatically open the map in the default web browser
webbrowser.open(map_path)
