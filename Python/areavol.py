import requests
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
import csv
import sys
from time import sleep
from operator import add

userDateOne = sys.argv[1]
tempDate = datetime.strptime(userDateOne, "%d%m%Y")
userDateTwo = datetime.strptime(userDateOne, "%d%m%Y") - timedelta(days = 1)
date     = tempDate.strftime("%d/%m/%Y")
print "Scraper started"
print "Downloading data for date: " + date

areaVolUrl    ="http://iexindia.com/marketdata/areavolume.aspx"

headers      = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36"}

session = requests.Session()
session.headers.update(headers)
sleep(1)
#################################################################
################### CODE FOR AREA VOLUME URL ####################
#################################################################

requestAreaVol = session.get(areaVolUrl)
sleep(1.5)
print "Requesting url: http://iexindia.com/marketdata/areavolume.aspx"
soupAreaVol    = BeautifulSoup(requestAreaVol.content)

VIEWSTATE       = soupAreaVol.find(id="__VIEWSTATE")['value']
EVENTTARGET     = soupAreaVol.find(id="__EVENTTARGET")['value']
EVENTARGUMENT   = soupAreaVol.find(id="__EVENTARGUMENT")['value']
LASTFOCUS       = soupAreaVol.find(id="__LASTFOCUS")['value']
EVENTVALIDATION = soupAreaVol.find(id="__EVENTVALIDATION")['value']

# ------------ A1 Starts ---------------

dataAreaPrice   = {"__VIEWSTATE":VIEWSTATE,
	"__EVENTTARGET":EVENTTARGET,
	"__EVENTARGUMENT":EVENTARGUMENT,
	"__LASTFOCUS":LASTFOCUS,
	"__EVENTVALIDATION":EVENTVALIDATION,
	"ctl00$ContentPlaceHolder1$ddlInterval":"15-MINUTE BLOCK",
	"ctl00$ContentPlaceHolder1$ddlPeriod":"-1",
	"ctl00$ContentPlaceHolder1$tbStartDate": date,
	"ctl00$ContentPlaceHolder1$tbEndDate": date,
	"ctl00$ContentPlaceHolder1$ddlVolumeType":"Both",
	"ctl00$ContentPlaceHolder1$ChkAreas$0":"on",
	"ctl00$ContentPlaceHolder1$btnUpdateReport":"Update Report",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl01$ctl02":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl05$ctl00":"Select a format",
	"ctl00$ContentPlaceHolder1$ctl00$ctl04":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl05":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl06":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl07":"0"
}

sleep(1.5)
requestAreaVolOne         = session.post(areaVolUrl , data=dataAreaPrice)
soupAreaVol1              = BeautifulSoup(requestAreaVolOne.content)
print "Getting data!"
areaVolRequestUrl         = soupAreaVol1.find('iframe')['src']
sleep(1.5)
request_areaVolUrl1       = "http://www.iexindia.com/" + areaVolRequestUrl 
request_areaVolUrl2       = session.get(request_areaVolUrl1)
print "Writing to csv"
soupAreaVol2              = BeautifulSoup(request_areaVolUrl2.content)
targetAreaPrice             = soupAreaVol2.select("#report")[0]['src']
sleep(1.5)
final_request_areaVolUrl  = "http://www.iexindia.com/" + targetAreaPrice
responseAreaPrice           = session.get(final_request_areaVolUrl)
soupAreaVol3              = BeautifulSoup(responseAreaPrice.content)
#print soupAreaVol3.prettify()

tdA1Buy = soupAreaVol3.select("td.a56")
tdA1Sell = soupAreaVol3.select("td.a57")

buyA1 = []
buyA1.append(["Buy A1"])

for td in tdA1Buy:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	buyA1.append([value])

sellA1 = []
sellA1.append(["Sell A1"])
for td in tdA1Sell:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	sellA1.append([value])

#print buyA1
#print sellA1

outputA1 = map(add, buyA1, sellA1)
#print outputA1

# ------------ A1 Ends ---------------

# ------------ A2 Starts ---------------

dataAreaPrice   = {"__VIEWSTATE":VIEWSTATE,
	"__EVENTTARGET":EVENTTARGET,
	"__EVENTARGUMENT":EVENTARGUMENT,
	"__LASTFOCUS":LASTFOCUS,
	"__EVENTVALIDATION":EVENTVALIDATION,
	"ctl00$ContentPlaceHolder1$ddlInterval":"15-MINUTE BLOCK",
	"ctl00$ContentPlaceHolder1$ddlPeriod":"-1",
	"ctl00$ContentPlaceHolder1$tbStartDate": date,
	"ctl00$ContentPlaceHolder1$tbEndDate": date,
	"ctl00$ContentPlaceHolder1$ddlVolumeType":"Both",
	"ctl00$ContentPlaceHolder1$ChkAreas$1":"on",
	"ctl00$ContentPlaceHolder1$btnUpdateReport":"Update Report",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl01$ctl02":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl05$ctl00":"Select a format",
	"ctl00$ContentPlaceHolder1$ctl00$ctl04":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl05":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl06":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl07":"0"
}

