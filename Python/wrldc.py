import requests
from datetime import datetime, date
from BeautifulSoup import BeautifulSoup
import csv
import sys
from time import sleep
from operator import add
import win32com.client
import os

userDate  =  sys.argv[1]
cons      =  sys.argv[2]
tempDate  =  datetime.strptime(userDate, "%d%m%Y")
dateOne   =  tempDate.strftime("%d-%b-%Y")
tempMonth =  tempDate.strftime("%b")
tempDay   =  tempDate.strftime("%d")
tempYear  =  tempDate.strftime("%Y")

dateTwo = tempDay+"-"+tempMonth.upper()+"-"+tempYear

print "Scraper started"
print "Downloading data for date: " + dateOne

wrldcUrl = "http://www.wrldc.com/test/schperi.asp"

headers  = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36"}

session = requests.Session()
session.headers.update(headers)
sleep(1)
requestWrldc = session.get(wrldcUrl)
#print requestWrldc.headers
print "Requesting url: http://www.wrldc.com/test/schperi.asp"

dataWrldc   = {
	"date_txt": dateOne,
	"htxt": dateTwo,
	"htxt_Month":"1",
	"scl2": cons,
	"scl1": "1",
	"text2" : "2",
	"text3" : ""
}
#sleep(15)
requestWrldcData    = session.post(wrldcUrl , data=dataWrldc, timeout=40)
soupWrldc           = BeautifulSoup(requestWrldcData.content)
#print soupWrldc
print "Getting data!"
tdWrldc = soupWrldc.findAll('td', style="FONT-SIZE: smaller; FONT-VARIANT: small-caps;BACKGROUND-COLOR: peachpuff")
#print len(tdWrldc)
tempValues = []
for i in range(0, len(tdWrldc)):
	tempData =  tdWrldc[i].string.split()
	values = tempData[0].encode("utf8")
	tempValues.append([values])

#print len(tempValues)
#print tempValues
#td = soupWrldc.findAll( "td", {'rowspan' : '2'} )

table4 = soupWrldc.find('table', {'id': 'table4'})
rowTop = table4.findAll("tr")
row = rowTop[0].findAll("td")

tdValues = []
for i in xrange(0, len(row)):
	text = row[i].text.split()
	value = text[0].encode('utf8')
	tdValues.append(value)

#print tdValues
blockIndex = tdValues.index("BLOCK")
totalIndex = tdValues.index("TOTAL")
totals = (i for i,x in enumerate(tdValues) if x == "TOTAL")
totalsIndex = []
for i in totals: totalsIndex.append(i) 
print totalsIndex
stoaIndex  = tdValues.index("STOA(EX_PERI)")
mtoaIndex  = tdValues.index("MTOA(EX_PERI)")
skipBy = totalsIndex[1] - blockIndex

#print tempValues
finalValuesStoa = []
for i in range(stoaIndex, len(tempValues), skipBy+1):
	finalValuesStoa.append(tempValues[i])

#print finalValuesStoa

#finalValuesMtoa = []
#for i in range(mtoaIndex, len(tempValues), skipBy+1):
#        finalValuesMtoa.append(tempValues[i])

#print finalValuesMtoa
#finalTotal = [x + y for x, y in zip(finalValuesStoa, finalValuesMtoa)]
#finalStoaMtoa = map(add, finalValuesStoa, finalValuesMtoa)
finalDat = tempDate.strftime("%d-%m-%Y")
def dateBlocks(date):
	return [date]*96

finalDa = dateBlocks(finalDat)
finalDate = []
for i in finalDa:
	finalDate.append([i])

#print finalDate

#finalVal = map(add, finalDate, finalValuesStoa)

finalValues = map(add, finalDate, finalValuesStoa)

#print finalValues

finalOutput = []
finalOutput.append(["DATE", "STOA"])

for i in finalValues:
	finalOutput.append(i)

#print finalOutput

filePath = "D:\D Drive data\PSPCL\STEP\Exchange Price Projection\All States\SYSTEM\Bilateral"
filename = "STOA_"+cons+"_"+userDate+".csv"
fullPath = filePath + "\\" + filename

with open(fullPath, 'wb') as fp:
    a = csv.writer(fp, delimiter=',')
    data = finalOutput
    a.writerows(data)

print "Data for WRLDC extracted!"

"""
print "Refreshing open_access.xlsx for latest data..."
xl = win32com.client.DispatchEx("Excel.Application")
wb = xl.workbooks.open("C:\\Users\\admin\\Downloads\\open_access.xlsx")
xl.Visible = True
wb.RefreshAll()
sleep(10)
wb.Save()
xl.Quit()
print "Workbook refreshed!"
"""
