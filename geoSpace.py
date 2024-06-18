from shapely.geometry import Polygon
from shapely.geometry.polygon import orient
import requests

def get_data_points(polygon_coords):
    # Function to interact with your API to get data points within the polygon
    # Replace the URL and parameters as per your API's requirements
    url = "YOUR_API_ENDPOINT"
    response = requests.post(url, json={"polygon": polygon_coords})
    if response.status_code == 200:
        return response.json()  # Assumes the API returns a JSON list of data points
    else:
        return []

def expand_polygon(polygon, distance_km):
    # Expand the polygon by the specified distance (in kilometers)
    # 1 degree of latitude is approximately 111 km, so we convert km to degrees
    distance_deg = distance_km / 111
    return polygon.buffer(distance_deg)

def find_data_with_expansion(initial_polygon_coords, step_km=1):
    # Convert the input list of coordinates to a Shapely Polygon
    initial_polygon = Polygon(initial_polygon_coords[0])

    # Check for data points in the initial polygon
    data_points = get_data_points(initial_polygon_coords)
    if data_points:
        return data_points

    # If no data points found, expand the polygon until we find data points
    current_polygon = initial_polygon
    while not data_points:
        current_polygon = expand_polygon(current_polygon, step_km)
        # Orient the polygon to ensure it is counter-clockwise
        current_polygon = orient(current_polygon, sign=1.0)
        expanded_coords = [list(current_polygon.exterior.coords)]
        data_points = get_data_points(expanded_coords)

    return data_points

# Example usage
initial_polygon_coords = [
    [
        [-72.2809303, 42.9275042],
        [-72.2810161, 42.9258858],
        [-72.2789776, 42.9256423],
        [-72.2790742, 42.927402],
        [-72.280941, 42.9275042]
    ]
]

data_points = find_data_with_expansion(initial_polygon_coords)
print(data_points)
