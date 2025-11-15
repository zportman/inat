# https://stackoverflow.com/questions/12251189/how-to-draw-rectangles-on-a-basemap
#https://gist.github.com/blaylockbk/79658bdde8c1334ab88d3a67c6e57477 


from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import pandas as pd
import csv
import math

pd.set_option('display.max_columns', None)  


# Make the figure
#fig = plt.figure()
#ax = fig.add_subplot(111)

midwestern_pocket_states = ["Minnesota", "Iowa", "Wisconsin", "Illinois"]


def round_down_to_even_first_decimal(num):
    """take a number, round it down to the even first decimal point"""
    num = float(num)
    num = num * 10 #multiply by 10 to get to first deciumal
    num = num / 2 #dividew by 2 to get the even round up
    num = math.floor(num) #round
    num = num * 2 #multiply by 2 to get back to the non-evens
    num = num / 10 #divide by 10 to get back to 1 decimal
    return num

def make_map_polygon(lat, lon):
    #Given a lat and long, returns the array of 4 points that make up that gridcell polygon
    # since you rounded down to make the lat lon originally, we add  here :3
    
    point1 = [lat, lon]
    point2 = [lat, lon+0.1999]
    point3 = [lat+0.1999, lon + 0.1999]
    point4 = [lat+0.1999, lon]
    
    return np.array([point1, point2, point3, point4])


#allbees = pd.read_csv("affinis-16-nov-2024.csv", sep=',', on_bad_lines = "skip", index_col=False, dtype='unicode')

#allbees = pd.read_csv("affinis-26-mar-2025.csv", sep=',', on_bad_lines = "skip", index_col=False, dtype='unicode')

#allbees = pd.read_csv("affinis-26-mar-2025.csv", sep=',', on_bad_lines = "skip", index_col=False, dtype='unicode')

#changed to get all bumbles, not just affinis - using data downloadednfrom inat
###allbees = pd.read_csv("all-bumble-pocket-observations-566842.csv/observations-566842.csv", sep=',', on_bad_lines = "skip", index_col=False, dtype='unicode')

#just affinis again...
#allbees = pd.read_csv("observations-598205.csv/observations-598205.csv", sep=',', on_bad_lines = "skip", index_col=False, dtype='unicode')
allbees = pd.read_csv("observations-614815.csv/observations-614815.csv", sep=',', on_bad_lines = "skip", index_col=False, dtype='unicode')



#first filter by the species you want
allbees = allbees[allbees['scientific_name'] =="Bombus affinis"]


#convert date to datetime
allbees['observed_on'] = pd.to_datetime(allbees['observed_on'])
allbees['year'] = pd.to_datetime(allbees['observed_on']).dt.year

allbees = allbees[allbees['geoprivacy'] !="private"] #remove all private locations

print(allbees.head())
print (len(allbees))

#round the lats
allbees['latitude']  = allbees['latitude'].apply(round_down_to_even_first_decimal)

#round the longs
allbees['longitude']  = allbees['longitude'].apply(round_down_to_even_first_decimal)


#add the gricell column
allbees['gridcell'] = allbees['latitude'].astype(str) + "," + allbees['longitude'].astype(str)
print(allbees.head())

#MN_bees = allbees[allbees.place_state_name =="Minnesota"]

#get counts per year:
all_2020 = allbees[allbees['observed_on'].dt.year == 2020]
all_2020_midwest = all_2020[all_2020['place_state_name'].isin(midwestern_pocket_states)] 

all_2021 = allbees[allbees['observed_on'].dt.year == 2021]
all_2021_midwest = all_2021[all_2021['place_state_name'].isin(midwestern_pocket_states)] 


all_2022 = allbees[allbees['observed_on'].dt.year == 2022]
all_2022_midwest = all_2022[all_2022['place_state_name'].isin(midwestern_pocket_states)] 


all_2023 = allbees[allbees['observed_on'].dt.year == 2023]
all_2023_midwest = all_2023[all_2023['place_state_name'].isin(midwestern_pocket_states)] 


