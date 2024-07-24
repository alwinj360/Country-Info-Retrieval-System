from irsystems.countryIRSystemList import CountryIRSystemList
from irsystems.countryIRSystemBSTDict import countryIRSystemBSTDict
from irsystems.countryIRSystemLLDict import CountryIRSystemLLDict
from irsystems.countryIRSystemSLDict import CountryIRSystemSLDict
from irsystems.countryIRSystemHTDict import CountryIRSystemHTDict

import time # importing the time to calcuate the time needed to run the queries
import random # generating random numbers


def countryIRSystem_analysis(rand_file_name, no_queries, no_entries):
    # rand_file_name: the name of the file containing the random data
    # no_queries: the number of queries to run on the system
    # no_entries: the max number of entries in the file
    # this function is responsible for including all the necessary code to analyze the performance of the system

    # countryIRSystem based on list
    countryIRS_List = CountryIRSystemList()
    countryIRS_List.load_data(rand_file_name)

    # countryIRSystem based on Binary Search Tree Dictionary
    countryIRS_BST = countryIRSystemBSTDict()
    countryIRS_BST.load_data(rand_file_name)

    # countryIRSystem based on Linked List Dictionary
    countryIRS_LL = CountryIRSystemLLDict()
    countryIRS_LL.load_data(rand_file_name)

    # countryIRSystem based on Sorted List Dictionary
    countryIRS_SL = CountryIRSystemSLDict()
    countryIRS_SL.load_data(rand_file_name)

    # countryIRSystem based on Hash Table Dictionary
    countryIRS_HT = CountryIRSystemHTDict()
    countryIRS_HT.load_data(rand_file_name)

    # generating no_queries random queries 
    # using the random life expectancies
    random_country_names_list = []
    for i in range(0,no_queries):
        n = "India" + str(random.randint(1, no_entries))
        random_country_names_list.append(n)
    

    # Starting time calculation for List based implementation
    start_time = time.time()
    results1 = []
    #running the no_queries query search
    for rand_country_name in random_country_names_list:
      result = countryIRS_List.search_country(rand_country_name)
      results1.append(result)
    #calculating the time after the for loop
    end_time = time.time()
    # calculating how long it took to run the 1000 queries
    print("No of entries: "+ str(no_entries))
    print("searching " + str(no_queries) + " queries using the List based implementation: --- %s seconds ---" % (end_time - start_time))  

    # Starting the time calculation for the BST Dict based implementation
    start_time2 = time.time()
    results2 = []
    #running the no_queries query search
    for rand_country_name in random_country_names_list:
      result = countryIRS_BST.search_country(rand_country_name)
      results2.append(result)
    #calculating the time after the for loop
    end_time2 = time.time()
    # calculating how long it took to run the 1000 queries
    print("searching " + str(no_queries) + " queries using the BST_Dict based implementation: --- %s seconds ---" % (end_time2 - start_time2)) 

    
    # Starting the time calculation for the LL Dict based implementation
    start_time3 = time.time()
    results3 = []
    #running the no_queries query search
    for rand_country_name in random_country_names_list:
      result = countryIRS_LL.search_country(rand_country_name)
      results3.append(result)
    
    #calculating the time after the for loop
    end_time3 = time.time()
    # calculating how long it took to run the 1000 queries
    print("searching " + str(no_queries) + " queries using the LL_Dict based implementation: --- %s seconds ---" % (end_time3 - start_time3)) 
    

    # Starting the time calculation for the SL Dict based implementation
    start_time4 = time.time()
    results4 = []
    #running the no_queries query search
    for rand_country_name in random_country_names_list:
      result = countryIRS_SL.search_country(rand_country_name)
      results4.append(result)
    #calculating the time after the for loop
    end_time4 = time.time()
    # calculating how long it took to run the 1000 queries
    print("searching " + str(no_queries) + " queries using the SL_Dict based implementation: --- %s seconds ---" % (end_time4 - start_time4)) 
    

    # Starting the time calculation for the HT Dict based implementation
    start_time5 = time.time()
    results5 = []
    #running the no_queries query search
    for rand_country_name in random_country_names_list:
      result = countryIRS_HT.search_country(rand_country_name)
      results5.append(result)
      break
    #calculating the time after the for loop
    end_time5 = time.time()
    # calculating how long it took to run the 1000 queries
    print("searching " + str(no_queries) + " queries using the HT_Dict based implementation: --- %s seconds ---" % (end_time5 - start_time5)) 
