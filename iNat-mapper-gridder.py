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

# Make the figure
fig = plt.figure()
ax = fig.add_subplot(111)

"""
def draw_screen_poly( lats, lons, m):
    x, y = m( lons, lats )
    xy = zip(x,y)
    poly = Polygon( list(xy), facecolor='red', alpha=0.4 )
    plt.gca().add_patch(poly)

lats = [ -30, 30, 30, -30 ]
lons = [ -50, -50, 50, 50 ]

m = Basemap(projection='sinu',lon_0=0)
m.drawcoastlines()
m.drawmapboundary()
draw_screen_poly( lats, lons, m )

plt.show()"""
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


allbees = pd.read_csv("affinis-16-nov-2024.csv", sep=',', on_bad_lines = "skip", index_col=False, dtype='unicode')

#convert date to datetime
allbees['observed_on'] = pd.to_datetime(allbees['observed_on'])

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
all_2021 = allbees[allbees['observed_on'].dt.year == 2021]
all_2022 = allbees[allbees['observed_on'].dt.year == 2022]
all_2023 = allbees[allbees['observed_on'].dt.year == 2023]
all_2024 = allbees[allbees['observed_on'].dt.year == 2024]
all_recent = allbees[allbees['observed_on'].dt.year > 2019]

grids_2020 = all_2020['gridcell'].unique()

grids_2021 = all_2021['gridcell'].unique()

grids_2022 = all_2022['gridcell'].unique()

grids_2023 = all_2023['gridcell'].unique()

grids_2024 = all_2024['gridcell'].unique()

grids_recent = all_recent['gridcell'].unique()




#map = Basemap(llcrnrlon=-97, llcrnrlat=34, urcrnrlon=-77, urcrnrlat=50, projection='cyl', resolution = 'h')
#map = Basemap(lat_1=35.,lat_2=45, llcrnrlon=-97, llcrnrlat=34, urcrnrlon=-77, urcrnrlat=50, projection='aea', resolution = 'h')
map = Basemap(width=1600000,height=1450000,resolution='h',projection='aea',lat_1=37.,lat_2=43,lon_0=-87,lat_0=43)

#for southeast MN corner: lat_1=40., lat_2=45., lon_0=-91, lat_0=44



map.drawstates()
map.drawcountries()

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='white',lake_color='aqua')
#map.drawcoastlines()



#x1,y1 = map(41.0,-81.6)
#x2,y2 = map(41.0,-81.1001)
#x3,y3 = map(41.9,-81.1001)
#x4,y4 = map(41.9,81.6)

#poly = Polygon([(x1,y1),(x2,y2),(x3,y3),(x4,y4)],facecolor='red')
#plt.gca().add_patch(poly)

patches = []

#seems to work....up left, bot left, bot right, top right
#test = np.array([[-92,47.6],[-92,43.8],[-87,43.6],[-87,47.6]])
#patches.append(Polygon(test))

#43.0,-89.6
#grid = np.array([[-89.6,43.0],[-89.6,43.1999],[-89.4001,43.1999],[-89.4001,43.0]])
#grid = make_map_polygon(-89.6,43.0)
#patches.append(Polygon(grid))

#ax.add_collection(PatchCollection(patches, facecolor='blue', edgecolor='k', linewidths=1.5, alpha = 0.5))
#ax.add_collection(PatchCollection(patches, facecolor='blue', alpha = 0.5))


#for location in grids_2023:
for location in grids_recent:
    lat = float(location.split(",")[0])
    lon = float(location.split(",")[1])
    print (lat, lon)
    grid = make_map_polygon(lon, lat)
    
    grid = map.projtran(grid) #This is the secret to making it work, bla
    patches.append(Polygon(grid))    

ax.add_collection(PatchCollection(patches, facecolor='red', alpha = 0.5))



plt.show()


