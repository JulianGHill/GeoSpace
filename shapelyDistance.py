from shapely.geometry import Point, Polygon

# Define the polygon and the point
polygon_coords = [
    (-72.281059, 42.927402),
    (-72.2810805, 42.9259644),
    (-72.2782588, 42.925823),
    (-72.2782588, 42.9274177),
    (-72.2810912, 42.9273942)
]

point_coords = (-72.2761452, 42.9287846)

# Create Shapely objects
polygon = Polygon(polygon_coords)
point = Point(point_coords)

# Calculate the distance from the point to the polygon
distance = point.distance(polygon)

# Convert the distance to kilometers (assuming the input is in degrees and using Haversine formula for better accuracy)
from math import radians, sin, cos, sqrt, atan2

def haversine(lon1, lat1, lon2, lat2):
    R = 6371.0  # Radius of the Earth in kilometers

    dlon = radians(lon2 - lon1)
    dlat = radians(lat1 - lat2)

    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

# Extract the nearest point on the polygon to the given point
nearest_point = polygon.exterior.interpolate(polygon.exterior.project(point))

# Calculate the Haversine distance
distance_km = haversine(point.x, point.y, nearest_point.x, nearest_point.y)

print(f"The distance from the point to the closest edge of the polygon is {distance_km:.2f} kilometers.")
