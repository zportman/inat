from pyinaturalist import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import pandas as pd
import time
import csv


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

def midwest_state_breakdown(species, year1, year2):
    #species should be the iNat number
    #Given a year1, year2, and a species, creates the 4 state midwest plot for the given years

    fig1, ax1 = plt.subplots(nrows=2, ncols=2, figsize=(9, 6))
    fig1.tight_layout(pad=2) 
    
    #First Minnesota
    
    ax1[0,0].set_title('Minnesota', y=0.95)
    xaxis = pd.Series() #set the container for the x axis
    
    for year in range(year1, year2):
        cumulative = get_day_histogram(species, dt.datetime(year, 3, 1), dt.datetime(year, 10, 31), "38")
        cumulative = np.cumsum(cumulative)
        
        #need to use a constant values for x axis for reasons that will forever remain unknown....
        if xaxis.empty:
            xaxis = cumulative
        ax1[0,0].plot(xaxis.index, cumulative.values, label = str(year))
        

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)    
    ax1[0,0].legend(loc="upper left", reverse=True)    
    ax1[0,0].xaxis.set_major_formatter(mdates.DateFormatter('%#b-%#d'))      
    
    
    ax1[0,1].set_title('Wisconsin', y=0.95, pad = 2)
    xaxis = pd.Series() #set the container for the x axis
    
    
    for year in range(year1, year2):
        cumulative = get_day_histogram(species, dt.datetime(year, 3, 1), dt.datetime(year, 10, 31), "32")
        cumulative = np.cumsum(cumulative)
        
        #need to use a constant values for x axis for reasons that will forever remain unknown....
        if xaxis.empty:
            xaxis = cumulative        
        ax1[0,1].plot(xaxis.index, cumulative.values, label = str(year))
        

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)    
    ax1[0,1].legend(loc="upper left", reverse=True)    
    ax1[0,1].xaxis.set_major_formatter(mdates.DateFormatter('%#b-%#d'))      
        
    
    
    
    ax1[1,0].set_title('Iowa', y=0.95, pad = 2)
    xaxis = pd.Series() #set the container for the x axis
    
    for year in range(year1, year2):
        cumulative = get_day_histogram(species, dt.datetime(year, 3, 1), dt.datetime(year, 10, 31), "24")
        cumulative = np.cumsum(cumulative)
        #need to use a constant values for x axis for reasons that will forever remain unknown....
        if xaxis.empty:
            xaxis = cumulative        
        ax1[1,0].plot(xaxis.index, cumulative.values, label = str(year))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)    
    ax1[1,0].legend(loc="upper left", reverse=True)    
    ax1[1,0].xaxis.set_major_formatter(mdates.DateFormatter('%#b-%#d'))
    
    
    
    ax1[1,1].set_title('Illinois', y=0.95, pad = 2)
    xaxis = pd.Series() #set the container for the x axis
    
    for year in range(year1, year2):
        cumulative = get_day_histogram(species, dt.datetime(year, 3, 1), dt.datetime(year, 10, 31), "35")
        cumulative = np.cumsum(cumulative)
        #need to use a constant values for x axis for reasons that will forever remain unknown....
        if xaxis.empty:
            xaxis = cumulative        
        ax1[1,1].plot(xaxis.index, cumulative.values, label = str(year))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)    
    ax1[1,1].legend(loc="upper left", reverse=True)    
    ax1[1,1].xaxis.set_major_formatter(mdates.DateFormatter('%#b-%#d'))    
    
    plt.savefig('output/' + species_list[species] + '.png')
    
    plt.show()
    


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
    Twent_twentyfive = get_day_histogram(species, dt.datetime(2025, 3, 1), dt.datetime(2025, 10, 31), "38")   
    

    
    
    v = np.cumsum(Twent_twentytwenty) 
    w = np.cumsum(Twent_twentyone) 
    x = np.cumsum(Twent_twentytwo) 
    y = np.cumsum(Twent_twentythree) 
    z = np.cumsum(Twent_twentyfour)  
    a = np.cumsum(Twent_twentyfive)     
    
    
      
    ax1[0,0].set_title('Minnesota', y=0.95)
    
    ax1[0,0].plot(z.index, v.values, label = '2020')
    ax1[0,0].plot(z.index, w.values, label = '2021')
    ax1[0,0].plot(z.index, x.values, label = '2022')
    ax1[0,0].plot(z.index, y.values, label = '2023') 
    ax1[0,0].plot(z.index, z.values, label = '2024')    
    #ax1[0,0].plot(z.index, a.values, label = '2025')    
    
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)    
    ax1[0,0].legend(loc="upper left", reverse=True)    
    ax1[0,0].xaxis.set_major_formatter(mdates.DateFormatter('%#b-%#d'))
    
    
    #second Wisconsin
    Twent_twentytwenty = get_day_histogram(species, dt.datetime(2020, 3, 1), dt.datetime(2020, 10, 31), "32")
    Twent_twentyone = get_day_histogram(species, dt.datetime(2021, 3, 1), dt.datetime(2021, 10, 31), "32")
    Twent_twentytwo = get_day_histogram(species, dt.datetime(2022, 3, 1), dt.datetime(2022, 10, 31), "32")
    Twent_twentythree = get_day_histogram(species, dt.datetime(2023, 3, 1), dt.datetime(2023, 10, 31), "32")
    Twent_twentyfour = get_day_histogram(species, dt.datetime(2024, 3, 1), dt.datetime(2024, 10, 31), "32")   
    #Twent_twentyfive = get_day_histogram(species, dt.datetime(2025, 3, 1), dt.datetime(2025, 10, 31), "32")   
    
    
    v = np.cumsum(Twent_twentytwenty) 
    w = np.cumsum(Twent_twentyone) 
    x = np.cumsum(Twent_twentytwo) 
    y = np.cumsum(Twent_twentythree) 
    z = np.cumsum(Twent_twentyfour)
    a = np.cumsum(Twent_twentyfive)     
    
    
    ax1[0,1].set_title('Wisconsin', y=0.95, pad = 2)
    
    ax1[0,1].plot(z.index, v.values, label = '2020')
    ax1[0,1].plot(z.index, w.values, label = '2021')
    ax1[0,1].plot(z.index, x.values, label = '2022')
    ax1[0,1].plot(z.index, y.values, label = '2023') 
    ax1[0,1].plot(z.index, z.values, label = '2024')    
    #ax1[0,1].plot(z.index, a.values, label = '2025')    
    
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)    
    ax1[0,1].legend(loc="upper left", reverse=True)    
    ax1[0,1].xaxis.set_major_formatter(mdates.DateFormatter('%#b-%#d'))    
    
    
    #third iowa
    Twent_twentytwenty = get_day_histogram(species, dt.datetime(2020, 3, 1), dt.datetime(2020, 10, 31), "24")
    Twent_twentyone = get_day_histogram(species, dt.datetime(2021, 3, 1), dt.datetime(2021, 10, 31), "24")
    Twent_twentytwo = get_day_histogram(species, dt.datetime(2022, 3, 1), dt.datetime(2022, 10, 31), "24")
    Twent_twentythree = get_day_histogram(species, dt.datetime(2023, 3, 1), dt.datetime(2023, 10, 31), "24")
    Twent_twentyfour = get_day_histogram(species, dt.datetime(2024, 3, 1), dt.datetime(2024, 10, 31), "24") 
    Twent_twentyfive = get_day_histogram(species, dt.datetime(2025, 3, 1), dt.datetime(2025, 10, 31), "24")   
    
    
    v = np.cumsum(Twent_twentytwenty) 
    w = np.cumsum(Twent_twentyone) 
    x = np.cumsum(Twent_twentytwo) 
    y = np.cumsum(Twent_twentythree) 
    z = np.cumsum(Twent_twentyfour) 
    a = np.cumsum(Twent_twentyfive)     
    
    
    ax1[1,0].set_title('Iowa', y=0.95, pad = 2)
    
    ax1[1,0].plot(z.index, v.values, label = '2020')
    ax1[1,0].plot(z.index, w.values, label = '2021')
    ax1[1,0].plot(z.index, x.values, label = '2022')
    ax1[1,0].plot(z.index, y.values, label = '2023') 
    ax1[1,0].plot(z.index, z.values, label = '2024')    
    #ax1[1,0].plot(z.index, a.values, label = '2025')    
    
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)    
    ax1[1,0].legend(loc="upper left", reverse=True)    
    ax1[1,0].xaxis.set_major_formatter(mdates.DateFormatter('%#b-%#d'))  
    
    #fourth Illinois
    Twent_twentytwenty = get_day_histogram(species, dt.datetime(2020, 3, 1), dt.datetime(2020, 10, 31), "35")
    Twent_twentyone = get_day_histogram(species, dt.datetime(2021, 3, 1), dt.datetime(2021, 10, 31), "35")
    Twent_twentytwo = get_day_histogram(species, dt.datetime(2022, 3, 1), dt.datetime(2022, 10, 31), "35")
    Twent_twentythree = get_day_histogram(species, dt.datetime(2023, 3, 1), dt.datetime(2023, 10, 31), "35")
    Twent_twentyfour = get_day_histogram(species, dt.datetime(2024, 3, 1), dt.datetime(2024, 10, 31), "35")   
    Twent_twentyfive = get_day_histogram(species, dt.datetime(2025, 3, 1), dt.datetime(2025, 10, 31), "35")   
    
    
    #trying out excluded observors
    Twent_twentyfour = get_day_histogram_minus_observers(species, dt.datetime(2024, 3, 1), dt.datetime(2024, 10, 31), "35", excluded_observers = ['barty', 'wmct276'])   #    
    #
    v = np.cumsum(Twent_twentytwenty) 
    w = np.cumsum(Twent_twentyone) 
    x = np.cumsum(Twent_twentytwo) 
    y = np.cumsum(Twent_twentythree) 
    z = np.cumsum(Twent_twentyfour) 
    a = np.cumsum(Twent_twentyfive)     
    
    
    ax1[1,1].set_title('Illinois', y=0.95, pad = 2)
    
    ax1[1,1].plot(z.index, v.values, label = '2020')
    ax1[1,1].plot(z.index, w.values, label = '2021')
    ax1[1,1].plot(z.index, x.values, label = '2022')
    ax1[1,1].plot(z.index, y.values, label = '2023') 
    ax1[1,1].plot(z.index, z.values, label = '2024')    
    #ax1[1,1].plot(z.index, a.values, label = '2025')    
    
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)    
    ax1[1,1].legend(loc="upper left", reverse=True)    
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
    