sleep(1.5)
requestAreaVolOne         = session.post(areaVolUrl , data=dataAreaPrice)
soupAreaVol1              = BeautifulSoup(requestAreaVolOne.content)
print "Getting data!"
areaVolRequestUrl         = soupAreaVol1.find('iframe')['src']
sleep(1.5)
request_areaVolUrl1       = "http://www.iexindia.com/" + areaVolRequestUrl 
request_areaVolUrl2       = session.get(request_areaVolUrl1)
print "Writing to csv"
soupAreaVol2              = BeautifulSoup(request_areaVolUrl2.content)
targetAreaPrice             = soupAreaVol2.select("#report")[0]['src']
sleep(1.5)
final_request_areaVolUrl  = "http://www.iexindia.com/" + targetAreaPrice
responseAreaPrice           = session.get(final_request_areaVolUrl)
soupAreaVol3              = BeautifulSoup(responseAreaPrice.content)
#print soupAreaVol3.prettify()

tdA2Buy = soupAreaVol3.select("td.a56")
tdA2Sell = soupAreaVol3.select("td.a57")

buyA2 = []
buyA2.append(["Buy A2"])

for td in tdA2Buy:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	buyA2.append([value])

sellA2 = []
sellA2.append(["Sell A2"])
for td in tdA2Sell:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	sellA2.append([value])

#print buyA2
#print sellA2

outputA2 = map(add, buyA2, sellA2)
#print outputA2

# ------------ A2 Ends ---------------

# ------------ E1 Starts ---------------

dataAreaPrice   = {"__VIEWSTATE":VIEWSTATE,
	"__EVENTTARGET":EVENTTARGET,
	"__EVENTARGUMENT":EVENTARGUMENT,
	"__LASTFOCUS":LASTFOCUS,
	"__EVENTVALIDATION":EVENTVALIDATION,
	"ctl00$ContentPlaceHolder1$ddlInterval":"15-MINUTE BLOCK",
	"ctl00$ContentPlaceHolder1$ddlPeriod":"-1",
	"ctl00$ContentPlaceHolder1$tbStartDate": date,
	"ctl00$ContentPlaceHolder1$tbEndDate": date,
	"ctl00$ContentPlaceHolder1$ddlVolumeType":"Both",
	"ctl00$ContentPlaceHolder1$ChkAreas$2":"on",
	"ctl00$ContentPlaceHolder1$btnUpdateReport":"Update Report",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl01$ctl02":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl05$ctl00":"Select a format",
	"ctl00$ContentPlaceHolder1$ctl00$ctl04":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl05":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl06":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl07":"0"
}

sleep(1.5)
requestAreaVolOne         = session.post(areaVolUrl , data=dataAreaPrice)
soupAreaVol1              = BeautifulSoup(requestAreaVolOne.content)
print "Getting data!"
areaVolRequestUrl         = soupAreaVol1.find('iframe')['src']
sleep(1.5)
request_areaVolUrl1       = "http://www.iexindia.com/" + areaVolRequestUrl 
request_areaVolUrl2       = session.get(request_areaVolUrl1)
print "Writing to csv"
soupAreaVol2              = BeautifulSoup(request_areaVolUrl2.content)
targetAreaPrice             = soupAreaVol2.select("#report")[0]['src']
sleep(1.5)
final_request_areaVolUrl  = "http://www.iexindia.com/" + targetAreaPrice
responseAreaPrice           = session.get(final_request_areaVolUrl)
soupAreaVol3              = BeautifulSoup(responseAreaPrice.content)

tdE1Buy = soupAreaVol3.select("td.a56")
tdE1Sell = soupAreaVol3.select("td.a57")

buyE1 = []
buyE1.append(["Buy E1"])

for td in tdE1Buy:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	buyE1.append([value])

sellE1 = []
sellE1.append(["Sell E1"])
for td in tdE1Sell:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	sellE1.append([value])

#print buyE1
#print sellE1

outputE1 = map(add, buyE1, sellE1)
#print outputE1

# ------------ E1 Ends ---------------

# ------------ E2 Starts ---------------

dataAreaPrice   = {"__VIEWSTATE":VIEWSTATE,
	"__EVENTTARGET":EVENTTARGET,
	"__EVENTARGUMENT":EVENTARGUMENT,
	"__LASTFOCUS":LASTFOCUS,
	"__EVENTVALIDATION":EVENTVALIDATION,
	"ctl00$ContentPlaceHolder1$ddlInterval":"15-MINUTE BLOCK",
	"ctl00$ContentPlaceHolder1$ddlPeriod":"-1",
	"ctl00$ContentPlaceHolder1$tbStartDate": date,
	"ctl00$ContentPlaceHolder1$tbEndDate": date,
	"ctl00$ContentPlaceHolder1$ddlVolumeType":"Both",
	"ctl00$ContentPlaceHolder1$ChkAreas$3":"on",
	"ctl00$ContentPlaceHolder1$btnUpdateReport":"Update Report",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl01$ctl02":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl05$ctl00":"Select a format",
	"ctl00$ContentPlaceHolder1$ctl00$ctl04":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl05":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl06":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl07":"0"
}

