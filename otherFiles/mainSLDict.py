from countryIRSystemSLDict import CountryIRSystemSLDict
from dict.sldict import SLDict
from dict.sldict import _Pair

class sldict_test():
  print("\n\n" + "Testing sldict() \n\n")
  Alist = SLDict() # makes a sortedlist 
  
  Alist["China"] = "country"
  print("Printing Alist[\"China\"]: " + Alist["China"])
  # update key with new value
  Alist["China"] = "updated_country"
  print("Printing Alist[\"China\"]: " + Alist["China"])

  Alist["America"] = "country"
  Alist["India"] = "country"
  Alist["Bolivia"] = "country"
  Alist["Denmark"] = "country"

  print("\nPrinting sorted list:\n" + str(Alist))
  print("Testing __len__(): " + str(len(Alist)))


class countryirsystemsldict_test():
  print("\n\n" + "Testing countryirsystemsldict() \n\n")
  countrySystem = CountryIRSystemSLDict() # creates SLDict for country data
  countrySystem.load_data("datafiles/country_data.csv")
  list_1 = countrySystem.given_series_for_all_countries('1') # returns a list of all population totals
  list_2 = countrySystem.given_series_for_all_countries('5') # returns a list of all the GDPs per capita 

  print("All Population Totals \n--------------------------------")
  for i in range(len(list_1)):
    print(list_1[i])

  print("\nAll GDPs \n------------------------------")
  for i in range(len(list_2)):
    print(list_2[i])

  ab = countrySystem.series_for_given_country('3', 'jordan') # returns pop. % that has access to clean cooking fuel and tech in Jordan
  bc = countrySystem.series_for_given_country('4', 'China') #  correctly returns none as china data is not yet available
  print(ab)
  print(bc)
  
  print("\nTesting find_min() for GDPs:" +
        "\n--------------")
  print(countrySystem.find_min(5))
  print("\nTesting find_max() for Population:" +
        "\n--------------")
  print(countrySystem.find_max(1))

if __name__ == "__main__":
  sldict_test()
  countryirsystemsldict_test()
