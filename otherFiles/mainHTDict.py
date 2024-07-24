from countryIRSystemHTDict import *
from dict.htdict import HTDict
from country import Country

class htdict_test():
  print("\nTESTING HTDict():")
  print("**************************")
  
  HT = HTDict()
  
  # The values are the expected hashcodes based on _hash()
  HT["United States"] = "hash_13"
  HT["Afghan"] = "hash_6"
  HT["Jordan"] = "hash_6"
  HT["United Arab Emirates"] = "hash_0"
  HT["Philippines"] = "hash_11"
  HT["France"] = "hash_6"

  print("Visualization of hashtable:\n")
  HT.printAll()

  # Testing __len__()
  print("\nRecords in HT: "+ str(len(HT)))
  print(HT["Jordan"])

class countryirsystemhtdict_test():
  print("\nTESTING CountryIRSystemHTDict():")
  print("****************************")
  
  IRS = CountryIRSystemHTDict()
  IRS.load_data("datafiles/country_data.csv")

  print("\nTesting search_country:")
  print("-----------------------")
  print("Searching for Mexico...")
  # Returns the country object for Mexico
  print(IRS.search_country("Mexico"))
  
  print("\nTesting find_min() for Population & GDPs:" 
        + "\n-----------------------")
  # Testing find_min() and find_max()
  print(IRS.find_min(1)) # expected min: Uruguay/ '3429086' for population total
  print(IRS.find_min(5)) # expected min: Afghanistan/ 516.866552182696 for GDP
  
  print("\nTesting find_max() for Population & GDPs:" 
        + "\n-----------------------")
  print(IRS.find_max(1)) # expected max: India/ '1396387127' for population total
  print(IRS.find_max(5)) # expected max: US / 63530.633483909 for GDP

  print("\nTesting series_for_given_country():")
  print("-----------------------")
  # returns GDP per capita data for the country of Jordan
  print(IRS.series_for_given_country("5", "Jordan"))

  print("\n" + "Testing 'given_series_for_all_countries' function" + "\n-----------------------")
  outputList = IRS.given_series_for_all_countries('1')
  print("\nPrinting All Populations\n")
  for item in outputList:
    print(item) # Expected: All population totals

  outputList = IRS.given_series_for_all_countries('5')
  print("\nPrinting All GDPs\n")
  for item in outputList:
    print(item) # Expected: All GDPs

if __name__ == "__main__":
  countryirsystemhtdict_test()