all_2024 = allbees[allbees['observed_on'].dt.year == 2024]
all_2024_midwest = all_2024[all_2024['place_state_name'].isin(midwestern_pocket_states)] 

all_2025 = allbees[allbees['observed_on'].dt.year == 2025]
all_2025_midwest = all_2025[all_2025['place_state_name'].isin(midwestern_pocket_states)] 

all_recent = allbees[allbees['observed_on'].dt.year > 2019]
all_recent_midwest = all_recent[all_recent['place_state_name'].isin(midwestern_pocket_states)] 


grids_2020 = all_2020['gridcell'].unique()
count_midwest_grids_2020 = len(all_2020_midwest['gridcell'].unique())

grids_2021 = all_2021['gridcell'].unique()
count_midwest_grids_2021 = len(all_2021_midwest['gridcell'].unique())

grids_2022 = all_2022['gridcell'].unique()
count_midwest_grids_2022 = len(all_2022_midwest['gridcell'].unique())

grids_2023 = all_2023['gridcell'].unique()
count_midwest_grids_2023 = len(all_2023_midwest['gridcell'].unique())

grids_2024 = all_2024['gridcell'].unique()
count_midwest_grids_2024 = len(all_2024_midwest['gridcell'].unique())

grids_2025 = all_2025['gridcell'].unique()
count_midwest_grids_2025 = len(all_2025_midwest['gridcell'].unique())

grids_recent = all_recent['gridcell'].unique()
count_midwest_grids_recent = len(all_recent_midwest['gridcell'].unique())



fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(6, 10))
fig.tight_layout(pad=-0.1) 
fig.subplots_adjust(wspace = 0.05, top = 0.98)
#fig.tight_layout() 


#map = Basemap(llcrnrlon=-97, llcrnrlat=34, urcrnrlon=-77, urcrnrlat=50, projection='cyl', resolution = 'h')
#map = Basemap(lat_1=35.,lat_2=45, llcrnrlon=-97, llcrnrlat=34, urcrnrlon=-77, urcrnrlat=50, projection='aea', resolution = 'h')
###map = Basemap(width=1600000,height=1450000,resolution='h',projection='aea',lat_1=37.,lat_2=43,lon_0=-87,lat_0=43)


#change resolution to c for faster
###map = Basemap(width=1600000,height=1450000,resolution='c',projection='aea',lat_1=37.,lat_2=43,lon_0=-87,lat_0=43, ax=ax[0,0]) #whole affinis area
map = Basemap(width=1200000,height=1000000,resolution='h',projection='aea',lat_1=40., lat_2=45., lon_0=-90.5, lat_0=44, ax=ax[0,0]) #whole affinis area

#for southeast MN corner: lat_1=40., lat_2=45., lon_0=-91, lat_0=44
#nw corner of IL: lat_1=40., lat_2=45., lon_0=-90, lat_0=42.5


map.drawstates()
map.drawcountries()

map.drawmapboundary(fill_color='lightblue')
map.fillcontinents(color='white',lake_color='lightblue')
#map.drawcoastlines()

map2 = Basemap(width=1200000,height=1000000,resolution='h',projection='aea',lat_1=40., lat_2=45., lon_0=-90.5, lat_0=44, ax=ax[0,1])
map2.drawstates()
map2.drawcountries()

map2.drawmapboundary(fill_color='lightblue')
map2.fillcontinents(color='white',lake_color='lightblue')

map3 = Basemap(width=1200000,height=1000000,resolution='h',projection='aea',lat_1=40., lat_2=45., lon_0=-90.5, lat_0=44, ax=ax[1,0])
map3.drawstates()
map3.drawcountries()

map3.drawmapboundary(fill_color='lightblue')
map3.fillcontinents(color='white',lake_color='lightblue')

