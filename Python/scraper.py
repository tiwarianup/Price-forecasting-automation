import requests
from datetime import datetime, date
from bs4 import BeautifulSoup
import csv
import sys
from time import sleep

userDate = sys.argv[1]
tempDate = datetime.strptime(userDate, "%d%m%Y")
date     = tempDate.strftime("%d/%m/%Y")
print "Scraper started"
print "Downloading data for date: " + date

marketUrl    ="http://www.iexindia.com/marketdata/market_snapshot.aspx"
areaPriceUrl = "http://www.iexindia.com/marketdata/areaprice.aspx"

headers      = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36"}

session = requests.Session()
session.headers.update(headers)
sleep(1)
#################################################################
################### CODE FOR AREA PRICE URL #####################
#################################################################

requestAreaPrice = session.get(areaPriceUrl)
sleep(1.5)
print "Requesting url: http://www.iexindia.com/marketdata/areaprice.aspx"
soupAreaPrice    = BeautifulSoup(requestAreaPrice.content)

VIEWSTATE       = soupAreaPrice.find(id="__VIEWSTATE")['value']
EVENTTARGET     = soupAreaPrice.find(id="__EVENTTARGET")['value']
EVENTARGUMENT   = soupAreaPrice.find(id="__EVENTARGUMENT")['value']
LASTFOCUS       = soupAreaPrice.find(id="__LASTFOCUS")['value']
EVENTVALIDATION = soupAreaPrice.find(id="__EVENTVALIDATION")['value']
SCROLLPOSITIONX = soupAreaPrice.find(id="__SCROLLPOSITIONX")['value']
SCROLLPOSITIONY = soupAreaPrice.find(id="__SCROLLPOSITIONY")['value']

dataAreaPrice   = {"__VIEWSTATE":VIEWSTATE,
	"__EVENTTARGET":EVENTTARGET,
	"__EVENTARGUMENT":EVENTARGUMENT,
	"__LASTFOCUS":LASTFOCUS,
	"__EVENTVALIDATION":EVENTVALIDATION,
	"__SCROLLPOSITIONX":SCROLLPOSITIONX,
	"__SCROLLPOSITIONY":SCROLLPOSITIONY,
	"ctl00$ContentPlaceHolder1$ddlInterval":"15-MINUTE BLOCK",
	"ctl00$ContentPlaceHolder1$ddlPeriod":"-1",
	"ctl00$ContentPlaceHolder1$tbStartDate": date,
	"ctl00$ContentPlaceHolder1$tbEndDate": date,
	"ctl00$ContentPlaceHolder1$ChkAreas$6":"on",
	"ctl00$ContentPlaceHolder1$btnUpdateReport":"Update Report",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl01$ctl02":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl05$ctl00":"Select a format",
	"ctl00$ContentPlaceHolder1$ctl00$ctl04":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl05":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl06":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl07":"0"
}

sleep(1.5)
requestAreaPriceOne         = session.post(areaPriceUrl , data=dataAreaPrice)
soupAreaPrice1              = BeautifulSoup(requestAreaPriceOne.content)
print "Getting data!"
areaPriceRequestUrl         = soupAreaPrice1.find('iframe')['src']
sleep(1.5)
request_areaPriceUrl1       = "http://www.iexindia.com/" + areaPriceRequestUrl 
request_areaPriceUrl2       = session.get(request_areaPriceUrl1)
print "Writing to csv"
soupAreaPrice2              = BeautifulSoup(request_areaPriceUrl2.content)
targetAreaPrice             = soupAreaPrice2.select("#report")[0]['src']
sleep(1.5)
final_request_areaPriceUrl  = "http://www.iexindia.com/" + targetAreaPrice
responseAreaPrice           = session.get(final_request_areaPriceUrl)
soupAreaPrice3              = BeautifulSoup(responseAreaPrice.content)
#print soupAreaPrice3.prettify()
tdArea = soupAreaPrice3.select("td.a41")
data = []
data.append("Price")

for td in tdArea:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	data.append(float(value))

#print data
#print len(data)
priceData = data
#print priceData
#with open('F:\\DataScience\\priceData.csv', 'w') as fp:
#    a = csv.writer(fp, delimiter=',')
#    for i in data:
#    	a.writerow([i])

print "Data for price url extracted!"

#################################################################
###################### CODE FOR MARKET URL ######################
#################################################################
sleep(1)
print "Requesting url: http://www.iexindia.com/marketdata/market_snapshot.aspx"
requestMarket = session.get(marketUrl)
soupMarket    = BeautifulSoup(requestMarket.content)

VIEWSTATE       = soupMarket.find(id="__VIEWSTATE")['value']
EVENTTARGET     = soupMarket.find(id="__EVENTTARGET")['value']
EVENTARGUMENT   = soupMarket.find(id="__EVENTARGUMENT")['value']
LASTFOCUS       = soupMarket.find(id="__LASTFOCUS")['value']
EVENTVALIDATION = soupMarket.find(id="__EVENTVALIDATION")['value']


