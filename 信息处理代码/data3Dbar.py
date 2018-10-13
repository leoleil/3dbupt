# -*- coding: utf-8 -*- 
import csv
import datetime
import time
import json
filename='E:/个人课程资料/网页设计/by/by_student_network_record.csv'
filename2='E:/个人课程资料/网页设计/by/net.json'
dataSet=[]
data=[]
count=(datetime.datetime(2018, 1,1)-datetime.datetime(2017, 1,1)).days*24
countList=[0]*count
print('count is:',count)
print('countList is:',countList)

with open(filename,'r',encoding="utf-8") as f:
	with open(filename2,'w', encoding="utf-8") as f2:
		reader=csv.reader(f,delimiter='\t')
		# writer=csv.writer(f2,delimiter='\t')
		for row in reader:
			# print(reader.line_num,row)
			if len(row)==7 and time.strptime(row[1],'%Y-%m-%d %H:%M:%S')>=time.strptime('2017-01-01 00:00:00','%Y-%m-%d %H:%M:%S') and time.strptime(row[2],'%Y-%m-%d %H:%M:%S')<time.strptime('2018-01-1 00:00:00','%Y-%m-%d %H:%M:%S'):
				myrow=[row[1],row[2]]
				dataSet.append(myrow)
				print(reader.line_num,myrow)
		for row_1 in dataSet:

			date1=time.mktime(time.strptime(row_1[0],'%Y-%m-%d %H:%M:%S'))   
			date2=time.mktime(time.strptime(row_1[1],'%Y-%m-%d %H:%M:%S'))   
			date3=time.mktime(time.strptime('2017-1-1 00:00:00','%Y-%m-%d %H:%M:%S'))   
			indexMin=int((date1-date3)/60/60)
			indexMax=int((date2-date3)/60/60)
			while indexMin<=indexMax:
				countList[indexMin]=countList[indexMin]+1
				indexMin=indexMin+1
		print('countList is:',countList)
		num=0
		for row_2 in countList:
			item=[num%24,num//24,row_2]
			data.append(item)
			num=num+1
			# #print(reader.line_num,row)
			# if row[4]=='淋浴支出' and time.strptime(row[1],'%Y-%m-%d')>=time.strptime('2017-01-01','%Y-%m-%d') and time.strptime(row[1],'%Y-%m-%d')<time.strptime('2018-01-01','%Y-%m-%d'):
			# 	print(reader.line_num,row)
			# 	myrow= [row[1],row[2]]
			# 	writer.writerow(myrow)
		print(data)
		json.dump(data,f2)