map4 = Basemap(width=1200000,height=1000000,resolution='h',projection='aea',lat_1=40., lat_2=45., lon_0=-90.5, lat_0=44, ax=ax[1,1])
map4.drawstates()
map4.drawcountries()

map4.drawmapboundary(fill_color='lightblue')
map4.fillcontinents(color='white',lake_color='lightblue')

map5 = Basemap(width=1200000,height=1000000,resolution='h',projection='aea',lat_1=40., lat_2=45., lon_0=-90.5, lat_0=44, ax=ax[2,0])
map5.drawstates()
map5.drawcountries()

map5.drawmapboundary(fill_color='lightblue')
map5.fillcontinents(color='white',lake_color='lightblue')

map6 = Basemap(width=1200000,height=1000000,resolution='h',projection='aea',lat_1=40., lat_2=45., lon_0=-90.5, lat_0=44, ax=ax[2,1])
map6.drawstates()
map6.drawcountries()

map6.drawmapboundary(fill_color='lightblue')
map6.fillcontinents(color='white',lake_color='lightblue')


#seems to work....up left, bot left, bot right, top right
#test = np.array([[-92,47.6],[-92,43.8],[-87,43.6],[-87,47.6]])
#patches.append(Polygon(test))

#43.0,-89.6
#grid = np.array([[-89.6,43.0],[-89.6,43.1999],[-89.4001,43.1999],[-89.4001,43.0]])
#grid = make_map_polygon(-89.6,43.0)
#patches.append(Polygon(grid))

#ax.add_collection(PatchCollection(patches, facecolor='blue', edgecolor='k', linewidths=1.5, alpha = 0.5))
#ax.add_collection(PatchCollection(patches, facecolor='blue', alpha = 0.5))


#make dataframe for the combined figure
###all_years = pd.DataFrame(columns = ['latlon', 2020, 2021, 2022, 2023, 2024, 2025])

patches = []

#for location in grids_2023:
for location in grids_2020:
    lat = float(location.split(",")[0])
    lon = float(location.split(",")[1])
    print (lat, lon)
    grid = make_map_polygon(lon, lat)
    
    grid = map.projtran(grid) #This is the secret to making it work, bla
    patches.append(Polygon(grid))    

ax[0,0].add_collection(PatchCollection(patches, facecolor='red', alpha = 0.7))

ax[0,0].set_title("2020 (" + str(count_midwest_grids_2020) + ")", y=0.88, backgroundcolor = 'silver') 

patches2 = []

for location in grids_2021:
    lat = float(location.split(",")[0])
    lon = float(location.split(",")[1])
    print (lat, lon)
    grid = make_map_polygon(lon, lat)
    
    grid = map.projtran(grid) #This is the secret to making it work, bla
    patches2.append(Polygon(grid))    

ax[0,1].add_collection(PatchCollection(patches2, facecolor='red', alpha = 0.7))
ax[0,1].set_title("2021 (" + str(count_midwest_grids_2021) + ")", y=0.88, backgroundcolor = 'silver') 


patches3 = []

for location in grids_2022:
    lat = float(location.split(",")[0])
    lon = float(location.split(",")[1])
    print (lat, lon)
    grid = make_map_polygon(lon, lat)
    
    grid = map.projtran(grid) #This is the secret to making it work, bla
    patches3.append(Polygon(grid))    

ax[1,0].add_collection(PatchCollection(patches3, facecolor='red', alpha = 0.7))
ax[1,0].set_title("2022 (" + str(count_midwest_grids_2022) + ")", y=0.88, backgroundcolor = 'silver') 


patches4 = []

for location in grids_2023:
    lat = float(location.split(",")[0])
    lon = float(location.split(",")[1])
    print (lat, lon)
    grid = make_map_polygon(lon, lat)
    
    grid = map.projtran(grid) #This is the secret to making it work, bla
    patches4.append(Polygon(grid))    

ax[1,1].add_collection(PatchCollection(patches4, facecolor='red', alpha = 0.7))
ax[1,1].set_title("2023 (" + str(count_midwest_grids_2023) + ")", y=0.88, backgroundcolor = 'silver') 