def get_day_histogram(species, time1, time2, place="97394"): #place = north america
    #Time should be in datetime format, but I don't think it need to be, check pyinat docs
    #Default place ID is set to North America.
    
    #get a histogram of days observed
    #histogram = get_observation_histogram(taxon_id=species, interval = 'day', d1=time1, d2 = time2, quality_grade='research')
    #histogram = get_observation_histogram(taxon_id=species, interval = 'day', d1=time1, d2 = time2, quality_grade='research',
    #                                      nelat='64.18813159901904', nelng='-50', swlat ='22', swlng='-100' )
    ###histogram = get_observation_histogram( taxon_id=species, interval = 'day', d1=time1, d2 = time2, quality_grade='research',   place_id=place)
    histogram = get_observation_histogram( taxon_id=species, interval = 'day', d1=time1, d2 = time2, verifiable='true',   place_id=place)
    
    
    print("histogram:",histogram)

    days = pd.Series(histogram)
    
    #ok I'm going insane because it doesn't report all the dates, they start from first occurrence. Dunno why. Need to fill in the missing zeros...
    #I love stackoverflow: https://stackoverflow.com/questions/19324453/add-missing-dates-to-pandas-dataframe
    
    idx = pd.date_range(time1, time2)
    days.index = pd.DatetimeIndex(days.index)
    days = days.reindex(idx, fill_value=0)
    
    return days



