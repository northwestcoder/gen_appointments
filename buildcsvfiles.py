import locations

quote				= "\""
quotecomma			= "\","
comma				= ","
newline				= "\n"
space				= " "


HOWMANYSLOTSPERTIME = 15


def createData() -> str:

	listofnewlocations = ""
	listofnewdates = ""
	listofnewtimes = ""


	for idx, item in enumerate(locations.CoreLocationDataColumns):
		listofnewlocations += quote + item + quote
		if idx+1 != len(locations.CoreLocationDataColumns):
			listofnewlocations += comma
	listofnewlocations += newline

	listofnewdates += quote + 'Key' + quotecomma + quote + 'Location' + quotecomma + quote + 'Name' + quote + newline
	listofnewtimes += quote + 'Key' + quotecomma + quote + 'Date' + quotecomma + quote + 'Name' + quotecomma + quote + 'Times' + quote + newline

	# start of main iter
	rowcount = 0
	for newrow in range(len(locations.df_hospitals)):
		newrow = ""
		hospital_bundle = locations.df_hospitals[rowcount].split(',')
		newlocationid = locations.handlerMap("Key")

		# 1 the ID
		newrow+= quote + newlocationid + quotecomma								
		# 2 the identity info
		newrow+= quote + hospital_bundle[0] + quotecomma
		newrow+= quote + 'Description Goes Here ' + newlocationid + quotecomma
		newrow+= quote + 'https://cloud.google.com/_static/cloud/images/social-icon-google-cloud-1200-630.png' + quotecomma
		
		# 3 the geo info
		newrow+= quote + hospital_bundle[1] + comma + hospital_bundle[2] + comma + hospital_bundle[3] + space + hospital_bundle[4] + quotecomma

		#5 lat long, leaving empty for now

		newrow+= quote + quote 
			
		#5 newline if not last line
		if rowcount != len(locations.df_hospitals):														
			newrow+= newline
		
		listofnewlocations += newrow

		#now we populate dates and times based upon each location

		for item in range(len(locations.df_dates)):
			daterowcount = 0 
			newdatekey = locations.handlerMap("Key")
			listofnewdates += quote + newdatekey + quotecomma + quote + newlocationid + quotecomma + quote + locations.df_dates[item].strip('\n') + quote + newline
			for item in range(len(locations.df_times)):
				timerowcount = 0
				for timeitem in range(HOWMANYSLOTSPERTIME):
					newtimekey = locations.handlerMap("Key")			
					listofnewtimes += quote + newtimekey + quotecomma + quote + newdatekey + quotecomma + quote + 'Slot ' + str(timeitem + 1) + quotecomma + quote + locations.df_times[item].strip('\n') + quote + newline

		rowcount+=1

	return listofnewlocations, listofnewdates, listofnewtimes


# uncomment to test:
#test = createData(True, 10, True, 2)
#print(test)
#print(test[1])
