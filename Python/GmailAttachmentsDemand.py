#Sayani's code

import email, getpass, imaplib, os, sys
from datetime import datetime, date, timedelta
import os
import time
import shutil
from pyunpack import Archive

detach_dir = "D:\D Drive data\PSPCL\STEP\Exchange Price Projection\All States\SYSTEM\Email Attachments"

user = "priceforecastteam" #sys.argv[1]
pwd = "pusasuni" #sys.argv[2] 
m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user,pwd)
m.select("[Gmail]/All Mail", readonly=True)

d = date.today() - timedelta(days=0)
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
        if mail["Subject"] == "Demand Forecasting Data" or mail["Subject"] == "Re: Demand Forecasting Data":
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


pathDelhi       = "D:\D Drive data\PSPCL\STEP\Exchange Price Projection\All States\SYSTEM\Delhi"
pathGujarat     = "D:\D Drive data\PSPCL\STEP\Exchange Price Projection\All States\SYSTEM\Gujarat"
pathHaryana     = "D:\D Drive data\PSPCL\STEP\Exchange Price Projection\All States\SYSTEM\Haryana"
pathMaharashtra = "D:\D Drive data\PSPCL\STEP\Exchange Price Projection\All States\SYSTEM\Maharashtra"
pathMP          = "D:\D Drive data\PSPCL\STEP\Exchange Price Projection\All States\SYSTEM\MP"
pathOrissa      = "D:\D Drive data\PSPCL\STEP\Exchange Price Projection\All States\SYSTEM\Orissa"
pathRajasthan   = "D:\D Drive data\PSPCL\STEP\Exchange Price Projection\All States\SYSTEM\Rajasthan"
pathUK          = "D:\D Drive data\PSPCL\STEP\Exchange Price Projection\All States\SYSTEM\UK"
pathUP          = "D:\D Drive data\PSPCL\STEP\Exchange Price Projection\All States\SYSTEM\UP"
pathWB          = "D:\D Drive data\PSPCL\STEP\Exchange Price Projection\All States\SYSTEM\WB"
pathExtra       = "D:\D Drive data\PSPCL\STEP\Exchange Price Projection\All States\SYSTEM\Extra"

if not os.path.exists(pathExtra):
    os.makedirs(pathExtra)

tempDirectory = detach_dir + "\\Temp"
print tempDirectory

if not os.path.exists(tempDirectory):
    os.makedirs(tempDirectory)

for files in filenames:
    os.chdir(detach_dir)
    Archive(os.path.abspath(files)).extractall(tempDirectory)

tempfiles = [f for f in os.listdir(tempDirectory)]
#print tempfiles


for tempfile in tempfiles:
    os.chdir(tempDirectory)
    if tempfile.lower()[0:2] == "gu":
        shutil.copy(tempfile, pathGujarat)
    elif tempfile.lower()[0:2] == "de":
        shutil.copy(tempfile, pathDelhi)
    elif tempfile.lower()[0:2] == "ha":
        shutil.copy(tempfile, pathHaryana)
    elif tempfile.lower()[0:2] == "ma":
        shutil.copy(tempfile, pathMaharashtra)
    elif tempfile.lower()[0:2] == "mp":
        shutil.copy(tempfile, pathMP)
    elif tempfile.lower()[0:2] == "or":
        shutil.copy(tempfile, pathOrissa)
    elif tempfile.lower()[0:2] == "ra":
        shutil.copy(tempfile, pathRajasthan)
    elif tempfile.lower()[0:2] == "uk":
        shutil.copy(tempfile, pathUK)
    elif tempfile.lower()[0:2] == "up":
        shutil.copy(tempfile, pathUP)
    elif tempfile.lower()[0:2] == "wb":
        shutil.copy(tempfile, pathWB)
    else:
        shutil.copy(tempfile, pathExtra)

os.chdir(detach_dir)
shutil.rmtree(tempDirectory)
