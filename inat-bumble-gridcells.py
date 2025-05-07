"""Goals:
1. Count up gridcells of affinis (and I guess other species to compare and graph that by year
2. Also get number unique observors and average number of observations per person
3. Maybe rewrite the bumble cumulative using the cycle-through-each-observation method

fuuuuck I dunno i fyou can do a cycle method with this BS JSON crap
might be easier to just calcuate every possib gridcell and loop through those and count the number of observation in each gridcell per year. 
so every state, gridcell, year combo, blarf
oh -- or can just simplify by specifying fields :)
"""

#from pyinaturalist import *
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import numpy as np
import csv 
import math
pd.set_option('display.max_columns', None)  

#remove top and right borders for all plots
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False


def get_observers_state_year(data, state, year):
    """Given a state and a year, returns the array for all the counts of observers"""
    state_bees = data[data.place_state_name ==state] #filter by state
    state_bees_year = state_bees[state_bees['observed_on'].dt.year == year] #filter by year   
    observers = state_bees_year['user_login'].value_counts() #get value counts of observers
    
    #print some stats
    print ("obs stats:", state, year, len(observers), sum(observers)/len(observers))
    
    #return just the array of counts
    return observers.values

#allbees = pd.read_csv("affinis-16-nov-2024.csv", sep=',', on_bad_lines = "skip", index_col=False, dtype='unicode')
allbees = pd.read_csv("affinis-26-mar-2025.csv", sep=',', on_bad_lines = "skip", index_col=False, dtype='unicode')


#convert date to datetime
allbees['observed_on'] = pd.to_datetime(allbees['observed_on'])

allbees = allbees[allbees['geoprivacy'] !="private"] #remove all private locations

print(allbees.head())
print (len(allbees))



#first doing all observors
#MN_bees = allbees[allbees.place_state_name =="Minnesota"]
allbees_2024 = allbees[allbees['observed_on'].dt.year == 2024]

#get counts of observers:
observers = allbees_2024['user_login'].value_counts()

print ("number of 2024 obs:", len(observers))
print ("just array", observers.values)

all_2020 = allbees[allbees['observed_on'].dt.year == 2020]
all_2020 = all_2020['user_login'].value_counts()
all_2021 = allbees[allbees['observed_on'].dt.year == 2021]
all_2021 = all_2021['user_login'].value_counts()
all_2022 = allbees[allbees['observed_on'].dt.year == 2022]
all_2022 = all_2022['user_login'].value_counts()

all_2023 = allbees[allbees['observed_on'].dt.year == 2023]
all_2023 = all_2023['user_login'].value_counts()

all_2024 = allbees[allbees['observed_on'].dt.year == 2024]
all_2024 = all_2024['user_login'].value_counts()
                   

fig = plt.figure(figsize =(10, 7))
plt.boxplot([all_2020, all_2021, all_2022, all_2023, all_2024])
plt.show()


fig1, ax1 = plt.subplots(nrows=2, ncols=2, figsize=(9, 6))
fig1.tight_layout(pad=2) 


#first Minnesota
MN_2020 = get_observers_state_year(allbees, "Minnesota", 2020)
MN_2021 = get_observers_state_year(allbees, "Minnesota", 2021)
MN_2022 = get_observers_state_year(allbees, "Minnesota", 2022)
MN_2023 = get_observers_state_year(allbees, "Minnesota", 2023)
MN_2024 = get_observers_state_year(allbees, "Minnesota", 2024)

ax1[0,0].set_title('Minnesota', y=0.95)
ax1[0,0].boxplot([MN_2020, MN_2021, MN_2022, MN_2023, MN_2024]) 
ax1[0,0].set_xticks([1,2,3,4,5], ['2020', '2021', '2022', '2023', '2024'])

#second Wisconsin
WI_2020 = get_observers_state_year(allbees, "Wisconsin", 2020)
WI_2021 = get_observers_state_year(allbees, "Wisconsin", 2021)
WI_2022 = get_observers_state_year(allbees, "Wisconsin", 2022)
WI_2023 = get_observers_state_year(allbees, "Wisconsin", 2023)
WI_2024 = get_observers_state_year(allbees, "Wisconsin", 2024)

