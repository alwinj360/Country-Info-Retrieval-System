from otherFiles.randomfiles import * 
from otherFiles.analysis_methods import *


def countryIRS_BST_test():
  country_irs = countryIRSystemBSTDict()

  print("**testing loading the inventory**")
  country_irs.load_data("rand_file_1.csv")
  print(type(country_irs))
  print("**Testing the inventory is compelete **")

# The following if statement is so that "countryIRSystem_analysis" is not run automatically when this file is imported.
if __name__ == "__main__":
  # The data generation does not work as expected on my computer, hence I generated the data by running the same code in replit.
  # generate_data_csv("temp_rand.csv", 10000)

  # Number of entries in the randomly-generated file.
  no_entries = 100
  # Number of queries to be executed in this analysis.
  no_queries = 100000
  file_name = "dataFiles/rand_"+str(no_entries)+".csv"
  countryIRSystem_analysis(file_name, no_queries, no_entries)

