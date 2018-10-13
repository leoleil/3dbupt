# -*- coding: utf-8 -*- 
import csv
import datetime
import time
import json
filename='E:/个人课程资料/网页设计/by/by_student_info.csv'
filename2='E:/个人课程资料/网页设计/by/学院人数.json'
mylist={'信息与通信工程学院':0,'计算机学院':0,'理学院':0,'经济管理学院':0,'数字媒体与设计艺术学院':0,'软件学院':0,'现代邮政学院':0,'国际学院':0,'电子工程学院':0,'人文学院':0,'自动化学院':0,'网络空间安全学院':0,'光电信息学院':0}
data=[]
with open(filename,'r',encoding="utf-8") as f:
	with open(filename2,'w', encoding="utf-8") as f2:
		reader=csv.reader(f,delimiter='\t')
		# writer=csv.writer(f2,delimiter='\t')
		for row in reader:
			#print(reader.line_num,row)
			if row[2]=='2017' and len(row)==5:
				# print(row[3])
				mylist.setdefault(row[3], 0)
				mylist[row[3]]=mylist[row[3]]+1
		print(mylist)
		for i in mylist:
			item={'name':i,'value':mylist[i]}
			data.append(item)
			# if len(row)==7 and time.strptime(row[1],'%Y-%m-%d %H:%M:%S')>=time.strptime('2017-09-01 00:00:00','%Y-%m-%d %H:%M:%S') and time.strptime(row[2],'%Y-%m-%d %H:%M:%S')<time.strptime('2017-09-30 00:00:00','%Y-%m-%d %H:%M:%S'):
			# 	myrow=[row[1],row[2]]
			# 	data.append(myrow)
			# 	print(reader.line_num,myrow)
			# #print(reader.line_num,row)
			# if row[4]=='淋浴支出' and time.strptime(row[1],'%Y-%m-%d')>=time.strptime('2017-01-01','%Y-%m-%d') and time.strptime(row[1],'%Y-%m-%d')<time.strptime('2018-01-01','%Y-%m-%d'):
			# 	print(reader.line_num,row)
			# 	myrow= [row[1],row[2]]
			# 	writer.writerow(myrow)
		print(data)
		json.dump(data,f2)


