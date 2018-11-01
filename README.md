
Uses sqlalchemy to analyze the data in a sqlite datafile.

The data is precipitation and temperature data for 9 observation stations in Hawaii.

Analysis is done on the last 12 months of data and on the activity level of the stations with a histogram of the temperatures for the most active station. Dates were chosen for a trip(1-7-2018 to 1-21-2018) with analysis done on the previous years temperature data to determine expected temps, and expected rainfall for the trip. Further analysis was done to graph the temperature range (min, average, max) expected for the trip as a whole and for each trip date. 

Part 2 includes developing an api to provide precipitation and temperature data through 6 endpoints using flask, sqlalchemy and sqlite.
