from pyinaturalist import *
from pyinaturalist_convert import to_dataframe
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)


geoData = gpd.read_file('US-counties.geojson') #moving this earlier out of the loop
# Make sure the "id" column is an integer
geoData.id = geoData['id'].astype(int)

# filter to MN.
statesToKeep = ['27']
geoData = geoData[geoData.STATE.isin(statesToKeep)]
#what does geodata look like?
print (geoData)

species_list = {'52775': "Bombus", '121519': "B. affinis", '198857': "B. ashtoni", '198856': "B. auricomus", '52779': "B. bimaculatus", 
                '143854': "B. borealis", '198859': "B. citrinus", '271451': "B. crotchii", '52774': "B. fervidus", '541839': "B. flavidus", 
                '308937': "B. fraternus", '120215': "B. griseocollis", '118970': "B. impatiens",
                '143036': "B. insularis", '82371': "B. occidentalis", '155085': "B. perplexus",
                '56887': "B. pensylvanicus", '144011': "B. rufocinctus", '127905': "B. ternarius", '121517': "B. terricola", '128670': "B. vagans", '51110': "Xylocopa virginica",
                '127812': "All Hylaeus", '567666': "Melissodes bimaculatus"}

species = '144011' #rufocinctus
species = '198856' #auricomus
species = '120215' #griseocollis
species = '118970' #impatiens
species = '121519' #affinis
species = '143854' #borealis
species = '52779' #bimaculatus
species = '56887' #pensylvanicus


place = '38' #minnesota

zach = '318825'


#first just map all observations, then split between ID by me and not ID by me



observations = get_observations(quality_grade = "research", verifiable = True,  place_id = place, taxon_id=species, page='all')
print ('got data')


zp_confirmed = get_observations(quality_grade = "research", verifiable = True,  place_id = place, taxon_id=species, page='all', ident_user_id = zach)


# Convert results to a clean DataFrame
df = to_dataframe(observations)
zp_df = to_dataframe(zp_confirmed)

#extract identifier and species from it...

#first flatten the identifier ditionary to string

df['identifications_str'] = df['identifications'].astype(str)
zp_df['identifications_str'] = zp_df['identifications'].astype(str)


print(df.head())
print(len(df))

print(zp_df.head())
print(len(zp_df))

print(df.identifications.value_counts())




# Extract Latitude (index 0) and Longitude (index 1) into separate columns
df['Latitude'] = df['location'].apply(lambda x: x[0])
df['Longitude'] = df['location'].apply(lambda x: x[1])

zp_df['Latitude'] = zp_df['location'].apply(lambda x: x[0])
zp_df['Longitude'] = zp_df['location'].apply(lambda x: x[1])


gdf_points = gpd.GeoDataFrame(
    df, 
    geometry=gpd.points_from_xy(df.Longitude, df.Latitude),
    crs="EPSG:4326"
)

zp_gdf_points = gpd.GeoDataFrame(
    zp_df, 
    geometry=gpd.points_from_xy(zp_df.Longitude, zp_df.Latitude),
    crs="EPSG:4326"
)



fig, ax = plt.subplots(figsize=(10, 10))

# Layer 1: Plot the background county polygon shapes from the JSON
geoData.plot(
    ax=ax, 
    color='whitesmoke', 
    edgecolor='gray', 
    linewidth=0.5, 
    label='County Borders'
)

# Layer 2: Overlay your data points on top of the map
gdf_points.plot(
    ax=ax, 
    color='red', 
    markersize=20, 
    edgecolor='black', 
    zorder=3, 
    label='My Points'
)

zp_gdf_points.plot(
    ax=ax, 
    color='blue', 
    markersize=20, 
    edgecolor='black', 
    zorder=4, 
    label='My Points'
)

# 6. Zoom the map viewport directly around your data cluster boundaries
# This stops it from looking like a tiny speck if your JSON covers the whole US
plt.xlim([-97.5, -89.0])
plt.ylim([43.0, 49.5])

plt.title(species_list[species], fontsize=18)
plt.legend()
plt.show()