import csv
import sys
import os
import glob
# we are referencing the opening of the CSV as col, like America Online, CSV Online
fname = './/csv-expo//R-SH1-R-BD-5.csv'
# fname = "C:/Users/nicholai/code/sheets2csv/csv-expo/*.csv"
#for filename in glob.glob(fname):
	#with open (filename, 'r') as f:
		#for line in f:
#col = open(fname)
myoutputthing = open('output.csv','w')
#This appears to be a function which reads the csv itself.
f_part = fname.split('-')
f_part[1]
col = open(fname)
thecsv = csv.reader(col)
i=0
columns1=[]
for cur_line in thecsv:
  i+=1
  if i>2:
#	print cur_line
	if cur_line[0].strip() != '':
		col1= cur_line[0].split('-')
		if col1[1] in ['T1','TH1','TH2']:
#			print col1,cur_line[6],cur_line[8]
			secparcol1 = cur_line[0].split('-')
			separcoldd1 = secparcol1[1]
			separcol2 = fname.split('-')
			
			secparcoldd2 = separcol2[3]
			expo = 'expo//'
			secparcolddss2 = f_part[1].replace(expo,'')
			
			separcoldd3 = secparcol1[3]
			secparcoldd8 = separcol2[1]

			# print separcoldd1 + '-' + secparcolddss2 + '-' + separcoldd3 + '-' + f_part[3] + '-' + cur_line[8] + '-' + cur_line[6];
			columns1 = separcoldd1, secparcolddss2, separcoldd3, f_part[3],cur_line[8], cur_line[6]
			#with myoutputthing:
			writer = csv.writer(myoutputthing)#, delimiter=' ')
			writer.writerows([columns1])

	