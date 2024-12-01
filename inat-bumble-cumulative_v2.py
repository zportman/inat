from pyinaturalist import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import pandas as pd


#TODO: get number of unique observors per state per year, and graph the average number of observations per using box plots?
#TODO: count up number of unique location squares :/
#need to match those up with iNat obscured coordinate boxes somehow...

#remove top and right borders for all plots
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False

"""A script to get species data from iNatutralist to make cumulative graphs for ***bee monitoring*** """

# Created by Zach Portman, 9 Jul 2024

"""something to think about -- you could actually get the number of unique observors manually by getting ALL obsevations and then making your own array/histogram 
while keeping a list of observors and excluding those...
Note that you use the histogram function cuz it's ezpz, but you could do this all manually using the get_observations function if needed. blarf."""

project = 185321 #all bees

#states with affinis:
#38 Minnesota
#24 Iowa
#32 Wisconsin
#35 Illinois
#33 West Virginia
#7 Virginia
def affinis_state_breakdown(species):
#species should be the iNat number
    

 
    fig1, ax1 = plt.subplots(nrows=2, ncols=2, figsize=(9, 6))
    fig1.tight_layout(pad=2) 
    
    
    
    
    
    #some code to make the current year cut off -- though not usig now cuz then too hard to see linnes
    duration = datetime.now() - dt.datetime(2024, 3, 1)
    duration = duration.days + 1 #adding 1 to prevent off by 1 apparently...
    #print ("duration", z.index[:duration])    
    
    
    #First Minnesota
    
    
    Twent_twentytwenty = get_day_histogram(species, dt.datetime(2020, 3, 1), dt.datetime(2020, 10, 31), "38")
    Twent_twentyone = get_day_histogram(species, dt.datetime(2021, 3, 1), dt.datetime(2021, 10, 31), "38")
    Twent_twentytwo = get_day_histogram(species, dt.datetime(2022, 3, 1), dt.datetime(2022, 10, 31), "38")
    Twent_twentythree = get_day_histogram(species, dt.datetime(2023, 3, 1), dt.datetime(2023, 10, 31), "38")
    Twent_twentyfour = get_day_histogram(species, dt.datetime(2024, 3, 1), dt.datetime(2024, 10, 31), "38")   
    
    v = np.cumsum(Twent_twentytwenty) 
    w = np.cumsum(Twent_twentyone) 
    x = np.cumsum(Twent_twentytwo) 
    y = np.cumsum(Twent_twentythree) 
    z = np.cumsum(Twent_twentyfour)     
    
      
    ax1[0,0].set_title('Minnesota', y=0.95)
    
    
    ax1[0,0].plot(z.index, z.values, label = '2024')    
    ax1[0,0].plot(z.index, y.values, label = '2023') 
    ax1[0,0].plot(z.index, x.values, label = '2022')
    ax1[0,0].plot(z.index, w.values, label = '2021')
    ax1[0,0].plot(z.index, v.values, label = '2020')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)    
    ax1[0,0].legend(loc="upper left")    
    ax1[0,0].xaxis.set_major_formatter(mdates.DateFormatter('%#b-%#d'))
    
    
    #second Wisconsin
    Twent_twentytwenty = get_day_histogram(species, dt.datetime(2020, 3, 1), dt.datetime(2020, 10, 31), "32")
    Twent_twentyone = get_day_histogram(species, dt.datetime(2021, 3, 1), dt.datetime(2021, 10, 31), "32")
    Twent_twentytwo = get_day_histogram(species, dt.datetime(2022, 3, 1), dt.datetime(2022, 10, 31), "32")
    Twent_twentythree = get_day_histogram(species, dt.datetime(2023, 3, 1), dt.datetime(2023, 10, 31), "32")
    Twent_twentyfour = get_day_histogram(species, dt.datetime(2024, 3, 1), dt.datetime(2024, 10, 31), "32")   
    
    v = np.cumsum(Twent_twentytwenty) 
    w = np.cumsum(Twent_twentyone) 
    x = np.cumsum(Twent_twentytwo) 
    y = np.cumsum(Twent_twentythree) 
    z = np.cumsum(Twent_twentyfour)     
    
    ax1[0,1].set_title('Wisconsin', y=0.95, pad = 2)
    
    
    ax1[0,1].plot(z.index, z.values, label = '2024')    
    ax1[0,1].plot(z.index, y.values, label = '2023') 
    ax1[0,1].plot(z.index, x.values, label = '2022')
    ax1[0,1].plot(z.index, w.values, label = '2021')
    ax1[0,1].plot(z.index, v.values, label = '2020')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)    
    ax1[0,1].legend(loc="upper left")    
    ax1[0,1].xaxis.set_major_formatter(mdates.DateFormatter('%#b-%#d'))    
    
    
    #third iowa
    Twent_twentytwenty = get_day_histogram(species, dt.datetime(2020, 3, 1), dt.datetime(2020, 10, 31), "24")
    Twent_twentyone = get_day_histogram(species, dt.datetime(2021, 3, 1), dt.datetime(2021, 10, 31), "24")
    Twent_twentytwo = get_day_histogram(species, dt.datetime(2022, 3, 1), dt.datetime(2022, 10, 31), "24")
    Twent_twentythree = get_day_histogram(species, dt.datetime(2023, 3, 1), dt.datetime(2023, 10, 31), "24")
    Twent_twentyfour = get_day_histogram(species, dt.datetime(2024, 3, 1), dt.datetime(2024, 10, 31), "24")   
    
    v = np.cumsum(Twent_twentytwenty) 
    w = np.cumsum(Twent_twentyone) 
    x = np.cumsum(Twent_twentytwo) 
    y = np.cumsum(Twent_twentythree) 
    z = np.cumsum(Twent_twentyfour)     
    
    ax1[1,0].set_title('Iowa', y=0.95, pad = 2)
    
    
    ax1[1,0].plot(z.index, z.values, label = '2024')    
    ax1[1,0].plot(z.index, y.values, label = '2023') 
    ax1[1,0].plot(z.index, x.values, label = '2022')
    ax1[1,0].plot(z.index, w.values, label = '2021')
    ax1[1,0].plot(z.index, v.values, label = '2020')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)    
    ax1[1,0].legend(loc="upper left")    
    ax1[1,0].xaxis.set_major_formatter(mdates.DateFormatter('%#b-%#d'))  
    
    #fourth Illinois
    Twent_twentytwenty = get_day_histogram(species, dt.datetime(2020, 3, 1), dt.datetime(2020, 10, 31), "35")
    Twent_twentyone = get_day_histogram(species, dt.datetime(2021, 3, 1), dt.datetime(2021, 10, 31), "35")
    Twent_twentytwo = get_day_histogram(species, dt.datetime(2022, 3, 1), dt.datetime(2022, 10, 31), "35")
    Twent_twentythree = get_day_histogram(species, dt.datetime(2023, 3, 1), dt.datetime(2023, 10, 31), "35")
    Twent_twentyfour = get_day_histogram(species, dt.datetime(2024, 3, 1), dt.datetime(2024, 10, 31), "35")   
    
    v = np.cumsum(Twent_twentytwenty) 
    w = np.cumsum(Twent_twentyone) 
    x = np.cumsum(Twent_twentytwo) 
    y = np.cumsum(Twent_twentythree) 
    z = np.cumsum(Twent_twentyfour)     
    
    ax1[1,1].set_title('Illinois', y=0.95, pad = 2)
    
    
    ax1[1,1].plot(z.index, z.values, label = '2024')    
    ax1[1,1].plot(z.index, y.values, label = '2023') 
    ax1[1,1].plot(z.index, x.values, label = '2022')
    ax1[1,1].plot(z.index, w.values, label = '2021')
    ax1[1,1].plot(z.index, v.values, label = '2020')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)    
    ax1[1,1].legend(loc="upper left")    
    ax1[1,1].xaxis.set_major_formatter(mdates.DateFormatter('%#b-%#d'))  
    
    plt.show()
    