ax1[0,1].set_title('Wisconsin', y=0.95)
ax1[0,1].boxplot([WI_2020, WI_2021, WI_2022, WI_2023, WI_2024]) 
ax1[0,1].set_xticks([1,2,3,4,5], ['2020', '2021', '2022', '2023', '2024'])

#third Iowa
IA_2020 = get_observers_state_year(allbees, "Iowa", 2020)
IA_2021 = get_observers_state_year(allbees, "Iowa", 2021)
IA_2022 = get_observers_state_year(allbees, "Iowa", 2022)
IA_2023 = get_observers_state_year(allbees, "Iowa", 2023)
IA_2024 = get_observers_state_year(allbees, "Iowa", 2024)

ax1[1,0].set_title('Iowa', y=0.95)
ax1[1,0].boxplot([IA_2020, IA_2021, IA_2022, IA_2023, IA_2024]) 
ax1[1,0].set_xticks([1,2,3,4,5], ['2020', '2021', '2022', '2023', '2024'])

#fourth Illinois
IL_2020 = get_observers_state_year(allbees, "Illinois", 2020)
IL_2021 = get_observers_state_year(allbees, "Illinois", 2021)
IL_2022 = get_observers_state_year(allbees, "Illinois", 2022)
IL_2023 = get_observers_state_year(allbees, "Illinois", 2023)
IL_2024 = get_observers_state_year(allbees, "Illinois", 2024)

ax1[1,1].set_title('Illinois', y=0.95)
ax1[1,1].boxplot([IL_2020, IL_2021, IL_2022, IL_2023, IL_2024]) 
ax1[1,1].set_xticks([1,2,3,4,5], ['2020', '2021', '2022', '2023', '2024'])

plt.show()

print ("done!")



"""huh, for the gridcells, just make a new column and populate that 
with a string that combines the lat and long rounded down/up to the nearest even first decimal
round lat down
round long up
I think? I dunno what inat does naturally, this garbo site has zero documentation
Or just round both down?I think that is the way to go from what I can tell

So 43.07735499	-89.5520751
would be "43.0,-89.6"

"""

def round_down_to_even_first_decimal(num):
    """take a number, round it down to the even first decimal point"""
    num = float(num)
    num = num * 10 #multiply by 10 to get to first deciumal
    num = num / 2 #dividew by 2 to get the even round up
    num = math.floor(num) #round
    num = num * 2 #multiply by 2 to get back to the non-evens
    num = num / 10 #divide by 10 to get back to 1 decimal
    return num


def get_gridcells_year(data, year):
    """Given a  year, returns the count for each gridcells accross range for that year"""
    data = data[data['observed_on'].dt.year == year]
    data = data['gridcell'].value_counts()

    #return just the counts
    return data


def get_gridcells_state_year(data, state, year):
    """Given a state and year, returns the count for each gridcells accross range for that state in that year"""
    state_bees = data[data.place_state_name ==state] #filter by state    
    state_bees = state_bees[state_bees['observed_on'].dt.year == year]
    gridcells = state_bees['gridcell'].value_counts()

    #return just the counts
    return gridcells

#round the lats
allbees['latitude']  = allbees['latitude'].apply(round_down_to_even_first_decimal)

#round the longs
allbees['longitude']  = allbees['longitude'].apply(round_down_to_even_first_decimal)


#add the gricell column
allbees['gridcell'] = allbees['latitude'].astype(str) + "," + allbees['longitude'].astype(str)
print(allbees.head())


#now plot all gridcells by year, right nwo includes the entire range
#but first lets get rid of all years less than 2020
allbees = allbees[allbees['observed_on'].dt.year > 2019]

all_grids = allbees['gridcell'].value_counts()
print ("Number of grids all time (since 2020):", len(all_grids))
print (all_grids.head())

bees_2020 = allbees[allbees['observed_on'].dt.year == 2020]
bees_2020 = bees_2020['gridcell'].value_counts()

print (bees_2020.head())



all_grids_2020 = get_gridcells_year(allbees, 2020)
print ("Number of grids 2020:", len(all_grids_2020))

all_grids_2021 = get_gridcells_year(allbees, 2021)
print ("Number of grids 2021:", len(all_grids_2021))

all_grids_2022 = get_gridcells_year(allbees, 2022)
print ("Number of grids 2022:", len(all_grids_2022))

all_grids_2023 = get_gridcells_year(allbees, 2023)
print ("Number of grids 2023:", len(all_grids_2023))

