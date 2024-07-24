from dict.abstract import CountryIRSystemAbstract
from dict.htdict import HTDict
from otherFiles.country import Country
import csv


class CountryIRSystemHTDict(CountryIRSystemAbstract):
  def __init__(self):
    self._cInventory = HTDict()

  def load_data(self, file_name):
    with open (file_name, "r") as csvfile:
      csvreader = csv.reader(csvfile)

      for lines in csvreader:
        country = Country()

        country._country_name = lines[2]
        country._country_code = lines[3]
        country._population_total = lines[4]
        country._life_expectancy_at_birth = lines[5]
        country._access_to_clean_fuel_and_tech = lines[6]
        country._using_basic_drinking_water = lines[7]
        country._GDP_per_capita = lines[8]

        self._cInventory[country._country_name] = country

  # A function to retrieve a given country object from the hash table.
  # Written by: Alwin
  def search_country(self, country_name):
    if country_name in self._cInventory:
      return self._cInventory[country_name]

  #By: Elyas
  #Edited by Alwin and Vel
  def series_for_given_country(self, inp, strg_country):
    c = self.search_country(strg_country) # returns correct country obj or none
    if c is not None: # check for none case
      if inp == '1':
        s = c._population_total # holds series data if found
      elif inp == '2':
        s = c._life_expectancy_at_birth
      elif inp == '3':
        s = c._access_to_clean_fuel_and_tech
      elif inp == '4':
        s = c._using_basic_drinking_water
      elif inp == '5':
        s = c._GDP_per_capita
      return s
    return c # if c is none, it will return it.


  # By: Elyas
  # Edited by: Alwin 05/14/2023
    # Modified the function to run using the "values" function
    # so that we have the same "given_series_for_all_countries" function
    # across all the steps from 6 through 9.
  def given_series_for_all_countries(self, inp):
    # Stores all country objects in a list.
    countryList = self._cInventory.values()
    outputList = []
    # Iterates through each country obj in countryList and appends the
    # necessary development indicator (based on "inp") to the output list.
    for country in countryList:
      if inp == '1':
        outputList.append(str(country._country_name) + "\n\t" + str(country._population_total))
      elif inp == '2':
        outputList.append(str(country._country_name) + "\n\t" + str(country._life_expectancy_at_birth))
      elif inp == '3':
        outputList.append(str(country._country_name) + "\n\t" + str(country._access_to_clean_fuel_and_tech))
      elif inp == '4':
        outputList.append(str(country._country_name) + "\n\t" + str(country._using_basic_drinking_water))
      elif inp == '5':
        outputList.append(str(country._country_name) + "\n\t" + str(country._GDP_per_capita))
    return outputList


  #Author: Vel
  #Function to find the minimum value for a given input 
  def find_min(self, inp):
    values = self._cInventory.values() 

    #Initializes with the appropriate value for the given input
    init_dict = { 1: values[0]._population_total, 
                  2: values[0]._life_expectancy_at_birth, 
                  3: values[0]._access_to_clean_fuel_and_tech, 
                  4: values[0]._using_basic_drinking_water,
                  5: values[0]._GDP_per_capita }

    min = init_dict[inp]
    name = values[0]._country_name
    for i in values:
      min_dict = { 1: i._population_total, 
                    2: i._life_expectancy_at_birth, 
                    3: i._access_to_clean_fuel_and_tech, 
                    4: i._using_basic_drinking_water,
                    5: i._GDP_per_capita }
      if float(min_dict[inp]) < float(min):
        min = min_dict[inp]
        name = i._country_name
    return name + " " + min

  # Written by: Vel
  # given an input coded for a specific indicator, the output will be the
  # largest data record for that indicator
  def find_max(self, inp):
    values = self._cInventory.values() 

    max = 0.0
    name = values[0]._country_name
    for i in values:
      max_dict = { 1: i._population_total, 
                    2: i._life_expectancy_at_birth, 
                    3: i._access_to_clean_fuel_and_tech, 
                    4: i._using_basic_drinking_water,
                    5: i._GDP_per_capita }
      if float(max_dict[inp]) > float(max):
        max = max_dict[inp]
        name = i._country_name
    return name + " " + max


  # Made for testing purposes
  def HTPrint(self):
    self._cInventory.printAll()
