import geopandas as gpd
import matplotlib.pyplot as plt

# Path to the shapefile
shapefile_path = "/Users/mac/Desktop/Programming_Stuff/morocco/ma_shp"

# Load the specific layer for Morocco
morocco_data = gpd.read_file(shapefile_path, layer="ma")

# Inspect the loaded data
print(morocco_data.head())
print(morocco_data.columns)

# Plot the map if geometries exist
fig, ax = plt.subplots(figsize=(10, 8))
morocco_data.plot(ax=ax, color="lightblue", edgecolor="black")
ax.set_title("Map of Morocco", fontsize=16)
ax.axis("off")
plt.show()
