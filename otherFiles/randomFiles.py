import random
import os
import csv


def generate_data(rand_file_name, no_entries):
  # rand_file_name: the name of the random 
  # no_entries: the number of entries in the file
  
  file_name = "temp.txt" # temp file to hold the generated entries
  with open(file_name, 'w') as writefile:
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
      writefile.write(str(time) + " " + time_code + " " + country_name + " " + country_code + " " + str(population_total) + " " + str(life_expectancy) + " " + str(access_to_clean_fuels) + " " + str(using_basic_drinking_water) + " " + str(GDP_per_capita) + "\n")


  # randmize the entries in the file
  with open(file_name,'r') as source:
    data = [ (random.random(), line) for line in source ]
  data.sort()
  with open(rand_file_name,'w') as target:
    for _, line in data:
        target.write( line )

  # removing the temp file, not needed anymore
  os.remove(file_name)


# Generating random data. The car information is not important, rather the car vin number needs to be unique
def generate_data_csv(rand_file_name, no_entries):
  # rand_file_name: the name of the random 
  # no_entries: the number of entries in the file
  
  file_name = "temp.csv" # temp file to hold the generated entries
  with open(file_name, 'w', encoding='UTF8') as f:
    writefile = csv.writer(f)
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
    data = [ (random.random(), line) for line in csvreader ]
  data.sort()
  with open(rand_file_name,'w') as target:
    writefile = csv.writer(target)
    for _, line in data:
        writefile.writerow( line )

  # removing the temp file, not needed anymore
  os.remove(file_name)
