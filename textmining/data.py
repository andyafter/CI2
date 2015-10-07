import numpy
import xlrd

# this script is for reading data from the 2 files

mlac = xlrd.open_workbook('MsiaAccidentCases.xlsx')
osha = xlrd.open_workbook("osha.xlsx")
sheet = osha.sheets()[0]

print sheet.row(0)  # here is how u read the data