all_grids_2024 = get_gridcells_year(allbees, 2024)
print ("Number of grids 2024:", len(all_grids_2024))

#hm, so you can graph both bar chards of total gridcells, as well as boxplots of obs for each gridcell
fig = plt.figure(figsize =(10, 7))
plt.title('obs per gridcell per year')
plt.boxplot([all_grids_2020, all_grids_2021, all_grids_2022, all_grids_2023, all_grids_2024])
plt.show()


fig = plt.figure(figsize =(10, 7))
plt.title('total occupied gridcells per year')
plt.bar([2020, 2021, 2022, 2023, 2024], [len(all_grids_2020), len(all_grids_2021), len(all_grids_2022), len(all_grids_2023), len(all_grids_2024)])
plt.show()


#UGH NOW DO BREAKDOWN BY STATE

fig1, ax1 = plt.subplots(nrows=2, ncols=2, figsize=(9, 6))
fig1.tight_layout(pad=2) 


#first Minnesota
MN_grids_2020 = len(get_gridcells_state_year(allbees, "Minnesota", 2020))
MN_grids_2021 = len(get_gridcells_state_year(allbees, "Minnesota", 2021))
MN_grids_2022 = len(get_gridcells_state_year(allbees, "Minnesota", 2022))
MN_grids_2023 = len(get_gridcells_state_year(allbees, "Minnesota", 2023))
MN_grids_2024 = len(get_gridcells_state_year(allbees, "Minnesota", 2024))

ax1[0,0].set_title('Minnesota', y=0.95)
ax1[0,0].bar([2020, 2021, 2022, 2023, 2024], [MN_grids_2020, MN_grids_2021, MN_grids_2022, MN_grids_2023, MN_grids_2024])
ax1[0,0].bar_label(ax1[0,0].containers[0])


#second Wisconsin
WI_grids_2020 = len(get_gridcells_state_year(allbees, "Wisconsin", 2020))
WI_grids_2021 = len(get_gridcells_state_year(allbees, "Wisconsin", 2021))
WI_grids_2022 = len(get_gridcells_state_year(allbees, "Wisconsin", 2022))
WI_grids_2023 = len(get_gridcells_state_year(allbees, "Wisconsin", 2023))
WI_grids_2024 = len(get_gridcells_state_year(allbees, "Wisconsin", 2024))

ax1[0,1].set_title('Wisconsin', y=0.95)
ax1[0,1].bar([2020, 2021, 2022, 2023, 2024], [WI_grids_2020, WI_grids_2021, WI_grids_2022, WI_grids_2023, WI_grids_2024])
ax1[0,1].bar_label(ax1[0,1].containers[0])


#third Iowa
IA_grids_2020 = len(get_gridcells_state_year(allbees, "Iowa", 2020))
IA_grids_2021 = len(get_gridcells_state_year(allbees, "Iowa", 2021))
IA_grids_2022 = len(get_gridcells_state_year(allbees, "Iowa", 2022))
IA_grids_2023 = len(get_gridcells_state_year(allbees, "Iowa", 2023))
IA_grids_2024 = len(get_gridcells_state_year(allbees, "Iowa", 2024))

ax1[1,0].set_title('Iowa', y=0.95)
ax1[1,0].bar([2020, 2021, 2022, 2023, 2024], [IA_grids_2020, IA_grids_2021, IA_grids_2022, IA_grids_2023, IA_grids_2024])
ax1[1,0].bar_label(ax1[1,0].containers[0])


#fourth Illinois
IL_grids_2020 = len(get_gridcells_state_year(allbees, "Illinois", 2020))
IL_grids_2021 = len(get_gridcells_state_year(allbees, "Illinois", 2021))
IL_grids_2022 = len(get_gridcells_state_year(allbees, "Illinois", 2022))
IL_grids_2023 = len(get_gridcells_state_year(allbees, "Illinois", 2023))
IL_grids_2024 = len(get_gridcells_state_year(allbees, "Illinois", 2024))

ax1[1,1].set_title('Illinois', y=0.95)
ax1[1,1].bar([2020, 2021, 2022, 2023, 2024], [IL_grids_2020, IL_grids_2021, IL_grids_2022, IL_grids_2023, IL_grids_2024])
ax1[1,1].bar_label(ax1[1,1].containers[0])

plt.show()
