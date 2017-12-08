import os
import csv

reader = csv.reader(open('output.csv'))

anar = {}
for rowie in reader:
	key = rowie[0]
	if key in result:
		pass
	result[key] = rowie[1:]
print result