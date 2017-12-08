import os
import csv
#folders = [".//csv-expo//*.csv"]

path = './/csv-expo//'
outputty = open('output.csv','w')
for fname in os.listdir(path):
    #print  fname
	#This appears to be a function which reads the csv itself.
	colu = open(path+fname)
	f_part = fname.split('-')
	f_part[1]
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