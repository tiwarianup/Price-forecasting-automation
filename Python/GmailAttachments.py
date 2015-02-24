import email, getpass, imaplib, os, sys
from datetime import datetime, date, timedelta
import os
import time
import shutil
from pyunpack import Archive

detach_dir = 'D:\\D Drive data\\PSPCL\\STEP\\Exchange Price Projection\\All States\\SYSTEM\\Email Attachments'

user = "priceforecastteam" #sys.argv[1]
pwd = "pusasuni" #sys.argv[2] 
m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user,pwd)
m.select("[Gmail]/All Mail", readonly = True)

d = date.today() - timedelta(days = 0)
e = d.strftime("%d-%m-%y")
f = datetime.strptime(e, "%d-%m-%y")
g = f.strftime("%d-%b-%y")
#print g
x = '(SINCE "'+ g +'")'
#print x
resp, items = m.search(None, x) 
items = items[0].split()
print "Searching mails for date: " + x
print items, resp 
print "Emails found"
print "Please wait while attachments are downloaded..."

filenames = []

for emailid in items:
    resp, data = m.fetch(emailid, "(RFC822)")
    email_body = data[0][1]
    #print email_body
    mail = email.message_from_string(email_body)
    #print mail

    if mail.get_content_maintype() != 'multipart':
        continue

    print "["+mail["From"]+"] :" + mail["Subject"] + " " + mail["Date"]
    #print mail["From"]
    if mail["From"] == "Sayani Gupta <gupta.sayani@gmail.com>" or mail["From"] == "Ashwani Kumar <dilseashu@yahoo.co.in>":
        if mail["Subject"] == "Re: Model_Input_Files_Price_Forecast" or mail["Subject"] == "Model_Input_Files_Price_Forecast":
            for part in mail.walk():
                if part.get_content_maintype() == 'multipart':
                    continue

                if part.get('Content-Disposition') is None:
                    continue
            
                filename = part.get_filename()
                print filename
                counter = 1

                if not filename:
                    filename = 'part-%03d%s' % (counter, 'bin')
                    counter += 1

                filenames.append(filename)
                    
                att_path = os.path.join(detach_dir, filename)
                print att_path
                if not os.path.isfile(att_path):
                    fp = open(att_path, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()

print "Emails downloaded!" 
# -----------------------------------------------------------------------------------


pathOne = "D:\D Drive data\PSPCL\STEP\Exchange Price Projection\All States\SYSTEM\Price Model_IPP"
pathTwo = "D:\D Drive data\PSPCL\STEP\Exchange Price Projection\All States\SYSTEM\Price Model_NO IPP"
detach_dir = 'D:\\D Drive data\\PSPCL\\STEP\\Exchange Price Projection\\All States\\SYSTEM\\Email Attachments'

#month = datetime.now().strftime("%B")
#year = datetime.now().strftime("%Y")

#date = date.today() + timedelta(days=1)
#todaysDate = date.strftime("%d%m%Y")

#folderName = todaysDate

#filenames = [f for f in os.listdir(detach_dir)]

print filenames

for i in filenames:
    folderName = i.split(".")[0]
    os.chdir(pathOne)
    if not os.path.exists(folderName):
            os.makedirs(folderName)
    os.chdir(pathTwo)
    if not os.path.exists(folderName):
        os.makedirs(folderName)
    os.chdir(detach_dir)
    pathIpp = pathOne + "\\" + folderName
    pathNoIpp = pathTwo + "\\" + folderName
    print i
    Archive(i).extractall(pathIpp)
    Archive(i).extractall(pathNoIpp)