sleep(1.5)
requestAreaVolOne         = session.post(areaVolUrl , data=dataAreaPrice)
soupAreaVol1              = BeautifulSoup(requestAreaVolOne.content)
print "Getting data!"
areaVolRequestUrl         = soupAreaVol1.find('iframe')['src']
sleep(1.5)
request_areaVolUrl1       = "http://www.iexindia.com/" + areaVolRequestUrl 
request_areaVolUrl2       = session.get(request_areaVolUrl1)
print "Writing to csv"
soupAreaVol2              = BeautifulSoup(request_areaVolUrl2.content)
targetAreaPrice             = soupAreaVol2.select("#report")[0]['src']
sleep(1.5)
final_request_areaVolUrl  = "http://www.iexindia.com/" + targetAreaPrice
responseAreaPrice           = session.get(final_request_areaVolUrl)
soupAreaVol3              = BeautifulSoup(responseAreaPrice.content)

tdE2Buy = soupAreaVol3.select("td.a56")
tdE2Sell = soupAreaVol3.select("td.a57")

buyE2 = []
buyE2.append(["Buy E2"])

for td in tdE2Buy:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	buyE2.append([value])

sellE2 = []
sellE2.append(["Sell E2"])
for td in tdE2Sell:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	sellE2.append([value])

#print buyE2
#print sellE2

outputE2 = map(add, buyE2, sellE2)
#print outputE2

# ----------- E2 Ends -----------

# ----------- N1 Starts ---------

dataAreaPrice   = {"__VIEWSTATE":VIEWSTATE,
	"__EVENTTARGET":EVENTTARGET,
	"__EVENTARGUMENT":EVENTARGUMENT,
	"__LASTFOCUS":LASTFOCUS,
	"__EVENTVALIDATION":EVENTVALIDATION,
	"ctl00$ContentPlaceHolder1$ddlInterval":"15-MINUTE BLOCK",
	"ctl00$ContentPlaceHolder1$ddlPeriod":"-1",
	"ctl00$ContentPlaceHolder1$tbStartDate": date,
	"ctl00$ContentPlaceHolder1$tbEndDate": date,
	"ctl00$ContentPlaceHolder1$ddlVolumeType":"Both",
	"ctl00$ContentPlaceHolder1$ChkAreas$4":"on",
	"ctl00$ContentPlaceHolder1$btnUpdateReport":"Update Report",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl01$ctl02":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl05$ctl00":"Select a format",
	"ctl00$ContentPlaceHolder1$ctl00$ctl04":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl05":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl06":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl07":"0"
}

sleep(1.5)
requestAreaVolOne         = session.post(areaVolUrl , data=dataAreaPrice)
soupAreaVol1              = BeautifulSoup(requestAreaVolOne.content)
print "Getting data!"
areaVolRequestUrl         = soupAreaVol1.find('iframe')['src']
sleep(1.5)
request_areaVolUrl1       = "http://www.iexindia.com/" + areaVolRequestUrl 
request_areaVolUrl2       = session.get(request_areaVolUrl1)
print "Writing to csv"
soupAreaVol2              = BeautifulSoup(request_areaVolUrl2.content)
targetAreaPrice             = soupAreaVol2.select("#report")[0]['src']
sleep(1.5)
final_request_areaVolUrl  = "http://www.iexindia.com/" + targetAreaPrice
responseAreaPrice           = session.get(final_request_areaVolUrl)
soupAreaVol3              = BeautifulSoup(responseAreaPrice.content)

tdN1Buy = soupAreaVol3.select("td.a56")
tdN1Sell = soupAreaVol3.select("td.a57")

buyN1 = []
buyN1.append(["Buy N1"])

for td in tdN1Buy:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	buyN1.append([value])

sellN1 = []
sellN1.append(["Sell N1"])
for td in tdN1Sell:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	sellN1.append([value])

#print buyN1
#print sellN1

outputN1 = map(add, buyN1, sellN1)
#print outputN1

#------------- N1 Ends -----------

#------------- N2 Starts ---------

dataAreaPrice   = {"__VIEWSTATE":VIEWSTATE,
	"__EVENTTARGET":EVENTTARGET,
	"__EVENTARGUMENT":EVENTARGUMENT,
	"__LASTFOCUS":LASTFOCUS,
	"__EVENTVALIDATION":EVENTVALIDATION,
	"ctl00$ContentPlaceHolder1$ddlInterval":"15-MINUTE BLOCK",
	"ctl00$ContentPlaceHolder1$ddlPeriod":"-1",
	"ctl00$ContentPlaceHolder1$tbStartDate": date,
	"ctl00$ContentPlaceHolder1$tbEndDate": date,
	"ctl00$ContentPlaceHolder1$ddlVolumeType":"Both",
	"ctl00$ContentPlaceHolder1$ChkAreas$5":"on",
	"ctl00$ContentPlaceHolder1$btnUpdateReport":"Update Report",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl01$ctl02":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl05$ctl00":"Select a format",
	"ctl00$ContentPlaceHolder1$ctl00$ctl04":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl05":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl06":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl07":"0"
}

