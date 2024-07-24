#Sets, and stores data about the class object Country.
class Country:
  #By: Elyas Ehsan
  #Edited by: Vel Perez-Barba
  def __init__(self):
    self._country_name = " "
    self._country_code = " "
    self._life_expectancy_at_birth = 0.0
    self._access_to_clean_fuel_and_tech = 0.0
    self._using_basic_drinking_water = 0.0
    self._GDP_per_capita = 0.0
    self._population_total = 0

  #By: Elyas Ehsan
  #getter for country name
  @property
  def country_name(self):
    return self._country_name

  #By: Elyas Ehsan
  #Edited by Vel Perez-Barba
  #setter for country name
  @country_name.setter
  def country_name(self, name):
    assert name.isalpha(), "enter characters"
    self._country_name = name

  #By: Elyas Ehsan
  #getter for country Code
  @property
  def country_code(self):
    return self._country_code

  #By: Elyas Ehsan
  #Edited by Vel Perez-Barba
  #setter for country Code
  @country_code.setter
  def country_code(self, code):
    assert code.isalpha(), "enter characters"
    self._country_code = code
  
  #By: Elyas Ehsan
  #getter for indicator 1
  @property
  def life_expectancy_at_birth(self):
    return self._life_expectancy_at_birth
  
  #By: Elyas Ehsan
  #Edited by Vel Perez-Barba
  #setter for indicator 1
  @life_expectancy_at_birth.setter
  def life_expectancy_at_birth(self, total):
    assert (total > 0.0) and (total < 150.0)
    self._life_expectancy_at_birth = total

  #Author: Vel Perez-Barba
  #getter for indicator 2: % of population
  @property
  def access_to_clean_fuel_and_tech(self):
    return self._access_to_clean_fuel_and_tech

  #Author: Vel Perez-Barba
  #setter for indicator 2: % of population
  @access_to_clean_fuel_and_tech.setter
  def access_to_clean_fuel_and_tech(self, access_total):
    assert (access_total >= 0.0) and (access_total <= 100.0)
    self._access_to_clean_fuel_and_tech = access_total

  #Author: Vel Perez-Barba
  #getter for indicator 3: % of population
  @property
  def using_basic_drinking_water(self):
    return self._using_basic_drinking_water

  #Author: Vel Perez-Barba
  #setter for indicator 3: % of population
  @using_basic_drinking_water.setter
  def using_basic_drinking_water(self, data):
    assert (data >= 0.0) and (data <= 100.0), "must be between 0-100"
    self._using_basic_drinking_water = data

  #Author: Alwin Alwin Joseph  
  #getter for indicator 4 : GDP_per_capita
  @property
  def GDP_per_capita(self):    
    return self._GDP_per_capita

  #Author: Alwin Alwin Joseph
  #Edited by Vel Perez-Barba
  #setter for indicator 4 : GDP_per_capita
  @GDP_per_capita.setter
  def GDP_per_capita(self, data):
    assert (data > 0.0) and (data < 100000.0)
    self._GDP_per_capita = data

  #Author: Alwin Alwin Joseph
  #getter for indicator 5 : population
  @property
  def population_total(self):
    return self._population_total

  #Author: Alwin Alwin Joseph
  #Edited by Vel Perez-Barba
  #setter for indicator 5 : population
  @population_total.setter
  def population_total(self, data):
    assert data >= 0, "Please enter a non-negative number"
    self._population_total = data


  #Author: Vel Perez-Barba
  #Editted by: Elyas Ehsan
  #"to string" method for all variables
  
  def __str__(self):
    line = "\nCountry name: " + self.country_name + "\n" + "Code: " + self.country_code + "\n" + "Population total: " + str(self.population_total) + "\n" + "Life expectancy at birth: " + '{0:0.2f}'.format(float(self.life_expectancy_at_birth)) + " (years)" + "\n" + "Fuel/tech access: " + str(self.access_to_clean_fuel_and_tech) + "%" + "\n" + "Basic water usage data: " + '{0:0.2f}'.format(float(self.using_basic_drinking_water)) + "%" + "\n" + "GDP per capita: $" + '{0:0.2f}'.format(float(self._GDP_per_capita))
    return line
    
