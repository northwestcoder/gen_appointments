
GENERATE LOCATIONS, DATES, AND DATE TIMES for appointment scheduling


This script generates three csv files which are then meant to be loaded into a database, and from there used by a web application to allow an unknown quantity of public participants to select a time slot from the pool of available timeslots. We also include a simple database trigger which prevents locking contention or race conditions in one of the tables, "Bookings". E.g. this model solves for vaccine signups, or other public-facing situations where people need to grab time slots.

This is all quite low tech and quite by design. The goal here is to rapidly deploy without the need for complex web layers, react, full duplex traffic, API's and so forth. The primary candidate web app for this data model is [Appsheet](https://www.appsheet.com).

from a command line, run:

`python generate_appointments.py` 

This will generate 

- 55 hospitals (taken from the medicare.gov website), into hospitals.csv
- 2,585 dates for each hospital spanning a few months, into dates.csv
- and 426,525 time slots for each available time for each hospitall, into times.csv

The premise here is to then load up this data into a MySQL database or similar.

We have also provided sql create statements in db.sql file to create these tables, as well as one single trigger in file trigger.sql

If you are running this MySQL database in a cloud environment, you will need to set a super user flag in order to create the trigger:

`log_bin_trust_function_creators = ON`

(more info on how to do that [here](https://cloud.google.com/sql/docs/mysql/flags))

This highly bespoke python example uses pure pythonic string manipulation with no third party libraries; you should be able to use any version of python, even the 2.6 version baked into macOS! :)

There are "input files" in the input directory driving the csv generation, as follows:

*input/hospitals.csv*

A selection of hospitals and some of their columns/fields from medicare.gov data - all we are interested in is Name and Address. There's more you could do here of course. In our data model we end up with these fields: "Key","Name","Description","Image","Address","LatLong". The premise here is to come up with your own list of facilities and update this csv file accordingly.

*input/dates.csv*

A simple list of dates. These are the dates you want to make available to your audience. In our data model we end up with these fields: "Key","Location","Name". Name is the string representation of the date and Location is a foreign key reference to locations.csv. The premise here is that you will pick your own range of dates and then update this csv file accordingly.

*input/times.csv*

A simple list of times in military format. When you run this script, we generate 15 timeslots for each time listed in input/times.csv and in our output times.csv file the data will look like:

<pre>
"Key","Date","Name","Times"
"rgwhkg4jqmt440od","rs51fab4khga41gi","Slot 1","08:00:00"
"rkwz02rbqi02i7nk","rs51fab4khga41gi","Slot 2","08:00:00"
"8npy4z9sdelyb3r5","rs51fab4khga41gi","Slot 3","08:00:00"
...
"frjh5qawz492smsb","rs51fab4khga41gi","Slot 14","08:00:00"
"5jy35ohkt8hq97ac","rs51fab4khga41gi","Slot 15","08:00:00"
"4pgpp0am52tg7wvo","rs51fab4khga41gi","Slot 1","08:30:00"
"jsnptduedakti4dl","rs51fab4khga41gi","Slot 2","08:30:00"
...
"2wvc3w3551jhdq6v","rs51fab4khga41gi","Slot 14","08:30:00"
"uhayafyqrf5a8jmo","rs51fab4khga41gi","Slot 15","08:30:00"
"n9bvkgggjxo7hhzb","rs51fab4khga41gi","Slot 1","09:00:00"
"31pcnyb1q9z0fiaz","rs51fab4khga41gi","Slot 3","09:00:00"
...
"vs4u1v5swy13oov4","rs51fab4khga41gi","Slot 14","09:00:00"
"3nl701m3bkvjmr02","rs51fab4khga41gi","Slot 15","09:00:00"
</pre>

etc. The Date field here is a foreign key reference to our dates table. if you want to change the number of slots per time, change the variable called **HOWMANYSLOTSPERTIME** in buildcsvfiles.py. The general premise here is that you will create a list of the "times of day where this script will then generate NN slots for each of those times".

___

If you get this all working, now you can copy this [Sample Appsheet App](https://www.appsheet.com/samples/empty-template-meant-to-be-copied-per-the-instructions?appGuidString=3c165865-b012-4cf5-bbda-83ab62646c0f) and then change the table connections to point to your MySQL tables. Everything should work on this step with basically only one important change to the app:

- We have a single view **available_times** inside of the view.sql file. 
- This view needs to be run and created on your database.
- Then, in appsheet, when it comes time to replace the google sheet connections with your new table connections, for the Appsheet data source called "Datetime" you need to choose this view, as opposed to the table underneath it.
- This makes it so that the end users will only receive from Appsheet *available* time slots, as opposed to all of them.