sleep(1.5)
requestAreaVolOne         = session.post(areaVolUrl , data=dataAreaPrice)
soupAreaVol1              = BeautifulSoup(requestAreaVolOne.content)
print "Getting data!"
areaVolRequestUrl         = soupAreaVol1.find('iframe')['src']
sleep(1.5)
request_areaVolUrl1       = "http://www.iexindia.com/" + areaVolRequestUrl 
request_areaVolUrl2       = session.get(request_areaVolUrl1)
print "Writing to csv"
soupAreaVol2              = BeautifulSoup(request_areaVolUrl2.content)
targetAreaPrice             = soupAreaVol2.select("#report")[0]['src']
sleep(1.5)
final_request_areaVolUrl  = "http://www.iexindia.com/" + targetAreaPrice
responseAreaPrice           = session.get(final_request_areaVolUrl)
soupAreaVol3              = BeautifulSoup(responseAreaPrice.content)

tdN2Buy = soupAreaVol3.select("td.a56")
tdN2Sell = soupAreaVol3.select("td.a57")

buyN2 = []
buyN2.append(["Buy N2"])

for td in tdN2Buy:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	buyN2.append([value])

sellN2 = []
sellN2.append(["Sell N2"])
for td in tdN2Sell:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	sellN2.append([value])

#print buyN2
#print sellN2

outputN2 = map(add, buyN2, sellN2)
#print outputN2

#------------- N2 Ends -----------

#------------- N3 Starts ----------

