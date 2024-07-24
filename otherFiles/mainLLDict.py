from countryIRSystemLLDict import CountryIRSystemLLDict
from dict.lldict import LLDict
from dict.lldict import _LLNode

# Written by: Vel
def main_test_ll():
  print("TESTING LLDict()" + "\n" +
        "*************************")
  #testing LLDict---------------------------
  ll_dict = LLDict()
  #testing __setitem__ or dict[key] = value syntax
  ll_dict["India"] = "IND"
  ll_dict["Mexico"] = "MEX"
  ll_dict["Afghanistan"] = "AFG"
  
  print("Testing __getitem__ or dict[key] syntax:")
  print(ll_dict["InDia"])
  print(ll_dict["mexiCO"])
  print(ll_dict["afghanistan"])
  
  print("\nTesting __len__(): " + str(len(ll_dict)))

  print("\nTESTING CountryIRSystemLLDict()" + "\n" +
        "*************************")
  # Testing CountryIRSystemLLDict---------------------------
  # Creates and loads database of country objects using 
    # linked list dictionary
  country_dict = CountryIRSystemLLDict()
  country_dict.load_data("datafiles/country_data.csv")

  print("Testing search_country:" + "\n----------------" +
        "\nSearching for India...")
  print(country_dict.search_country("india")) # returns all country obj attributes
  print("\nSearching for Jamaica...")
  print(country_dict.search_country("jamaica")) # Jamaica not in database, correctly returns none

  print("\nTesting find_min() for Population & GDPs:" +
        "\n--------------")
  print(country_dict.find_min(1)) # expected min: Uruguay/ '3429086' for population total
  print(country_dict.find_min(5)) # expected min: Afghanistan/ 516.866552182696 for GDP
  print("\nTesting find_max() for Population & GDPs:" +
        "\n--------------")
  print(country_dict.find_max(1)) # expected max: India/ '1396387127' for population total
  print(country_dict.find_max(5)) # expected max: US / 63530.633483909 for GDP
  print('\n')
  
  # testing series function, all countries
  list = country_dict.given_series_for_all_countries('1')
  for i in list:
    print(i) # prints list of population totals
  # testing series function, one country
  data = country_dict.series_for_given_country('2', "india")
  print('\n' + data) # data expected is india's life expectancy at birth of '70.15'
  
  # country_dict.series_for_given_country('2', "indA") correctly raises KeyError

  print("--Testing Complete--")

if __name__ == "__main__":
  main_test_ll()
