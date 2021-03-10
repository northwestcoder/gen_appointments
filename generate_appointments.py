import time
import buildcsvfiles


# let's use a low tech timer to see how long the data gen takes
t_start = time.time()

locations = buildcsvfiles.createData()

with open('locations.csv', 'w') as f:
	f.write(locations[0])
	print("finished")

with open('dates.csv', 'w') as f:
	f.write(locations[1])
	print("finished")

with open('times.csv', 'w') as f:
	f.write(locations[2])
	print("finished")

t_end = time.time()
totaltime = t_end-t_start
print(str(totaltime) + " seconds")