dataAreaPrice   = {"__VIEWSTATE":VIEWSTATE,
	"__EVENTTARGET":EVENTTARGET,
	"__EVENTARGUMENT":EVENTARGUMENT,
	"__LASTFOCUS":LASTFOCUS,
	"__EVENTVALIDATION":EVENTVALIDATION,
	"ctl00$ContentPlaceHolder1$ddlInterval":"15-MINUTE BLOCK",
	"ctl00$ContentPlaceHolder1$ddlPeriod":"-1",
	"ctl00$ContentPlaceHolder1$tbStartDate": date,
	"ctl00$ContentPlaceHolder1$tbEndDate": date,
	"ctl00$ContentPlaceHolder1$ddlVolumeType":"Both",
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
requestAreaVolOne         = session.post(areaVolUrl , data=dataAreaPrice)
soupAreaVol1              = BeautifulSoup(requestAreaVolOne.content)
print "Getting data!"
areaVolRequestUrl         = soupAreaVol1.find('iframe')['src']
sleep(1.5)
request_areaVolUrl1       = "http://www.iexindia.com/" + areaVolRequestUrl 
request_areaVolUrl2       = session.get(request_areaVolUrl1)
print "Writing to csv"
soupAreaVol2              = BeautifulSoup(request_areaVolUrl2.content)
targetAreaPrice             = soupAreaVol2.select("#report")[0]['src']
sleep(1.5)
final_request_areaVolUrl  = "http://www.iexindia.com/" + targetAreaPrice
responseAreaPrice           = session.get(final_request_areaVolUrl)
soupAreaVol3              = BeautifulSoup(responseAreaPrice.content)

tdN3Buy = soupAreaVol3.select("td.a56")
tdN3Sell = soupAreaVol3.select("td.a57")

buyN3 = []
buyN3.append(["Buy N3"])

for td in tdN3Buy:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	buyN3.append([value])

sellN3 = []
sellN3.append(["Sell N3"])
for td in tdN3Sell:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	sellN3.append([value])

#print buyN3
#print sellN3

outputN3 = map(add, buyN3, sellN3)
#print outputN3

#------------- N3 Ends ------------

#------------- S1 Starts ----------

dataAreaPrice   = {"__VIEWSTATE":VIEWSTATE,
	"__EVENTTARGET":EVENTTARGET,
	"__EVENTARGUMENT":EVENTARGUMENT,
	"__LASTFOCUS":LASTFOCUS,
	"__EVENTVALIDATION":EVENTVALIDATION,
	"ctl00$ContentPlaceHolder1$ddlInterval":"15-MINUTE BLOCK",
	"ctl00$ContentPlaceHolder1$ddlPeriod":"-1",
	"ctl00$ContentPlaceHolder1$tbStartDate": date,
	"ctl00$ContentPlaceHolder1$tbEndDate": date,
	"ctl00$ContentPlaceHolder1$ddlVolumeType":"Both",
	"ctl00$ContentPlaceHolder1$ChkAreas$7":"on",
	"ctl00$ContentPlaceHolder1$btnUpdateReport":"Update Report",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl01$ctl02":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl05$ctl00":"Select a format",
	"ctl00$ContentPlaceHolder1$ctl00$ctl04":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl05":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl06":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl07":"0"
}

sleep(1.5)
requestAreaVolOne         = session.post(areaVolUrl , data=dataAreaPrice)
soupAreaVol1              = BeautifulSoup(requestAreaVolOne.content)
print "Getting data!"
areaVolRequestUrl         = soupAreaVol1.find('iframe')['src']
sleep(1.5)
request_areaVolUrl1       = "http://www.iexindia.com/" + areaVolRequestUrl 
request_areaVolUrl2       = session.get(request_areaVolUrl1)
print "Writing to csv"
soupAreaVol2              = BeautifulSoup(request_areaVolUrl2.content)
targetAreaPrice             = soupAreaVol2.select("#report")[0]['src']
sleep(1.5)
final_request_areaVolUrl  = "http://www.iexindia.com/" + targetAreaPrice
responseAreaPrice           = session.get(final_request_areaVolUrl)
soupAreaVol3              = BeautifulSoup(responseAreaPrice.content)

tdS1Buy = soupAreaVol3.select("td.a56")
tdS1Sell = soupAreaVol3.select("td.a57")

buyS1 = []
buyS1.append(["Buy S1"])

for td in tdS1Buy:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	buyS1.append([value])

sellS1 = []
sellS1.append(["Sell S1"])
for td in tdS1Sell:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	sellS1.append([value])

#print buyS1
#print sellS1

outputS1 = map(add, buyS1, sellS1)
#print outputS1

#------------- S1 Ends ------------

#------------- S2 Starts ----------

dataAreaPrice   = {"__VIEWSTATE":VIEWSTATE,
	"__EVENTTARGET":EVENTTARGET,
	"__EVENTARGUMENT":EVENTARGUMENT,
	"__LASTFOCUS":LASTFOCUS,
	"__EVENTVALIDATION":EVENTVALIDATION,
	"ctl00$ContentPlaceHolder1$ddlInterval":"15-MINUTE BLOCK",
	"ctl00$ContentPlaceHolder1$ddlPeriod":"-1",
	"ctl00$ContentPlaceHolder1$tbStartDate": date,
	"ctl00$ContentPlaceHolder1$tbEndDate": date,
	"ctl00$ContentPlaceHolder1$ddlVolumeType":"Both",
	"ctl00$ContentPlaceHolder1$ChkAreas$8":"on",
	"ctl00$ContentPlaceHolder1$btnUpdateReport":"Update Report",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl01$ctl02":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl05$ctl00":"Select a format",
	"ctl00$ContentPlaceHolder1$ctl00$ctl04":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl05":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl06":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl07":"0"
}

sleep(1.5)
requestAreaVolOne         = session.post(areaVolUrl , data=dataAreaPrice)
soupAreaVol1              = BeautifulSoup(requestAreaVolOne.content)
print "Getting data!"
areaVolRequestUrl         = soupAreaVol1.find('iframe')['src']
sleep(1.5)
request_areaVolUrl1       = "http://www.iexindia.com/" + areaVolRequestUrl 
request_areaVolUrl2       = session.get(request_areaVolUrl1)
print "Writing to csv"
soupAreaVol2              = BeautifulSoup(request_areaVolUrl2.content)
targetAreaPrice             = soupAreaVol2.select("#report")[0]['src']
sleep(1.5)
final_request_areaVolUrl  = "http://www.iexindia.com/" + targetAreaPrice
responseAreaPrice           = session.get(final_request_areaVolUrl)
soupAreaVol3              = BeautifulSoup(responseAreaPrice.content)

tdS2Buy = soupAreaVol3.select("td.a56")
tdS2Sell = soupAreaVol3.select("td.a57")

buyS2 = []
buyS2.append(["Buy S2"])

for td in tdS2Buy:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	buyS2.append([value])

sellS2 = []
sellS2.append(["Sell S2"])
for td in tdS2Sell:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	sellS2.append([value])

#print buyS2
#print sellS2

outputS2 = map(add, buyS2, sellS2)
#print outputS2

#------------- S2 Ends ------------

#------------- W1 Starts ----------

dataAreaPrice   = {"__VIEWSTATE":VIEWSTATE,
	"__EVENTTARGET":EVENTTARGET,
	"__EVENTARGUMENT":EVENTARGUMENT,
	"__LASTFOCUS":LASTFOCUS,
	"__EVENTVALIDATION":EVENTVALIDATION,
	"ctl00$ContentPlaceHolder1$ddlInterval":"15-MINUTE BLOCK",
	"ctl00$ContentPlaceHolder1$ddlPeriod":"-1",
	"ctl00$ContentPlaceHolder1$tbStartDate": date,
	"ctl00$ContentPlaceHolder1$tbEndDate": date,
	"ctl00$ContentPlaceHolder1$ddlVolumeType":"Both",
	"ctl00$ContentPlaceHolder1$ChkAreas$9":"on",
	"ctl00$ContentPlaceHolder1$btnUpdateReport":"Update Report",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl01$ctl02":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl05$ctl00":"Select a format",
	"ctl00$ContentPlaceHolder1$ctl00$ctl04":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl05":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl06":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl07":"0"
}

sleep(1.5)
requestAreaVolOne         = session.post(areaVolUrl , data=dataAreaPrice)
soupAreaVol1              = BeautifulSoup(requestAreaVolOne.content)
print "Getting data!"
areaVolRequestUrl         = soupAreaVol1.find('iframe')['src']
sleep(1.5)
request_areaVolUrl1       = "http://www.iexindia.com/" + areaVolRequestUrl 
request_areaVolUrl2       = session.get(request_areaVolUrl1)
print "Writing to csv"
soupAreaVol2              = BeautifulSoup(request_areaVolUrl2.content)
targetAreaPrice             = soupAreaVol2.select("#report")[0]['src']
sleep(1.5)
final_request_areaVolUrl  = "http://www.iexindia.com/" + targetAreaPrice
responseAreaPrice           = session.get(final_request_areaVolUrl)
soupAreaVol3              = BeautifulSoup(responseAreaPrice.content)

tdW1Buy = soupAreaVol3.select("td.a56")
tdW1Sell = soupAreaVol3.select("td.a57")

buyW1 = []
buyW1.append(["Buy W1"])

for td in tdW1Buy:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	buyW1.append([value])

sellW1 = []
sellW1.append(["Sell W1"])
for td in tdW1Sell:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	sellW1.append([value])

#print buyW1
#print sellW1

outputW1 = map(add, buyW1, sellW1)
#print outputW1

#------------- W1 Ends ------------

#------------- W2 Starts ----------

dataAreaPrice   = {"__VIEWSTATE":VIEWSTATE,
	"__EVENTTARGET":EVENTTARGET,
	"__EVENTARGUMENT":EVENTARGUMENT,
	"__LASTFOCUS":LASTFOCUS,
	"__EVENTVALIDATION":EVENTVALIDATION,
	"ctl00$ContentPlaceHolder1$ddlInterval":"15-MINUTE BLOCK",
	"ctl00$ContentPlaceHolder1$ddlPeriod":"-1",
	"ctl00$ContentPlaceHolder1$tbStartDate": date,
	"ctl00$ContentPlaceHolder1$tbEndDate": date,
	"ctl00$ContentPlaceHolder1$ddlVolumeType":"Both",
	"ctl00$ContentPlaceHolder1$ChkAreas$10":"on",
	"ctl00$ContentPlaceHolder1$btnUpdateReport":"Update Report",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl01$ctl02":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl05$ctl00":"Select a format",
	"ctl00$ContentPlaceHolder1$ctl00$ctl04":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl05":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl06":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl07":"0"
}

sleep(1.5)
requestAreaVolOne         = session.post(areaVolUrl , data=dataAreaPrice)
soupAreaVol1              = BeautifulSoup(requestAreaVolOne.content)
print "Getting data!"
areaVolRequestUrl         = soupAreaVol1.find('iframe')['src']
sleep(1.5)
request_areaVolUrl1       = "http://www.iexindia.com/" + areaVolRequestUrl 
request_areaVolUrl2       = session.get(request_areaVolUrl1)
print "Writing to csv"
soupAreaVol2              = BeautifulSoup(request_areaVolUrl2.content)
targetAreaPrice             = soupAreaVol2.select("#report")[0]['src']
sleep(1.5)
final_request_areaVolUrl  = "http://www.iexindia.com/" + targetAreaPrice
responseAreaPrice           = session.get(final_request_areaVolUrl)
soupAreaVol3              = BeautifulSoup(responseAreaPrice.content)

tdW2Buy = soupAreaVol3.select("td.a56")
tdW2Sell = soupAreaVol3.select("td.a57")

buyW2 = []
buyW2.append(["Buy W2"])

for td in tdW2Buy:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	buyW2.append([value])

sellW2 = []
sellW2.append(["Sell W2"])
for td in tdW2Sell:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	sellW2.append([value])

#print buyW2
#print sellW2

outputW2 = map(add, buyW2, sellW2)
#print outputW2

#------------- W2 Ends -------------

#------------ W3 Starts -----------

dataAreaPrice   = {"__VIEWSTATE":VIEWSTATE,
	"__EVENTTARGET":EVENTTARGET,
	"__EVENTARGUMENT":EVENTARGUMENT,
	"__LASTFOCUS":LASTFOCUS,
	"__EVENTVALIDATION":EVENTVALIDATION,
	"ctl00$ContentPlaceHolder1$ddlInterval":"15-MINUTE BLOCK",
	"ctl00$ContentPlaceHolder1$ddlPeriod":"-1",
	"ctl00$ContentPlaceHolder1$tbStartDate": date,
	"ctl00$ContentPlaceHolder1$tbEndDate": date,
	"ctl00$ContentPlaceHolder1$ddlVolumeType":"Both",
	"ctl00$ContentPlaceHolder1$ChkAreas$11":"on",
	"ctl00$ContentPlaceHolder1$btnUpdateReport":"Update Report",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl01$ctl02":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl05$ctl00":"Select a format",
	"ctl00$ContentPlaceHolder1$ctl00$ctl04":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl05":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl06":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl07":"0"
}

sleep(1.5)
requestAreaVolOne         = session.post(areaVolUrl , data=dataAreaPrice)
soupAreaVol1              = BeautifulSoup(requestAreaVolOne.content)
print "Getting data!"
areaVolRequestUrl         = soupAreaVol1.find('iframe')['src']
sleep(1.5)
request_areaVolUrl1       = "http://www.iexindia.com/" + areaVolRequestUrl 
request_areaVolUrl2       = session.get(request_areaVolUrl1)
print "Writing to csv"
soupAreaVol2              = BeautifulSoup(request_areaVolUrl2.content)
targetAreaPrice             = soupAreaVol2.select("#report")[0]['src']
sleep(1.5)
final_request_areaVolUrl  = "http://www.iexindia.com/" + targetAreaPrice
responseAreaPrice           = session.get(final_request_areaVolUrl)
soupAreaVol3              = BeautifulSoup(responseAreaPrice.content)

tdW3Buy = soupAreaVol3.select("td.a56")
tdW3Sell = soupAreaVol3.select("td.a57")

buyW3 = []
buyW3.append(["Buy W3"])

for td in tdW3Buy:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	buyW3.append([value])

sellW3 = []
sellW3.append(["Sell W3"])
for td in tdW3Sell:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	sellW3.append([value])

#print buyW3
#print sellW3

outputW3 = map(add, buyW3, sellW3)
#print outputW3

#------------ W3 Ends -------------

#------------ Cleared Vol starts -------

dataAreaPrice   = {"__VIEWSTATE":VIEWSTATE,
	"__EVENTTARGET":EVENTTARGET,
	"__EVENTARGUMENT":EVENTARGUMENT,
	"__LASTFOCUS":LASTFOCUS,
	"__EVENTVALIDATION":EVENTVALIDATION,
	"ctl00$ContentPlaceHolder1$ddlInterval":"15-MINUTE BLOCK",
	"ctl00$ContentPlaceHolder1$ddlPeriod":"-1",
	"ctl00$ContentPlaceHolder1$tbStartDate": date,
	"ctl00$ContentPlaceHolder1$tbEndDate": date,
	"ctl00$ContentPlaceHolder1$ddlVolumeType":"Both",
	"ctl00$ContentPlaceHolder1$ChkAreas$12":"on",
	"ctl00$ContentPlaceHolder1$btnUpdateReport":"Update Report",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl01$ctl02":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl05$ctl00":"Select a format",
	"ctl00$ContentPlaceHolder1$ctl00$ctl04":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl05":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl06":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl07":"0"
}

sleep(1.5)
requestAreaVolOne         = session.post(areaVolUrl , data=dataAreaPrice)
soupAreaVol1              = BeautifulSoup(requestAreaVolOne.content)
print "Getting data!"
areaVolRequestUrl         = soupAreaVol1.find('iframe')['src']
sleep(1.5)
request_areaVolUrl1       = "http://www.iexindia.com/" + areaVolRequestUrl 
request_areaVolUrl2       = session.get(request_areaVolUrl1)
print "Writing to csv"
soupAreaVol2              = BeautifulSoup(request_areaVolUrl2.content)
targetAreaPrice             = soupAreaVol2.select("#report")[0]['src']
sleep(1.5)
final_request_areaVolUrl  = "http://www.iexindia.com/" + targetAreaPrice
responseAreaPrice           = session.get(final_request_areaVolUrl)
soupAreaVol3              = BeautifulSoup(responseAreaPrice.content)

tdCvBuy = soupAreaVol3.select("td.a56")
tdCvSell = soupAreaVol3.select("td.a57")

buyCv = []
buyCv.append(["Buy Cleared Volume"])

for td in tdCvBuy:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	buyCv.append([value])

sellCv = []
sellCv.append(["Sell Cleared Volume"])
for td in tdCvSell:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	sellCv.append([value])

#print buyCv
#print sellCv

outputCv = map(add, buyCv, sellCv)
#print outputCv

#------------ Cleared Vol Ends ---------

#------------ MCV Starts --------------

dataAreaPrice   = {"__VIEWSTATE":VIEWSTATE,
	"__EVENTTARGET":EVENTTARGET,
	"__EVENTARGUMENT":EVENTARGUMENT,
	"__LASTFOCUS":LASTFOCUS,
	"__EVENTVALIDATION":EVENTVALIDATION,
	"ctl00$ContentPlaceHolder1$ddlInterval":"15-MINUTE BLOCK",
	"ctl00$ContentPlaceHolder1$ddlPeriod":"-1",
	"ctl00$ContentPlaceHolder1$tbStartDate": date,
	"ctl00$ContentPlaceHolder1$tbEndDate": date,
	"ctl00$ContentPlaceHolder1$ddlVolumeType":"Both",
	"ctl00$ContentPlaceHolder1$ChkAreas$13":"on",
	"ctl00$ContentPlaceHolder1$btnUpdateReport":"Update Report",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl01$ctl02":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl01$ctl05$ctl00":"Select a format",
	"ctl00$ContentPlaceHolder1$ctl00$ctl04":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl05":"",
	"ctl00$ContentPlaceHolder1$ctl00$ctl06":"1",
	"ctl00$ContentPlaceHolder1$ctl00$ctl07":"0"
}

sleep(1.5)
requestAreaVolOne         = session.post(areaVolUrl , data=dataAreaPrice)
soupAreaVol1              = BeautifulSoup(requestAreaVolOne.content)
print "Getting data!"
areaVolRequestUrl         = soupAreaVol1.find('iframe')['src']
sleep(1.5)
request_areaVolUrl1       = "http://www.iexindia.com/" + areaVolRequestUrl 
request_areaVolUrl2       = session.get(request_areaVolUrl1)
print "Writing to csv"
soupAreaVol2              = BeautifulSoup(request_areaVolUrl2.content)
targetAreaPrice             = soupAreaVol2.select("#report")[0]['src']
sleep(1.5)
final_request_areaVolUrl  = "http://www.iexindia.com/" + targetAreaPrice
responseAreaPrice           = session.get(final_request_areaVolUrl)
soupAreaVol3              = BeautifulSoup(responseAreaPrice.content)

tdMcvBuy = soupAreaVol3.select("td.a56")
tdMcvSell = soupAreaVol3.select("td.a57")

buyMcv = []
buyMcv.append(["Buy MCV"])

for td in tdMcvBuy:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	buyMcv.append([value])

sellMcv = []
sellMcv.append(["Sell MCV"])
for td in tdMcvSell:
	dat = td.string.split()
	value = dat[0].encode('utf8')
	sellMcv.append([value])

#print buyMcv
#print sellMcv

outputMcv = map(add, buyMcv, sellMcv)
#print outputMcv

#------------- MCV Ends --------------

#outputA1, outputA2, outputE1, outputE2, outputN1, outputN2, outputN3, outputS1, outputS2, outputW1, outputW2, outputW3, outputCv, outputMcv

finalDat = tempDate.strftime("%d-%m-%Y")
def dateBlocks(date):
	return [date]*96

finalDa = dateBlocks(finalDat)
finalDate = [["Date"]]
for i in finalDa:
	finalDate.append([i])
#print finalDate

Blocks = [["Blocks"], ["0000-0015"], ["0015-0030"], ["0030-0045"], ["0045-0100"], ["0100-0115"], ["0115-0130"], ["0130-0145"], ["0145-0200"], ["0200-0215"], ["0215-0230"], ["0230-0245"], ["0245-0300"], ["0300-0315"], ["0315-0330"], ["0330-0345"], ["0345-0400"], ["0400-0415"], ["0415-0430"], ["0430-0445"], ["0445-0500"], ["0500-0515"], ["0515-0530"], ["0530-0545"], ["0545-0600"], ["0600-0615"], ["0615-0630"], ["0630-0645"], ["0645-0700"], ["0700-0715"], ["0715-0730"], ["0730-0745"], ["0745-0800"], ["0800-0815"], ["0815-0830"], ["0830-0845"], ["0845-0900"], ["0900-0915"], ["0915-0930"], ["0930-0945"], ["0945-1000"], ["1000-1015"], ["1015-1030"], ["1030-1045"], ["1045-1100"], ["1100-1115"], ["1115-1130"], ["1130-1145"], ["1145-1200"], ["1200-1215"], ["1215-1230"], ["1230-1245"], ["1245-1300"], ["1300-1315"], ["1315-1330"], ["1330-1345"], ["1345-1400"], ["1400-1415"], ["1415-1430"], ["1430-1445"], ["1445-1500"], ["1500-1515"], ["1515-1530"], ["1530-1545"], ["1545-1600"], ["1600-1615"], ["1615-1630"], ["1630-1645"], ["1645-1700"], ["1700-1715"], ["1715-1730"], ["1730-1745"], ["1745-1800"], ["1800-1815"], ["1815-1830"], ["1830-1845"], ["1845-1900"], ["1900-1915"], ["1915-1930"], ["1930-1945"], ["1945-2000"], ["2000-2015"], ["2015-2030"], ["2030-2045"], ["2045-2100"], ["2100-2115"], ["2115-2130"], ["2130-2145"], ["2145-2200"], ["2200-2215"], ["2215-2230"], ["2230-2245"], ["2245-2300"], ["2300-2315"], ["2315-2330"], ["2330-2345"], ["2345-2400"]]

#print Blocks

datenBlocks = map(add, finalDate, Blocks)
#print datenBlocks
finalOut0 = map(add, datenBlocks, outputA1)
finalOut1 = map(add, finalOut0, outputA2)
finalOut2 = map(add, finalOut1, outputE1)
finalOut3 = map(add, finalOut2, outputE2)
finalOut4 = map(add, finalOut3, outputN1)
finalOut5 = map(add, finalOut4, outputN2)
finalOut6 = map(add, finalOut5, outputN3)
finalOut7 = map(add, finalOut6, outputS1)
finalOut8 = map(add, finalOut7, outputS2)
finalOut9 = map(add, finalOut8, outputW1)
finalOut10 = map(add, finalOut9, outputW2)
finalOut11 = map(add, finalOut10, outputW3)
finalOut12 = map(add, finalOut11, outputCv)
finalOut13 = map(add, finalOut12, outputMcv)

finalOutput = []

for i in finalOut13:
	finalOutput.append(i)

#print finalOutput

filePath = "D:\D Drive data\PSPCL\STEP\Exchange Price Projection\All States\SYSTEM\AreaVolume"
filename = "AreaVolume_"+"_"+userDateOne+".csv"
fullPath = filePath + "\\" + filename

with open(fullPath, 'wb') as fp:
    a = csv.writer(fp, delimiter=',')
    data = finalOutput
    a.writerows(data)

print "Data for Area Volume Link extracted!"