def get_day_histogram_minus_observers(species, time1, time2, place="97394", excluded_observers = ''): #place = north america
    """new variant that will remove certain observers that are specified"""
    #Time should be in datetime format, but I don't think it need to be, check pyinat docs
    #Default place ID is set to North America.
    
    #get a histogram of days observed
    #histogram = get_observation_histogram(taxon_id=species, interval = 'day', d1=time1, d2 = time2, quality_grade='research')
    #histogram = get_observation_histogram(taxon_id=species, interval = 'day', d1=time1, d2 = time2, quality_grade='research',
    #                                      nelat='64.18813159901904', nelng='-50', swlat ='22', swlng='-100' )
    ###histogram = get_observation_histogram( taxon_id=species, interval = 'day', d1=time1, d2 = time2, quality_grade='research',   place_id=place)
    histogram = get_observation_histogram( taxon_id=species, interval = 'day', d1=time1, d2 = time2, verifiable='true',   place_id=place)
    
    print("histogram:",histogram)

    days = pd.Series(histogram)
    
    #ok I'm going insane because it doesn't report all the dates, they start from first occurrence. Dunno why. Need to fill in the missing zeros...
    #I love stackoverflow: https://stackoverflow.com/questions/19324453/add-missing-dates-to-pandas-dataframe
    
    idx = pd.date_range(time1, time2)
    days.index = pd.DatetimeIndex(days.index)
    days = days.reindex(idx, fill_value=0)
    
    #get the data for the excluded user, fill it, and subtract it....
    if excluded_observers != '':
        for excluded in excluded_observers:
            histogram = get_observation_histogram( taxon_id=species, interval = 'day', d1=time1, d2 = time2, quality_grade='research',   place_id=place, user_id = excluded)
    
            excluded_days = pd.Series(histogram)
            
            idx = pd.date_range(time1, time2)
            excluded_days.index = pd.DatetimeIndex(excluded_days.index)
            excluded_days = excluded_days.reindex(idx, fill_value=0)    
            
            print( excluded, excluded_days.value_counts())
            
            print ("OLD DAYS", days.value_counts())
            
            days = days - excluded_days
            
            print( "NEW DAYS", days.value_counts())
            
    
    return days



