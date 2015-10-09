import numpy
import xlrd
from bad_data import *

# this script is for reading data from the 2 files

mlac = xlrd.open_workbook('MsiaAccidentCases.xlsx')
osha = xlrd.open_workbook("osha.xlsx")
oshasheet = osha.sheets()[0]
mlsheet = mlac.sheets()[0]

def get_data(sheet):
	data = [extract_row(sheet.row(n)) for n in range(sheet.nrows)]
	return data

def count_error(sheet):
	# unfinished
	data = get_data(sheet)
	return data 

def extract_row(row):
	result = []
	for i in row:
		# i is Cell object
		result.append(str(i).strip("text:u").strip("'").strip())
	return result	

mldata = get_data(mlsheet)
osdata = get_data(oshasheet)
print len(mldata)
print len(osdata)
