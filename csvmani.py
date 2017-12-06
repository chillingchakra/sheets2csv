import csv
import sys

#we are referencing the opening of the CSV as col, like America Online, CSV Online
col = open('.//csv-expo//R-SH1-R-BD-5.csv')

#This appears to be a function which reads the csv itself.
thecsv = csv.reader(col)

#For every row that you encounter when going thecsv, print row

for quanvarow in thecsv:
#	print row[19]

	quanvar = quanvarow[20]
	old_stdout = sys.stdout
	log_file = open("message.log","w")
	sys.stdout = log_file

	try: 
		#bro = quanvar(".")
		#print quanvar
		quanvar.index('.')

	except ValueError:
		print "All is Well"
		sys.stdout = old_stdout
		log_file.close()
	else:
		print 'There is a decimal point in the last quantity row. Check Excel'