def get_day_histogram_eastern(species, time1, time2):
    #same as get_day_histogram but only for custom eastern US
    
    #get a histogram of days observed
    #histogram = get_observation_histogram(taxon_id=species, interval = 'day', d1=time1, d2 = time2, quality_grade='research')
    histogram = get_observation_histogram(taxon_id=species, interval = 'day', d1=time1, d2 = time2, quality_grade='research',
                                          nelat='64.18813159901904', nelng='-50', swlat ='22', swlng='-100' )
    #histogram = get_observation_histogram( taxon_id=species, interval = 'day', d1=time1, d2 = time2, quality_grade='research',   place_id=place)
    
    print("histogram:",histogram)

    days = pd.Series(histogram)
    
    #ok I'm going insane because it doesn't report all the dates, they start from first occurrence. Dunno why. Need to fill in the missing zeros...
    #I love stackoverflow: https://stackoverflow.com/questions/19324453/add-missing-dates-to-pandas-dataframe
    
    idx = pd.date_range(time1, time2)
    days.index = pd.DatetimeIndex(days.index)
    days = days.reindex(idx, fill_value=0)
    
    return days
    
def get_day_histogram(species, time1, time2, place="97394"):
    #Time should be in datetime format, but I don't think it need to be, check pyinat docs
    #Default place ID is set to North America.
    
    #get a histogram of days observed
    #histogram = get_observation_histogram(taxon_id=species, interval = 'day', d1=time1, d2 = time2, quality_grade='research')
    #histogram = get_observation_histogram(taxon_id=species, interval = 'day', d1=time1, d2 = time2, quality_grade='research',
    #                                      nelat='64.18813159901904', nelng='-50', swlat ='22', swlng='-100' )
    histogram = get_observation_histogram( taxon_id=species, interval = 'day', d1=time1, d2 = time2, quality_grade='research',   place_id=place)
    
    print("histogram:",histogram)

    days = pd.Series(histogram)
    
    #ok I'm going insane because it doesn't report all the dates, they start from first occurrence. Dunno why. Need to fill in the missing zeros...
    #I love stackoverflow: https://stackoverflow.com/questions/19324453/add-missing-dates-to-pandas-dataframe
    
    idx = pd.date_range(time1, time2)
    days.index = pd.DatetimeIndex(days.index)
    days = days.reindex(idx, fill_value=0)
    
    return days




