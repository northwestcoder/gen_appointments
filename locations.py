import random
import datetime
import time
import string
import os

# this file does a few things 
# 1. creates a geolocation bundle, 
# 2. load a bunch of input/seed data into memory
# 3. load some handlers into a handler map

for filename in os.listdir("inputs"):
	#first, if we want current dates, regen this file prior to loading into memory
	if filename.endswith(".csv") or filename.endswith(".txt"): 
		arrayname = os.path.join(filename[:-4])
		globals()["df_"+arrayname] = 0
		with open("inputs/" + filename, "r") as file:
			globals()["df_"+arrayname] = file.readlines()
			file.close()
	else:
		continue


CoreLocationDataColumns = [
'Key',
'Name',
'Description',
'Image',
'Address',
'LatLong'
]


handlers = {
"Key" : "nextRandomID",
"geolocation_bundle" : "coreGeolocationBundle",
"hospital_selector" : "coreHospitalBundle"
		}


# generates a 16 char random key
def nextRandomID(size=16, chars=string.ascii_lowercase + string.digits):
	uniqueid = ''.join(random.choice(chars) for _ in range(size))
	return uniqueid




#  generates an geolocation bundle, defined as: "address, city, state, postalcode"
def coreGeolocationBundle():
	geolocation = []
	geolocation.append( str(random.randint(100,9999)) + " " + random.choice(df_streetnames))
	citystatecombo = random.choice(df_city_county_state).split(',')
	geolocation.append(citystatecombo[0])
	geolocation.append(citystatecombo[1])
	geolocation.append(citystatecombo[2])
	geolocation.append(random.choice(df_postalcodes))
	return geolocation

def coreHospitalBundle():
	hospitalinfo = ""
	randomhospital = random.choice(df_hospitals).split(',')
	hospitalinfo += randomhospital[1] + ", " + randomhospital[2] + ", " + randomhospital[3] + " " + randomhospital[4]
	return hospitalinfo

def handlerMap(type):
	return globals()[handlers.get(type)]()



