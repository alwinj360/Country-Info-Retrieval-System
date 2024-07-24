from irsystems.countryIRSystemBSTDict import *

irsystem = countryIRSystemBSTDict()
irsystem.__init__()
irsystem.load_data("datafiles/country_data.csv")
irsystem.find_min2(1)
