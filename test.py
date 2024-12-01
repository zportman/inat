import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Create a new figure
plt.figure(figsize=(8, 6))

# Set up a Basemap instance with the Robinson projection
# Center it on the U.S. Eastern region by setting lon_0 around -90 (Mississippi River)
m = Basemap(projection='robin', lon_0=-90, resolution='c',
            llcrnrlat=24, urcrnrlat=50,  # Latitude bounds (focus on the U.S.)
            llcrnrlon=-85, urcrnrlon=-60)  # Longitude bounds (focus on the Eastern U.S.)

# Draw coastlines and countries
m.drawcoastlines()
m.drawcountries()

# Show the map
plt.title('Eastern United States with Robinson Projection')
plt.show()
