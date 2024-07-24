# Authors: Elyas Ehsan
#          Vel Perez_Barba
#          Alwin Alwin Joseph

from otherFiles.country import Country
import csv


class CountryIRSystemList:
  """
  A class representing the Informational Retrieval System for countries

  ...

  Attributes
  -----------
  countries: list
      a list of Country objects


  Methods
  --------
  
  load_data(self, file_name)
      Opens the data csv file holding all the countries information 
      and reads data into a list of country objects

  search_country(self, country_name)
    passes through each object in the list of country objects and 
    compares the user's input to each object's country name variable, 
    if it matches, it returns the corresponding object. Note, this 
    method is case-sensitive.

  series_for_given_country(self, inp, strg_country)
    Takes in input from user (this input will determine what series 
    the function will be accessing from the country object.) The 
    search_country function will be called to take in secondary input 
    from the user, a country name. a formatted string with the country 
    name and series accessed with the corresponding data will be returned.

  given_series_for_all_countries(self, inp)
    Creates an new empty string list.
    Function loops through list of country objects.
    Given the user input, it accesses the given series in country object.
    The corresponding string is chosen and appended to country list.
    The string list is returned.

  min_and_max(self, inp)
    Determines the indicator the user wants, access corresponding indicator 
    from each class object from country obj list. In a loop, finds the max 
    and minimum data point. The max value and min value are formatted and returned 
    to as a string.

  all_data_for_country(self)
    This method asks for input of country, passes input to search_country and
    returns object the is returned from that method.
  
  """

  def __init__(self):
    self._countries = []  # creating a list of countries

  # Written by: Alwin and Vel
  def load_data(self, file_name):
    """ Reads from the data file, creates the country objects, read each 
    country's information, and store them in the countries list
    
    Parameters
    ----------
    file_name: str
        The name of the file holding the data
    """
    with open(file_name, "r") as csvfile:
      csvreader = csv.reader(csvfile)
      for lines in csvreader:
        country = Country()

        country._country_name = lines[2]
        country._country_code = lines[3]
        country._population_total = lines[4]
        country._life_expectancy_at_birth = lines[5]
        country._access_to_clean_fuel_and_tech = lines[6]
        country._using_basic_drinking_water = lines[7]
        country._GDP_per_capita = lines[8] = lines[8]
        self._countries.append(country)
          
  #Written by: Alwin and Vel
  #This method is case-sensitive
  def search_country(self, country_name):
    """ Takes in a string and compares to each country object's name 
     from list of countries. If matched, said country object is returned.
     Else, none is returned.
    
     Parameters
    ----------
    country_name: str
      country name string literal
    """
    for country in self._countries:
      if country._country_name == country_name:
        return country
      #add Exception handling
    return None  
  
  # Written by: Elyas
  def series_for_given_country(self, inp, strg_country):
    """ Takes in input from user (this input will determine what series the 
    function will be accessing from the country object.) The search_country 
    function will be called to process in strg_country from the user, a country 
    name. If a object returns, a formatted string with the country name and
    series accessed with the corresponding data will be returned.

     Parameters
    ----------
    inp: str
        series selection number
    strg_country: str
        string literal of a country name
    """
    obj_country = self.search_country(strg_country)


    if inp == "1":
      data = obj_country._population_total
      #format
      return str(obj_country._country_name) + "\n Total population: " + str(data)
    
    if inp == "2":
      data = obj_country._life_expectancy_at_birth
      #format
      return str(obj_country._country_name) + "\n Life expectancy at birth, total (years): " + str(data)
    
    if inp == "3":
      data = obj_country._access_to_clean_fuel_and_tech
      #format
      return str(obj_country._country_name) + "\n Access to clean fuels and technologies for cooking (% of population): " + str(data)
    
    if inp == "4":
      data = obj_country._using_basic_drinking_water
      #format
      return str(obj_country._country_name) + "\n People using at least basic drinking water services (% of population): " + str(data)
    
    if inp == "5":
      data = obj_country._GDP_per_capita
      #format
      return str(obj_country._country_name) + "\n GDP per capita (Current US $): " + str(data)
      
  #5 Written by: Alwin
  def given_series_for_all_countries(self, inp):
      """Creates an new empty string list.
       Function loops through list of country objects.
       Given the user input, it accesses the given series in country object.
       The corresponding string is chosen and appended to country list.
       The string list is returned.

      Parameters
      --------------
        inp: str
          user input/number flagging for certain indicator
      """
      outList = []
      # Appending the selected series data into the output list.
      for country in self._countries:
        if inp == "1":
          seriesData = country._country_name + "\n \t\t" + country._population_total
          outList.append(seriesData)
        if inp == "2":
          seriesData = country._country_name + "\n \t\t" + country._life_expectancy_at_birth
          outList.append(seriesData)
        if inp == "3":
          seriesData = country._country_name + "\n \t\t" + country._access_to_clean_fuel_and_tech
          outList.append(seriesData)
        if inp == "4":
          seriesData = country._country_name + "\n \t\t" + country._using_basic_drinking_water
          outList.append(seriesData)
        if inp == "5":
          seriesData = country._country_name + "\n \t\t" + country._GDP_per_capita
          outList.append(seriesData)

      return outList

  # Written by: Vel
  def min_and_max(self, inp):
    """ Determines the indicator the user wants, access corresponding indicator 
     from each class object from country obj list. In a loop, finds the max
     and minimum data point. The max value and min value are formatted and 
     returned to as a string.
    
    Parameters
    -------------
    inp: str
      user input/number flagging for certain indicator
    
    """
    max_country_name = ""
    max = 0.0
    min_country_name = ""
    min = 0.0
    
    if inp == '1':
      min = self._countries[0]._population_total
      for country in self._countries:
        if int(country._population_total) < int(min):
          min_country_name = country._country_name
          min =  country._population_total
        if int(country._population_total) > int(max):
          max_country_name = country._country_name
          max = country._population_total
      
    if inp == '2':
        min = self._countries[0]._life_expectancy_at_birth
        for country in self._countries:
          if float(country._life_expectancy_at_birth) < float(min):
            min_country_name = country._country_name
            min = country._life_expectancy_at_birth
          if float(country._life_expectancy_at_birth) > float(max):
            max_country_name = country._country_name
            max = country._life_expectancy_at_birth
          
    if inp == '3':
      min = self._countries[0]._access_to_clean_fuel_and_tech
      for country in self._countries:
        if float(country._access_to_clean_fuel_and_tech) < float(min):
          min_country_name = country._country_name
          min = country._access_to_clean_fuel_and_tech
        if float(country._access_to_clean_fuel_and_tech) > float(max):
          max_country_name = country._country_name
          max = country._access_to_clean_fuel_and_tech
          
    if inp == '4':
      min = self._countries[0]._using_basic_drinking_water
      for country in self._countries:
        if float(country._using_basic_drinking_water) < float(min):
          min_country_name = country._country_name
          min = country._using_basic_drinking_water
        if float(country._using_basic_drinking_water) > float(max):
          max_country_name = country._country_name
          max = country._using_basic_drinking_water
          
    if inp == '5':
      min = self._countries[0]._GDP_per_capita
      for country in self._countries:
        if float(country._GDP_per_capita) < float(min):
          min_country_name = country._country_name
          min = country._GDP_per_capita
        if float(country._GDP_per_capita) > float(max):
          max_country_name = country._country_name
          max = country._GDP_per_capita
        
    return "\nMinimum: {} - {} \nMaximum: {} - {}".format(min_country_name, min, max_country_name, max)
      
  # Written by: Elyas
  def all_data_for_country(self, string_c):
    """This method accepts country name string. It passes input to search_country. It stores the returned object.
    """
    return self.search_country(string_c) 
    
  #Written by: Vel
  def __str__(self):
    """ This method is used for formatting. It is called in the country.py every time we have something in the object for example obj_c
    """
    countryIRSystem = ""
    for country in self._countries:
      countryIRSystem = countryIRSystem + str(country)

    return countryIRSystem

# no print or input() code lines in the CountryIRSystem.py file. All of the printing and asking for input should happen in the main.py file.
