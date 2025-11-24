from pyinaturalist import *
import csv
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


"""
#this no work because it gives insufficient information wah. gotta download
project = 224372 #the introduced bees umbrella project

species =  52785 #Megachile sculpturalis

response = get_observations(taxon_id = species, project_id= project) 


for bee in response: 
    pprint (bee)


pprint(response)
"""

introduced_bees = pd.read_csv("observations-644848-introduced_bees.csv", sep=',', on_bad_lines = "skip", index_col=False, dtype='unicode', usecols = ['observed_on', 'latitude', 'longitude', 'taxon_species_name'])

#get year from date
introduced_bees['observed_on'] = pd.to_datetime(introduced_bees['observed_on'])
introduced_bees['year'] = introduced_bees['observed_on'].dt.year

#lets just try with sculpturalis first

sculpturalis = introduced_bees[introduced_bees['taxon_species_name'] == "Megachile sculpturalis"]


print ("Megachile sculpturalis", sculpturalis)


lat = sculpturalis['latitude'].astype(float).tolist()
lon = sculpturalis['longitude'].astype(float).tolist()

print ("lat", len(lat), lat)
print ("lon", len(lon), lon)


#set up the mappity map


#FIRST - make a map of all records FWS used to assess

fig, ax = plt.subplots(figsize=(12, 6))
fig.tight_layout(pad=-0.1) 
fig.subplots_adjust(wspace = 0.05, top = 0.98)


#change resolution to c for faster
"""map = Basemap(resolution='h',projection='aea',
    llcrnrlon=-127, llcrnrlat=30,   # lower left corner (lon, lat)
    urcrnrlon=-80,  urcrnrlat=60,   # upper right corner (lon, lat)
    lat_1=29.5, lat_2=45.5,         # standard parallels (good for US-wide)
    lon_0=-96,
    ax=ax) #whole affinis area"""


m = Basemap(projection='merc',
            llcrnrlon=-135,
            llcrnrlat=24,
            urcrnrlon=-50,
            urcrnrlat=55,
            resolution='l',
            ax=ax)



m.drawstates()
m.drawcountries()

m.drawmapboundary(fill_color='lightblue')
m.fillcontinents(color='white',lake_color='lightblue')

lons, lats = m(lon, lat)
m.scatter(lons, lats, marker = 'o', color='r', linewidth=0.5, edgecolors='black', s=7, zorder=5 ) # 'ro' for red circles



plt.show()

#so can you make a function to calculate the color based on year, add that to the dataframe, and then pass that to the scatter??????
#could also set up auto calcuate map size by just getting min and max lats and longs and adding a buffer and plugging into map....



"""
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def get_color_gradient_by_year(years, start_year, end_year, colormap_name='viridis'):
    
    #Generates a list of RGB colors forming a gradient based on a list of years.

    #Args:
    #    years (list or array-like): A list or array of year values.
    #    start_year (int): The minimum year in the range for normalization.
    #    end_year (int): The maximum year in the range for normalization.
    #    colormap_name (str): The name of the Matplotlib colormap to use (e.g., 'viridis', 'plasma', 'cividis').

    #Returns:
    #    list: A list of (R, G, B) tuples, where each tuple represents a color
    #          corresponding to a year in the input list.
    
    
    # Normalize the years to a 0-1 range
    normalized_years = (np.array(years) - start_year) / (end_year - start_year)

    # Get the colormap
    cmap = cm.get_cmap(colormap_name)

    # Get colors from the colormap based on normalized years
    colors_rgba = cmap(normalized_years)

    # Convert RGBA to RGB (dropping the alpha channel if not needed)
    colors_rgb = [tuple(c[:3]) for c in colors_rgba]

    return colors_rgb

# Example usage:
years_data = [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025]
min_year = 1990
max_year = 2025

# Get colors using the 'plasma' colormap
gradient_colors = get_color_gradient_by_year(years_data, min_year, max_year, colormap_name='plasma')

# Print the generated colors
print("Generated Colors (RGB):")
for i, color in enumerate(gradient_colors):
    print(f"Year {years_data[i]}: {color}")

# Optional: Visualize the gradient (e.g., using a simple plot)
plt.figure(figsize=(8, 2))
for i, color in enumerate(gradient_colors):
    plt.axvline(x=years_data[i], color=color, linewidth=5)
plt.title("Color Gradient Based on Year")
plt.xlabel("Year")
plt.yticks([]) # Hide y-axis ticks
plt.show()
"""