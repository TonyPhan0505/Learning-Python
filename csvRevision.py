import csv
import urllib.request

#read csv file as texts
def readCSV_asTextWithSpaceDeli(filepath):
	with open(filepath,newline = '') as file:
		data = csv.reader(file,delimiter = ' ',quotechar = '|')
		for record in data:
			print(', '.join(record))

#read csv file as dictionary
def readCSV_asDict(filepath):
	with open(filepath,newline='') as file:
		data = csv.DictReader(file)
		for record in data:
			print(record)

#read csv file as Text with a tab delimiter
def readCSV_asTextWithTabDeli(filepath):
	with open(filepath,newline='') as file:
		data = csv.reader(file,delimiter='\t')
		for record in data:
			print(', '.join(record))

#read csv file as list
def readCSV_asList(filepath):
	with open(filepath,newline = '') as file:
		data = csv.reader(file)
		data_list = list(data)
		for record in data_list:		
			print(record)

#read csv file as Text with initial space in front of data piece
def readCSV_withInitialSpace(filepath):
	with open(filepath,newline='') as file:
		data = csv.reader(file,skipinitialspace = False)
		for record in data:
			print(', '.join(record))

#read csv file without initial spaces around the data entry and without quotes around the delimiter
def readCSV_withoutSpaceQuoteDeli(filepath):
	csv.register_dialect('csv_dialect',delimiter='|', quote=csv.QUOTE_ALL)
	with open(filepath,'r') as file:
		data = csv.reader(file,dialect='csv_dialect',skipinitialspaces=True)
		for record in data:
			print(', '.join(record))

#read csv file but only its one particular data field
def readCSV_oneField(filepath,field):
	with open(filepath,newline='') as file:
		data=csv.DictReader(file)
		print(field,':')
		for record in data:
			print(record[field])

#print total no. of rows and available field names
def displayRowsNumandFieldNames(filepath):
	with open(filepath,newline='') as file:
		data = csv.reader(file,delimiter=' ',quotechar=',')
		fields = next(data)
	return data.line_num, ', '.join([field for field in fields])

#write CSV file
def write_dataListInCSV(filepath,data_list):
	with open(filepath,newline='') as file:
		writer = csv.writer(file)
		writer.writerows(data_list)
		
#write Dictionary in a csv file
def write_dataDictInCSV(filepath,fieldnames,dict_data):
	with open(filepath,'w') as file:
		writer = csv.DictWriter(file, fieldnames = fieldnames)
		#writer.writeheader()
		writer.writerow(dict_data)
	
def get_sourcecode(url):
	return urllib.request.urlopen(url).read()

import requests

url = "https://www.google.com"
timeout = 5

