import random
import os
import csv

# Generating random data. The car information is not important, rather the car vin number needs to be unique
def generate_data_csv(rand_file_name, no_entries):
  # rand_file_name: the name of the random 
  # no_entries: the number of entries in the file
  
  file_name = "temp.csv" # temp file to hold the generated entries
  with open(file_name, 'w', encoding='UTF8', newline='') as f:
    writefile = csv.writer(f)
    header = ["Time", "Time Code", "Country Name", "Country Code", 
                  "Population, total", "Life expectancy at birth", 
                  "Access to clean fuels", "Basic drinking water", 
                  "GDP per capita"]
    writefile.writerow(header)
    for i in range(1, no_entries+1):
      time = 2020
      time_code = "YR2020"
      country_name = "India" + str(i)
      country_code = "IND"
      population_total = 1400000000
      life_expectancy = 70
      access_to_clean_fuels = 90
      using_basic_drinking_water = 90
      GDP_per_capita = 15000
      row = [str(time), time_code, country_name, country_code, str(population_total), str(life_expectancy), str(access_to_clean_fuels), str(using_basic_drinking_water), str(GDP_per_capita)]
      writefile.writerow(row)
   
  # randmize the entries in the file
  with open(file_name,'r') as source:
    csvreader = csv.reader(source)
    header = next(csvreader) # Read and save header (skip it)
    data = [ (random.random(), line) for line in csvreader ]
  data.sort()
  with open(rand_file_name,'w', encoding='UTF8', newline='') as target:
    writefile = csv.writer(target)
    writefile.writerow(header)
    for _, line in data:
        writefile.writerow( line )

  # removing the temp file, not needed anymore
  os.remove(file_name)
