# -*- coding: utf-8 -*- 
import csv
import datetime
import time
import json
filename='E:/个人课程资料/网页设计/by/by_student_consume_record.csv'
filename2='E:/个人课程资料/网页设计/by/消费信息.json'
data=[{'name':'不大于5元','value':0},{'name':'5.1~10.0元','value':0},{'name':'10.1~15.0元','value':0},{'name':'15.1~20.0元','value':0},{'name':'20.1~30.0元','value':0},{'name':'30元以上','value':0}]
with open(filename,'r', encoding="utf-8") as f:
	with open(filename2,'w', encoding="utf-8") as f2:
		reader=csv.reader(f,delimiter='\t')
		# writer=csv.writer(f2,delimiter='\t')
		for row in reader:
			print(reader.line_num,row)
			if len(row)==5 and row[4]=='餐费支出':
				if float(row[3])<=5.0:
					data[0]['value']=data[0]['value']+1
				elif float(row[3])<=10.0 and float(row[3])>5.0:
					data[1]['value']=data[1]['value']+1
				elif float(row[3])<=15.0 and float(row[3])>10.0:
					data[2]['value']=data[2]['value']+1
				elif float(row[3])<=20.0 and float(row[3])>15.0:
					data[3]['value']=data[3]['value']+1
				elif float(row[3])<=30.0 and float(row[3])>20.0:
					data[4]['value']=data[4]['value']+1
				else :
					data[5]['value']=data[5]['value']+1	
		print(data)
		json.dump(data,f2)


