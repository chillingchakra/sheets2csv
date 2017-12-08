import csv
import sys
import os
import glob
# we are referencing the opening of the CSV as col, like America Online, CSV Online
fname = glob.glob('.//csv-expo//*.csv')

str1 = ' '.join(fname)
# fname = "C:/Users/nicholai/code/sheets2csv/csv-expo/*.csv"
#for filename in glob.glob(fname):
	#with open (filename, 'r') as f:
		#for line in f:
f_part = str1.split('-')
#col = open(fname)
outputty = open('output.csv','w')
#This appears to be a function which reads the csv itself.

f_part[1]
colu = open(str1)
thecsv = csv.reader(colu)
indexi=0
colusOne=[]
for curr_l in thecsv:
  indexi+=1
  if indexi>2:
#	print cur_line
	if curr_l[0].strip() != '':
		colusOne= curr_l[0].split('-')
		if colusOne[1] in ['T1','TH1','TH2']:
#			print col1,cur_line[6],cur_line[8]
			perseco = curr_l[0].split('-')
			pabst = perseco[1]
			kettle = fname.split('-')
			
			kahlua = kettle[3]
			expo = 'expo//'
			expokilla = f_part[1].replace(expo,'')
			
			korbel = perseco[3]
			greygoo = kettle[1]

			# print pabst + '-' + expokilla + '-' + korbel + '-' + f_part[3] + '-' + cur_line[8] + '-' + cur_line[6];
			colusOne = pabst, expokilla, korbel, f_part[3],curr_l[8], curr_l[6]
			#with myoutputthing:
			writer = csv.writer(outputty)#, delimiter=' ')
			writer.writerows([colusOne])

	