def get_Bombus_midwest_table(species, year1=2020, year2= 2025):
    #Here, given a species, autogenerate a table for csv showing total bombus observations and species of interest for 2020-2025 and print to a csv...
    #this does not pull in private observations since it limits by state...
    
    output = [['Year', "All Midwest Bombus", "Midwest " + species_list[species], "MN " + species_list[species], "WI " + species_list[species], "IA " + species_list[species], "IL " + species_list[species]]]
    all_bombus = '52775' # ALL BOMBUS
    
    
    years_list = list(range(year1, year2+1))
    
    for year in years_list:
        
        bombus_records = get_day_histogram(all_bombus, dt.datetime(year, 3, 1), dt.datetime(year, 10, 31), ["38", "32", "24", "35"])
        all_bombus_totals = np.cumsum(bombus_records).iloc[-1]     
        
        species_records = get_day_histogram(species, dt.datetime(year, 3, 1), dt.datetime(year, 10, 31), ["38", "32", "24", "35"])
        species_totals = np.cumsum(species_records).iloc[-1]
        
        
        mn_records = get_day_histogram(species, dt.datetime(year, 3, 1), dt.datetime(year, 10, 31), 38)
        mn_species_totals = np.cumsum(mn_records).iloc[-1]     
        wi_records = get_day_histogram(species, dt.datetime(year, 3, 1), dt.datetime(year, 10, 31), 32)
        wi_species_totals = np.cumsum(wi_records).iloc[-1]      
        ia_records = get_day_histogram(species, dt.datetime(year, 3, 1), dt.datetime(year, 10, 31), 24)
        ia_species_totals = np.cumsum(ia_records).iloc[-1]              
        il_records = get_day_histogram(species, dt.datetime(year, 3, 1), dt.datetime(year, 10, 31), 35)
        il_species_totals = np.cumsum(il_records).iloc[-1]  
        
        #should also add in for each individual state.....
        
        
        #then just add year, bombus totals, and species totals to output table list
        
        output += [[year, all_bombus_totals, species_totals, mn_species_totals, wi_species_totals, ia_species_totals, il_species_totals]]
        print ("OOOOOOOOOOOOOOUTPUT", output)
    
    #last do column sums
    arr = np.array(output[1:])
    column_sums = np.sum(arr, axis=0)
    column_sums[0] = 0
    print ("COLUMN SUMS: ", column_sums)
    output += [column_sums.tolist()]
        
    #then shunt to csv    
    with open("bombus_totals.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(output)        

        
   

species_list = {'52775': "Bombus", '121519': "B. affinis", '198857': "B. ashtoni", '198856': "B. auricomus", '52779': "B. bimaculatus", 
                '143854': "B. borealis", '198859': "B. citrinus", '271451': "B. crotchii", '52774': "B. fervidus", '541839': "B. flavidus", 
                '308937': "B. fraternus", '120215': "B. griseocollis", '118970': "B. impatiens",
                '143036': "B. insularis", '82371': "B. occidentalis", '155085': "B. perplexus",
                '56887': "B. pensylvanicus", '144011': "B. rufocinctus", '127905': "B. ternarius", '121517': "B. terricola", '128670': "B. vagans", '51110': "Xylocopa virginica",
                '127812': "All Hylaeus"}

species = '198857' #ashtoni
species = '82371' #occidentalis
species = '541839' #flavidus
species = '271451' #crotchii


species = '128670' #vagans
species = '51110'#Xylocopa virginica

species = '52775' # ALL BOMBUS
species = '127812' #all Hylaeus

species = '121517' #terricola
species = '308937' #fraternus
species = '143036' #insularis

species = '52774' #fervidus
species = '127905' #ternarius
species = '198859' #citrinus
species = '155085' #perplexus
species = '56887' #pensylvanicus
species = '198856' #auricomus
species = '118970' #impatiens
species = '52775' # ALL BOMBUS
species = '143854' #borealis
species = '144011' #rufocinctus
species = '120215' #griseocollis
species = '52779' #bimaculatus
species = '121519' #affinis



#try out table:
get_Bombus_midwest_table(species)


Twent_twentytwenty = get_day_histogram(species, dt.datetime(2020, 3, 1), dt.datetime(2020, 10, 31))
Twent_twentyone = get_day_histogram(species, dt.datetime(2021, 3, 1), dt.datetime(2021, 10, 31))
Twent_twentytwo = get_day_histogram(species, dt.datetime(2022, 3, 1), dt.datetime(2022, 10, 31))
Twent_twentythree = get_day_histogram(species, dt.datetime(2023, 3, 1), dt.datetime(2023, 10, 31))
Twent_twentyfour = get_day_histogram(species, dt.datetime(2024, 3, 1), dt.datetime(2024, 10, 31))
Twent_twentyfive = get_day_histogram(species, dt.datetime(2025, 3, 1), dt.datetime(2025, 10, 31))


v = np.cumsum(Twent_twentytwenty) 
w = np.cumsum(Twent_twentyone) 
x = np.cumsum(Twent_twentytwo) 
y = np.cumsum(Twent_twentythree) 
z = np.cumsum(Twent_twentyfour) 
a = np.cumsum(Twent_twentyfive) 


#print out sums cuz why not
print ("2020 total", w[-1])
print ("W", w)


#plotting!!
fig = plt.figure(figsize=[8,5])

ax = fig.add_subplot(111)
ax.set_title(r'All records of $' + species_list[species] + '$', y=0.95, pad = 2)



print (y)

#here gonna trim z to not go beyond current date
duration = datetime.now() - dt.datetime(2024, 3, 1)
duration = duration.days + 1 #adding 1 to prevent off by 1 apparently...
print ("duration", z.index[:duration])

#ok just doing everything on the SECOND index, so be aware of that.
ax.plot(y.index[:duration], v.values[:duration], label = '2020')    
ax.plot(y.index, w.values, label = '2021')
ax.plot(y.index, x.values, label = '2022')
ax.plot(y.index, y.values, label = '2023') 
ax.plot(y.index, z.values, label = '2024') 
ax.plot(y.index, a.values, label = '2025')


ax.legend(loc="upper left", reverse=True)


#set date format on x axis
ax.xaxis.set_major_formatter(mdates.DateFormatter('%#b-%#d'))



plt.show()


#try multiple states:
Twent_twentytwenty = get_day_histogram(species, dt.datetime(2020, 3, 1), dt.datetime(2020, 10, 31), ["38", "32", "24", "35"])
Twent_twentyone = get_day_histogram(species, dt.datetime(2021, 3, 1), dt.datetime(2021, 10, 31), ["38", "32", "24", "35"])
Twent_twentytwo = get_day_histogram(species, dt.datetime(2022, 3, 1), dt.datetime(2022, 10, 31), ["38", "32", "24", "35"])
Twent_twentythree = get_day_histogram(species, dt.datetime(2023, 3, 1), dt.datetime(2023, 10, 31), ["38", "32", "24", "35"])
Twent_twentyfour = get_day_histogram(species, dt.datetime(2024, 3, 1), dt.datetime(2024, 10, 31), ["38", "32", "24", "35"])
Twent_twentyfive = get_day_histogram(species, dt.datetime(2025, 3, 1), dt.datetime(2025, 10, 31), ["38", "32", "24", "35"])


v = np.cumsum(Twent_twentytwenty) 
w = np.cumsum(Twent_twentyone) 
x = np.cumsum(Twent_twentytwo) 
y = np.cumsum(Twent_twentythree) 
z = np.cumsum(Twent_twentyfour) 
a = np.cumsum(Twent_twentyfive) 


print ("2020 total", v.iloc[-1]) #huh guess it works :)
print ("2021 total", w.iloc[-1])
print ("2022 total", x.iloc[-1])
print ("2023 total", y.iloc[-1])
print ("2024 total", z.iloc[-1])
print ("2025 total", a.iloc[-1])


#plotting!!
fig = plt.figure(figsize=[8,5])

ax = fig.add_subplot(111)
ax.set_title('All Bombus observations (IA, IL, MN, WI)', y=0.95, pad = 2)
ax.set_title(r'All Midwest $' + species_list[species] + '$ (IA, IL, MN, WI)', y=0.95, pad = 2)


#here gonna trim z to not go beyond current date
duration = datetime.now() - dt.datetime(2024, 3, 1)
duration = duration.days + 1 #adding 1 to prevent off by 1 apparently...
print ("duration", z.index[:duration])

#ok just doing everything on the SECOND index, so be aware of that. 
ax.plot(y.index[:duration], v.values[:duration], label = '2020')    
ax.plot(y.index, w.values, label = '2021')
ax.plot(y.index, x.values, label = '2022')
ax.plot(y.index, y.values, label = '2023') 
ax.plot(y.index, z.values, label = '2024') 
ax.plot(y.index, a.values, label = '2025')


ax.legend(loc="upper left", reverse=True)
ax.tick_params(axis='both', labelsize=11) # for both x and y axes


#set date format on x axis
ax.xaxis.set_major_formatter(mdates.DateFormatter('%#b-%#d'))



plt.show()


#affinis_state_breakdown(species)
midwest_state_breakdown(species, 2020, 2026)


"""
for species in species_list:
    midwest_state_breakdown(species, 2020, 2026)
    time.sleep(10) #stop from getting throttled
"""

#running the deprecated method in order to get the illinois minus the 2 observers:
#affinis_state_breakdown(species)


print ("done")



#TODO: run overall and state methods but exclude observers with a number of observations over a certain cutoff
# could make a method pretty easily to get a list of observers with great number in total and also in a given state and then feed them to exclude.