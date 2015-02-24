import requests
from datetime import datetime, date
from BeautifulSoup import BeautifulSoup
import csv
from operator import add
import sys
from time import sleep

userDate = sys.argv[1]
city     = sys.argv[2]
tempDate = datetime.strptime(userDate, "%d%m%Y")
date     = tempDate.strftime("%d-%m-%Y")
print "Scraper started"
print "Downloading data for date: " + date

nrldcUrl = "http://nrldc.in/WBS/netdrwlsch.aspx"

headers      = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36"}

session = requests.Session()
session.headers.update(headers)
sleep(1)
requestNrldc = session.get(nrldcUrl)
print "Requesting url: http://nrldc.in/WBS/netdrwlsch.aspx"
soupRequestNrldc   = BeautifulSoup(requestNrldc.content)

VIEWSTATE          = soupRequestNrldc.find(id="__VIEWSTATE")['value']
EVENTTARGET        = soupRequestNrldc.find(id="__EVENTTARGET")['value']
EVENTARGUMENT      = soupRequestNrldc.find(id="__EVENTARGUMENT")['value']
LASTFOCUS          = soupRequestNrldc.find(id="__LASTFOCUS")['value']
EVENTVALIDATION    = soupRequestNrldc.find(id="__EVENTVALIDATION")['value']
VIEWSTATEGENERATOR = soupRequestNrldc.find(id="__VIEWSTATEGENERATOR")['value']

dataNrldc   = {"__VIEWSTATE":VIEWSTATE,
	"__EVENTTARGET":EVENTTARGET,
	"__EVENTARGUMENT":EVENTARGUMENT,
	"__LASTFOCUS":LASTFOCUS,
	"__EVENTVALIDATION":EVENTVALIDATION,
	"__VIEWSTATEGENERATOR":VIEWSTATEGENERATOR,
	"txtStartDate": date,
	"ToStatePickerID": city,
	"RevPickerID":"10"
}
sleep(1)
requestNrldcData    = session.post(nrldcUrl , data=dataNrldc)
soupNrldc           = BeautifulSoup(requestNrldcData.content)
print "Getting data!"
tdNrldc = soupNrldc.findAll("td", {"class": "withBdr"})
#print tdNrldc

tableNrldc = soupNrldc.find('table', {'id': 'demoTable'})
rowTop = tableNrldc.findAll("tr")
row = rowTop[0].findAll("th")
#print row

tdValues = []
for i in xrange(0, len(row)):
	text = row[i].text.split()
	print text
	value = text[0].encode('utf8')
	tdValues.append(value)

blockIndex = tdValues.index("Block")
#print blockIndex
totalIndex = tdValues.index("Total") 
#print totalIndex
#print bilateralIndex
skipBy = totalIndex - blockIndex
#print skipBy

tempValues = []
for i in range(0, len(tdNrldc)):
	tempData =  tdNrldc[i].string.split()
	values = tempData[0].encode("utf8")
	tempValues.append([values])

#print tempValues

finalValues = []
for i in range(totalIndex, len(tempValues), skipBy):
	finalValues.append(tempValues[i])

finalDat = tempDate.strftime("%d-%m-%Y")
def dateBlocks(date):
	return [date]*96

finalDa = dateBlocks(finalDat)
finalDate = []
for i in finalDa:
	finalDate.append([i])

#print finalDate
finalOutput = []
finalOutput.append(["DATE", "TOTAL"])
finalValues = map(add, finalDate, finalValues)
#print finalValues

for i in finalValues:
	finalOutput.append(i)

filePath = "D:\D Drive data\PSPCL\STEP\Exchange Price Projection\All States\SYSTEM\Bilateral"
filename = "TOTAL_"+city+"_"+userDate+".csv"
fullPath = filePath + "\\" + filename

with open(fullPath, 'wb') as fp:
    a = csv.writer(fp, delimiter=',')
    data = finalOutput
    a.writerows(data)

print "Data for NRLDC extracted!"