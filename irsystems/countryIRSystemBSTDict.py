# Authors: Vel Perez-Barba
#          Elyas Ehsan
#          Alwin Alwin Joseph

# Description: An information retrieval system that stores its objects in a binary search tree. This file also contains the associated functions of this system.

from dict.bstdict import *
from dict.abstract import *
from otherFiles.country import Country
import csv

#Edited by: Elyas (documentation)
class countryIRSystemBSTDict(CountryIRSystemAbstract):

  """This class uses a series of functions from our previous CountryIRSystem. The only difference with this one is that now we are using dictionaries where a value is stored inside of a dictionary and also accessed from within the dictionary. Also, this verison is much more cleaner more clear to undsertand. 
"""

  def __init__(self):
    self._cInventory = BSTDict()

  def load_data(self, file_name):
    """Opens and reads from the csv data file and creates country objects. 

    """

    with open (file_name, "r") as csvfile:
      csvreader = csv.reader(csvfile)
      next(csvreader)
      for lines in csvreader:
        country = Country()

        country._country_name = lines[2]
        country._country_code = lines[3]
        country._population_total = lines[4]
        country._life_expectancy_at_birth = lines[5]
        country._access_to_clean_fuel_and_tech = lines[6]
        country._using_basic_drinking_water = lines[7]
        country._GDP_per_capita = lines[8] = lines[8]
        self._cInventory[country._country_name] = country


  # Written by: Alwin
  # Description: A function to find a specific country object from the database.
  def search_country(self, country_name):
    """Takes in a string and compares to each country object's name from the list of countries. Uses the cInventory to store and access.
    """
    # return whole country object
    if country_name in self._cInventory: 
      return self._cInventory[country_name]
      #Exception handling for this method is added in dict.bstdict.py -> BSTDict class -> _find() method.
    return None

  # Elyas
  #returns selected series for a given country
  def series_for_given_country(self, inp, strg_country):
    """Takes in input from user (this input will determine what series the function will be accessing from the country object.) 
    The search_country function will be called to process in strg_country from the user, a country name. If a object returns, a formatted string with the country name and series accessed with the corresponding data will be returned. 
    This one is just a shorter and more effient way to write the method compared to the previous one in CountryIRSystem.
    """

    obj_country = self.search_country(strg_country)

    if inp == "1":
      data = obj_country._population_total

    elif inp == "2":
      data = obj_country._life_expectancy_at_birth

    elif inp == "3":
      data = obj_country._access_to_clean_fuel_and_tech

    elif inp == "4":
      data = obj_country._using_basic_drinking_water

    elif inp == "5":
      data = obj_country._GDP_per_capita

    return data



  # Written by: Elyas
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

  # Written by: Vel
  # Description: A function to find the minimum value for a given input.
  # Edited by: Alwin 07/19/2024
    # Fixed a problem in converting min_dict[inp] to a float.
      # I had to skip the first entry in the values[] list as it was empty. Hence "values[i+1]" is used in this code.
  def find_min(self, inp):
    values = self._cInventory.values() 

    min = 10000000000
    name = values[0]._country_name
    i = 0
    while i < (len(values) - 1):
      min_dict = { 1: values[i+1]._population_total, 
                   2: values[i+1]._life_expectancy_at_birth, 
                   3: values[i+1]._access_to_clean_fuel_and_tech, 
                   4: values[i+1]._using_basic_drinking_water,
                   5: values[i+1]._GDP_per_capita }

      if float(min_dict[inp]) < float(min):
          min = min_dict[inp]
          name = values[i+1]._country_name
      i += 1
    return name + " " + min
    
  # Written by: Vel
  # given an input coded for a specific indicator, the output will be the
  # largest data record for that indicator
  # Edited by: Alwin 07/19/2024
    # Fixed a problem in converting max_dict[inp] to a float.
      # I had to skip the first entry in the "values[]" list as it was empty. Hence "values[i+1]" is used in this code.
  def find_max(self, inp):
    values = self._cInventory.values() 

    max = 0.0
    name = values[0]._country_name
    i = 0
    while i < (len(values) - 1):
      max_dict = { 1: values[i+1]._population_total, 
                   2: values[i+1]._life_expectancy_at_birth, 
                   3: values[i+1]._access_to_clean_fuel_and_tech, 
                   4: values[i+1]._using_basic_drinking_water,
                   5: values[i+1]._GDP_per_capita }

      if float(max_dict[inp]) > float(max):
          max = max_dict[inp]
          name = values[i+1]._country_name
      i += 1
    return name + " " + max

  def printDict(self):
    #FIXME: None type printed at end of function.
     self._cInventory.print_tree()
