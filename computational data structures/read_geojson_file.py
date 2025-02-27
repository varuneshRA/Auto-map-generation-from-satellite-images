import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoJSON file containing the road network dataset
road_network = gpd.read_file('buildings_sample.geojson')

# Plot the road network
road_network.plot()
plt.title('Road Network')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
