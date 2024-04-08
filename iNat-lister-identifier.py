from pyinaturalist import *
import json

"""This is a script to organize iNaturalist observations in a taxonomy/list view since all the existing iNat views are incredibly clunky"""
"""Here modifie to look at identified observatoins by a user"""
# Created by Zach Portman, 23 Sep 2023

#Todo -- exclude casual observations, wah.


#98755 is nesting bees. 88826 is concentrating nectar. 98868 is mating bees. 98851 is sleepy bees
#predation of bees is 122506
#all bee observations is 185321

#zach user ID = 318825 or can just use 'zportman'
# can also get ID by fully searching for them in the general search and clicking on their name

project = 185321
user_ID = 'zportman'

#old query for the project
####response = get_observation_taxonomy(project_id= project, verifiable=True) # oh wow this works....gets counts of all taxa, whether leaf or node

#trying to get just the ones I identified
response = get_observation_taxonomy(project_id= project, verifiable=any, ident_user_id=user_ID) # all bees I identified for a given project, need to find all bees project


#first get rid of the wrapper that holds all the dictionaries
data = response["results"]

#ok I am dumb so just looping through the quick, dirty, and harcoded way
all_taxa = []
temp = []
parents = {} # a way to keep track of who is parent to who, willbe parent[child] format
all_names_and_IDs = {} # need a way to keep track of names and IDs for later converting 

for entry in data:
    print (entry)
    if "count" in entry:
        temp = [entry["id"], entry["count"], entry["name"], entry["rank"], entry["rank_level"], entry["parent_id"], entry["descendant_obs_count"],entry["direct_obs_count"]]
    elif "parent_id" in entry: #this works since life has neither count or parent ID
        temp = [entry["id"], 0, entry["name"], entry["rank"], entry["rank_level"], entry["parent_id"], entry["descendant_obs_count"],entry["direct_obs_count"]]        
    else: #is life, so no parent or county# https://www.inaturalist.org/observations?taxon_id=48460 #they changed life so it has no name anymore? blarf. 
        #temp = [entry["id"], 0, entry["name"], entry["rank"], entry["rank_level"], 0, entry["descendant_obs_count"],entry["direct_obs_count"]] #old code thatbroke
        continue #lets try this and just hardcode it later, lol. Life breaks it because itlacks many of the fields
        
        
        
    if "parent_id" in entry:
        parents[entry["id"]] = entry["parent_id"]
        
    all_names_and_IDs[entry["id"]] = entry["name"]
        
    all_taxa += [temp]
    

parents[48460] = 0  # final hack - give the highest level a zero ancestor
parents[0] = 0   # hardcoding this because it creates errors
all_names_and_IDs[0] = 'a'
all_names_and_IDs[48460] = 'Life' #hardcoding this because it broke the code, shrug emoji



print ("all names and IDs" , all_names_and_IDs)


#ok, next step is to loop through each taxa, get all the ancestors, convert that into a word string,and append to it, for later sorting easierness.
for taxa in all_taxa:
    #print ("taxa", taxa)
    ancestor = parents[taxa[0]] # look up the ancestor in the dictionary
    #print (ancestor)
    temp_ancestry_string = all_names_and_IDs[ancestor]
    
    while ancestor !=48460 and ancestor != 0:
        ancestor = parents[ancestor]
        #print (ancestor)
        temp_ancestry_string = all_names_and_IDs[ancestor] + temp_ancestry_string
        
    
    #also add the current name to ancestry thing for sorting help for later
    temp_ancestry_string += all_names_and_IDs[taxa[0]]
    
    taxa += [temp_ancestry_string]
    #print (temp_ancestry_string)
        

    
#plan: step 1 make aparent dictionary, then use (https://stackoverflow.com/questions/47497117/creating-hierarchical-tree-from-nested-dictionary-in-python) to get ancestors of each node
#then, can just sort by ancestors and rank, and just print out tab based on rank  
print (all_taxa)
all_taxa = sorted(all_taxa, key=lambda x:x[-1])

print (parents)
print ("all names and IDs" , all_names_and_IDs)



#ok, now I guess it just the final output, wow. Gotta do html I thinkythink.
final_string = ""

for taxa in all_taxa:
    spacing_length = ((32 - int(taxa[4])) * 2 ) * "." #this is for bees projecs
    #spacing_length = ((60 - int(taxa[4])) * 2 ) * "."# this is for predationof bees
    
    #ok here we ae just setting upt he species names
    final_string = final_string + spacing_length +  str(taxa[3]).capitalize() + " " + str(taxa[2]) + " " 
    
    #gonna handle species and subpecies different (removing the strict critera)
    
    if taxa[3] != "species" and taxa[3] != "subspecies":
    
        #now we are getting the link to the observations
        link = "https://www.inaturalist.org/observations?project_id=" + str(project) + "&place_id=any&verifiable=any&captive=any&taxon_id=" + str(taxa[0]) + "&lrank=" + taxa[3] + "&ident_user_id=" + str(user_ID) # +"&ident_taxon_id=318825"
        
        
        #do observations with children (total observations)
        link2 = "https://www.inaturalist.org/observations?project_id=" + str(project) + "&place_id=any&verifiable=any&captive=any&taxon_id=" + str(taxa[0]) + "&ident_user_id=" + str(user_ID)
        final_string = final_string + " " + "<a href='" + link2 + "'>" + str(taxa[6]) + " observations</a>"   
        
        #then do unidentified observations
        final_string = final_string + " ("+  "<a href='" + link + "'>" + str(taxa[7]) + "</a>" + " not identified further)" 
        
    
    else: #they are species or subspecies, so don't boter with strict vs inlusive observations, only do inclusive
        link = "https://www.inaturalist.org/observations?project_id=" + str(project) + "&place_id=any&verifiable=any&captive=any&taxon_id=" + str(taxa[0]) + "&ident_user_id=" + str(user_ID)
        final_string = final_string  +   "<a href='" + link + "'>" + str(taxa[6]) +" observations" + "</a>"          
        
    
    #now closing off each taxa
    final_string = final_string + "<br>" + "\n"  #can't use the br if pasting into iNat journal cuz it creates extraneous newlines
    #final_string = final_string +  "\n"  #can't use the br if pasting into iNat journal cuz it creates extraneous newlines
    
    #final_string = final_string + "\n"

#Idea -- can change from strict vs inclusive observations to XX observations not identified to species?


information_string = ""
for taxa in all_taxa:
    information_string = information_string + str(taxa) + "<br>"

f = open("Identifier_page_full_info.html", 'w')
f.write(information_string)
f.close()

f = open("Identifier_page_formatted.html", 'w')
f.write(final_string)
f.close()

print ("done done done")



###example of link you want: this is apis mellifera innesting beeshttps://www.inaturalist.org/observations?project_id=98755&place_id=any&verifiable=any&captive=any&taxon_id=47219

### alsohere is the begning of the taxa teree...but how to expand it out? https://www.inaturalist.org/taxa/search?q=47219%26project+id%3D98755&taxon_id=630955

#taxonomy - tree wise, is there a function to get the taxonomy tree for an individual observation? If so, could sort that somehow, even just alphabetically
# ie could even lump everything into a string and just sort alphabetically lol


#interesting: https://www.inaturalist.org/observations?captive=any&place_id=any&project_id=98755&taxon_id=1&verifiable=any&lrank=kingdom lrank can be used to get :)