species = '56887' #pensylvanicus
species = '198857' #ashtoni
species = '143036' #insularis
species = '128670' #vagans
species = '82371' #occidentalis
species = '127905' #ternarius
species = '541839' #flavidus
species = '51110'#Xylocopa virginica
species = '155085' #perplexus
species = '52779' #bimaculatus
species = '143854' #borealis
species = '52774' #fervidus
species = '308937' #fraternus
species = '198856' #auricomus
species = '120215' #griseocollis
species = '121517' #terricola
species = '52775' # ALL BOMBUS
species = '144011' #rufocinctus
species = '118970' #impatiens
species = '271451' #crotchii
species = '198859' #citrinus
species = '121519' #affinis



Twent_twentytwenty = get_day_histogram(species, dt.datetime(2020, 3, 1), dt.datetime(2020, 10, 31))
Twent_twentyone = get_day_histogram(species, dt.datetime(2021, 3, 1), dt.datetime(2021, 10, 31))
Twent_twentytwo = get_day_histogram(species, dt.datetime(2022, 3, 1), dt.datetime(2022, 10, 31))
Twent_twentythree = get_day_histogram(species, dt.datetime(2023, 3, 1), dt.datetime(2023, 10, 31))
Twent_twentyfour = get_day_histogram(species, dt.datetime(2024, 3, 1), dt.datetime(2024, 10, 31))

v = np.cumsum(Twent_twentytwenty) 
w = np.cumsum(Twent_twentyone) 
x = np.cumsum(Twent_twentytwo) 
y = np.cumsum(Twent_twentythree) 
z = np.cumsum(Twent_twentyfour) 




#plotting!!
fig = plt.figure(figsize=[10,6])

ax = fig.add_subplot(111)



print (y)

#here gonna trim z to not go beyond current date
duration = datetime.now() - dt.datetime(2024, 3, 1)
duration = duration.days + 1 #adding 1 to prevent off by 1 apparently...
print ("duration", z.index[:duration])

#ok just doing everything on the SECOND index, so be aware of that. 
ax.plot(y.index[:duration], z.values[:duration], label = '2024')    
ax.plot(y.index, y.values, label = '2023') 
ax.plot(y.index, x.values, label = '2022')
ax.plot(y.index, w.values, label = '2021')
ax.plot(y.index, v.values, label = '2020')

ax.legend(loc="upper left")


#set date format on x axis
ax.xaxis.set_major_formatter(mdates.DateFormatter('%#b-%#d'))



plt.show()
affinis_state_breakdown(species)

print ("done")