patches5 = []

for location in grids_2024:
    lat = float(location.split(",")[0])
    lon = float(location.split(",")[1])
    print (lat, lon)
    grid = make_map_polygon(lon, lat)
    
    grid = map.projtran(grid) #This is the secret to making it work, bla
    patches5.append(Polygon(grid))    

ax[2,0].add_collection(PatchCollection(patches5, facecolor='red', alpha = 0.7))
ax[2,0].set_title("2024 (" + str(count_midwest_grids_2024) + ")", y=0.88, backgroundcolor = 'silver') 


"""
patches6 = []


for location in grids_recent:
    lat = float(location.split(",")[0])
    lon = float(location.split(",")[1])
    print (lat, lon)
    grid = make_map_polygon(lon, lat)
    
    grid = map.projtran(grid) #This is the secret to making it work, bla
    patches6.append(Polygon(grid))    

ax[2,1].add_collection(PatchCollection(patches6, facecolor='red', alpha = 0.7))
ax[2,1].set_title("2020–2024 (" + str(count_midwest_grids_recent) + ")", y=0.88, backgroundcolor = 'silver') 
"""

patches6 = []

for location in grids_2025:
    lat = float(location.split(",")[0])
    lon = float(location.split(",")[1])
    print (lat, lon)
    grid = make_map_polygon(lon, lat)
    
    grid = map.projtran(grid) #This is the secret to making it work, bla
    patches6.append(Polygon(grid))    

ax[2,1].add_collection(PatchCollection(patches6, facecolor='red', alpha = 0.7))
ax[2,1].set_title("2025 (" + str(count_midwest_grids_2025) + ")", y=0.88, backgroundcolor = 'silver') 




fig.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

#plt.figure(dpi=1200)

plt.savefig("my_plot.png", dpi=600)

plt.show()


#a few possibilities for this.../
# thinking make a pandas array, with the lat long grid by each year
#for each one, if lat long year combo not in, add it
# then in the end for each gridcell can calculate how many  years and thus color

#actually maybe try different
#take the recent, subset it down to just lat, lon, and year, and then only do unique rows
# then just add to map normally using a 0.2 color

fig, ax = plt.subplots(figsize=(10, 10))

#map = Basemap(width=1200000,height=1000000,resolution='h',projection='aea',lat_1=40., lat_2=45., lon_0=-90.5, lat_0=44, ax=ax) #whole affinis area
map = Basemap(width=1400000,height=1200000,resolution='h',projection='aea',lat_1=40., lat_2=45., lon_0=-90.5, lat_0=44, ax=ax) #whole affinis area

#for southeast MN corner: lat_1=40., lat_2=45., lon_0=-91, lat_0=44
#nw corner of IL: lat_1=40., lat_2=45., lon_0=-90, lat_0=42.5

map.drawstates()
map.drawcountries()

map.drawmapboundary(fill_color='lightblue')
map.fillcontinents(color='white',lake_color='lightblue')
patches = []


columns_to_keep = ['latitude', 'longitude', 'year']
all_recent = all_recent[columns_to_keep]
all_recent = all_recent.drop_duplicates()

#make into list of lists to iterate
all_recent = all_recent.values.tolist()

for row in all_recent:
    lat = float(row[0])
    lon = float(row[1])
    #lat = float(location.split(",")[0])
    #lon = float(location.split(",")[1])
    print (lat, lon)
    grid = make_map_polygon(lon, lat)
    
    grid = map.projtran(grid) #This is the secret to making it work, bla
    patches.append(Polygon(grid))    

ax.add_collection(PatchCollection(patches, facecolor='red', alpha = 0.35))
ax.set_title("2020–2025 (" + str(count_midwest_grids_recent) + ")", fontsize=20, y=0.94, backgroundcolor = 'silver') 
plt.savefig("all-combined-alpha3.png", dpi=600)

plt.show()
