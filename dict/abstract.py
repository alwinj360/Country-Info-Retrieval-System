# Edited by: Alwin 07/18/2024
  # Explained the purpose of this file.

# This file declares ABCs (Abstract Base Classes) for all classes used in this project.
# The actual classes will inherit this structure. The abstract classes are like a contract. 
# The inheriting classes must implement the abstract methods declared here.
# This helps in keeping the code uniform.

from abc import abstractmethod
from abc import ABC

class CountryIRSystemAbstract(ABC):

  @abstractmethod
  def load_data(self, file_name):
    pass

  @abstractmethod
  def search_country(self, country_name):
    pass

  @abstractmethod
  def series_for_given_country(self, inp, strg_country):
    pass

  @abstractmethod
  def given_series_for_all_countries(self, inp):
    pass

  @abstractmethod
  def find_min(self, inp):
    pass

  @abstractmethod
  def find_max(self,inp):
    pass

# An abstract class representing the blueprint for
# a dictionary 
class DictAbstract(ABC):

  #Return the number of items stored in the dictionary
  @abstractmethod
  def __len__(self):
    pass

  #Implementing the python magic method __contains__
  #This will help to use in true or false sentences
  #e.g., if key is in dict
  @abstractmethod
  def __contains__(self, key):
    pass

  #Implementing the python magic method __getitem__
  #This function will help in using this sytax dict[key]
  @abstractmethod
  def __getitem__(self, key):  
    pass

  #Implements self[key] = value.  If key is already stored in
  #the dictionary then its value is modified.  If key is not in the map,
  #it is added.
  @abstractmethod
  def __setitem__(self, key, value):
    pass

  @abstractmethod
  def values(self):
    pass

