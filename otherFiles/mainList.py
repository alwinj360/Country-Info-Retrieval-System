# Written by: Vel Perez-Barba
# Edited by: Alwin Alwin Joseph
from country import Country
from irsystems.countryIRSystemList import *


def main():
  
  irsystem = CountryIRSystemList()
  irsystem.load_data("datafiles/country_data.csv")

  exit = False

  # while loop keeps the program running so the user can ask multiple queries until they want to exit the program.
  while exit == False:
    user_input = input("\n\nPlease enter a number to select: \n 00: Exit Program \n 1: Print Data for a given country \n 2: See indicators\n\n ")
    if user_input == '00':
      exit = True
      print("Exiting program")
    if user_input == '1':
      string_c = input("Please enter a country name: ")
      print(irsystem.all_data_for_country(string_c))
    if user_input == '2':
      print("\nPlease select the number of your chosen development indicator (or chosen series)")
      print(" 1: Population total")
      print(" 2: Life expectancy at birth (years)")
      print(" 3: Access to clean fuels and technologies for cooking (% of population)")
      print(" 4: People using at least basic drinking water services (% of population)")
      print(" 5: GDP per capita (current US$)")

      seriesDict = {'1': 'Population Total', '2': 'Life expectancy at birth (years)', '3': 'Access to clean fuels and technologies for cooking (% of population', '4': 'People using at least basic drinking water services (% of population)', '5': 'GDP per capita (current US$)'}
      inp = input("\n ")
  
      print("\nPlease select the number of the query method for your series")
      print(" 1: Print the series data for a specific country")
      print(" 2: Print a list of all countries for this indicator")
      print(" 3: Find minimum and maximum data points of this indicator")
  
      user_method_call = input("\n ")
      if user_method_call == '1':
        strg_c = input("\nPlease enter a country name: \n ")
        
        print("\n" + irsystem.series_for_given_country(inp,strg_c))
      if user_method_call == '2':
        #prints the name of the chosen indicator first.
        print("\n" + seriesDict[str(inp)] + "\n--------------------------------")
        list_countries = irsystem.given_series_for_all_countries(inp)
        for item in list_countries:
          print(item + "\n")
      if user_method_call == '3':
        #prints the name of the chosen indicator first.
        print("\n" + seriesDict[str(inp)])
        print(irsystem.min_and_max(inp))

    # A line is printed at the end of one iteration of the program.
    print("\n -------------------------------------------------------------")
  
if __name__ == "__main__":
  main()