dataMarket      = {"__VIEWSTATE":VIEWSTATE,
	"__EVENTTARGET":EVENTTARGET,
	"__EVENTARGUMENT":EVENTARGUMENT,
	"__LASTFOCUS":LASTFOCUS,
	"__EVENTVALIDATION":EVENTVALIDATION,
	"ctl00$ContentPlaceHolder1$ddlInterval":"15-MINUTE BLOCK",
	"ctl00$ContentPlaceHolder1$ddlPeriod":"-1",
	"ctl00$ContentPlaceHolder1$tbStartDate": date,
	"ctl00$ContentPlaceHolder1$tbEndDate": date,
	"ctl00$ContentPlaceHolder1$btnUpdateReport":"Update Report",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl01$ctl02":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl05$ctl00":"Select a format",
	"ctl00$ContentPlaceHolder1$ctl00$ctl04":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl05":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl06":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl07":"0"
}

#print dataMarket
sleep(1.5)
print "Getting data!"
requestMarketOne         = session.post(marketUrl , data=dataMarket)
soupMarket1              = BeautifulSoup(requestMarketOne.content)
marketRequestUrl         = soupMarket1.find('iframe')['src']
sleep(1.5)
print "Writing to csv"
request_marketUrl1       = "http://www.iexindia.com/" + marketRequestUrl 
request_marketUrl2       = session.get(request_marketUrl1)
soupMarket2              = BeautifulSoup(request_marketUrl2.content)
targetMarket             = soupMarket2.select("#report")[0]['src']
sleep(1.5)

final_request_marketUrl  = "http://www.iexindia.com/" + targetMarket
responseMarket           = session.get(final_request_marketUrl)
soupMarket3              = BeautifulSoup(responseMarket.content)

tdMarketPurBid = soupMarket3.select("td.a71")
tdMarketSelBid = soupMarket3.select("td.a72")
data = []
data.append("Purchase Bid")

for td in tdMarketPurBid:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	data.append(float(value))

values = []
values.append("Sell Bid")
for td in tdMarketSelBid:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	values.append(float(value))
	
#print values
#print data

#with open('F:\\DataScience\\marketData.csv', 'w') as fp:
#    a = csv.writer(fp, delimiter=',')
#    data = printData
#    a.writerows(data)

def dateBlocks(date):
	return [date]*96

Date = ["Date"]

writeDate = tempDate.strftime("%d-%m-%Y")

for i in dateBlocks(writeDate):
	Date.append(i)
#print Date

Blocks = ["Blocks", "0000-0015", "0015-0030", "0030-0045", "0045-0100", "0100-0115", "0115-0130", "0130-0145", "0145-0200", "0200-0215", "0215-0230", "0230-0245", "0245-0300", "0300-0315", "0315-0330", "0330-0345", "0345-0400", "0400-0415", "0415-0430", "0430-0445", "0445-0500", "0500-0515", "0515-0530", "0530-0545", "0545-0600", "0600-0615", "0615-0630", "0630-0645", "0645-0700", "0700-0715", "0715-0730", "0730-0745", "0745-0800", "0800-0815", "0815-0830", "0830-0845", "0845-0900", "0900-0915", "0915-0930", "0930-0945", "0945-1000", "1000-1015", "1015-1030", "1030-1045", "1045-1100", "1100-1115", "1115-1130", "1130-1145", "1145-1200", "1200-1215", "1215-1230", "1230-1245", "1245-1300", "1300-1315", "1315-1330", "1330-1345", "1345-1400", "1400-1415", "1415-1430", "1430-1445", "1445-1500", "1500-1515", "1515-1530", "1530-1545", "1545-1600", "1600-1615", "1615-1630", "1630-1645", "1645-1700", "1700-1715", "1715-1730", "1730-1745", "1745-1800", "1800-1815", "1815-1830", "1830-1845", "1845-1900", "1900-1915", "1915-1930", "1930-1945", "1945-2000", "2000-2015", "2015-2030", "2030-2045", "2045-2100", "2100-2115", "2115-2130", "2130-2145", "2145-2200", "2200-2215", "2215-2230", "2230-2245", "2245-2300", "2300-2315", "2315-2330", "2330-2345", "2345-2400"]

#print Blocks

finalOutput = zip(Date, Blocks, priceData, data, values)
#print finalOutput

writeData = []

for i in finalOutput:
	writeData.append(list(i))

#print writeData

with open('D:\D Drive data\PSPCL\STEP\Exchange Price Projection\All States\SYSTEM\User Input\user_input.csv', 'wb') as fp:
    a = csv.writer(fp, delimiter=',')
    data = writeData
    a.writerows(data)
print "Data for market url extracted!"

# &; AnupT39 *EOF*