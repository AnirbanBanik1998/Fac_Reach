import requests
from bs4 import BeautifulSoup
from xlwt import Workbook
import os
wb=Workbook()
sheet1=wb.add_sheet("Sheet 1")

headers = {
	    'User-Agent': 'FacultyScraper 1.0'
	    }
source_code=requests.get("http://www.srmuniv.ac.in/department-of-electrical-and-electronics-engineering/faculty", headers=headers)
text=source_code.text
soup=BeautifulSoup(text)
arr={}
i=0
j=1
k=1
sheet1.col(0).width=10000
sheet1.col(1).width=10000
for link in soup.findAll('tr'):
	soup1=BeautifulSoup(str(link))
	for l in soup1.findAll('td'):
		soup2=BeautifulSoup(str(l))
		for a in soup2.findAll('a'):
			title1=a.string
			if str(title1)!="None":
				arr[i]=str(title1).strip()
				i=i+1
		title2=l.string
		if str(title2)!="None":
			arr[i]=str(title2).strip()
			i=i+1

for i in range(0,len(arr)):
	if i%2==0:
		sheet1.write(j, 1, arr[i])
		j=j+1
	else:
		sheet1.write(k, 0, arr[i])
		k=k+1
wb.save('Faculty.xls')
