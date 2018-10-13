# -*- coding: utf-8 -*- 
import csv
import datetime
import time
import json
import operator
filename='E:/个人课程资料/网页设计/by/by_books_borrow_record.csv'
filename2='E:/个人课程资料/网页设计/by/借书数据.json'
mylist={}
data=[]
with open(filename,'r',encoding="utf-8") as f:
	with open(filename2,'w', encoding="utf-8") as f2:
		reader=csv.reader(f,delimiter='\t')
		# writer=csv.writer(f2,delimiter='\t')
		for row in reader:
			#print(reader.line_num,row)
			if len(row)==4:
				# print(row[3])
				mylist.setdefault(row[1], 0)
				mylist[row[1]]=mylist[row[1]]+1
		# print(sorted(mylist.items(),key=lambda item:item[1],reverse=True))
		# mylist=mylist[0:9]
		# print(mylist)
		for i in mylist:
			if mylist[i]>=9:
				item={'name':i,'value':mylist[i]}
				data.append(item)
		print(data)
		json.dump(data,f2)