"""
Author: Kanak
"""

import requests
from bs4 import BeautifulSoup
import filecmp
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

"""Provide a set of key-value pairs of url aliases -> urls like
URL = {"amz": "https://www.amazon.com/", "goog": "https://www.google.com/"}
The aliases can be anything you like, but each alias has to be distinct
"""
URL = {}

#Set these as well
SENDER_EMAIL = ""
PASSWORD = ""
RECEIVER_ADDRESSES = []

"""One way to improve this experience is to make these configurable parameters
into arguments that the main thread takes when executing.
So the script would be executed like this:

python main.py <urls> <sender_email> <password> <receiver_addresses>

But doing that is not worth the time for me.
It could be useful if I were coding this for a team
"""

BASE_HTML_PREFIX = "base"
NEW_HTML_PREFIX = "new"
TIME_INTERVAL = 3600

def gethtml(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.prettify().strip()

def createfilename(prefix, urlalias):
    return prefix + "_" + urlalias + ".txt"

"""Using the same filename will overwrite that file everytime.
That's intentional since this script is intended to be run multiple times
"""
def savehtml(url, basefilename):
    htmlstring = gethtml(url)
    with open(basefilename, 'w') as file:
        file.write(htmlstring)
    print("Saved current HTML into file {}".format(basefilename))

"""Assumes there exists a base file with the naem of basefilename.
Creates a new file with name newfilename.
Returns True if files are same
"""
def comparehtml(url, basefilename, newfilename):
    newhtml = gethtml(url)
    with open(newfilename, 'w') as newfile:
        newfile.write(newhtml)
    print("Saved current HTML into file {}".format(newfilename))
    return filecmp.cmp(newfilename, basefilename)

def sendemails(senderemail, password, recepientemailaddresses, subject, body, textfilenames=[]):
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(senderemail, password)
        for recepient in recepientemailaddresses:
            msg = MIMEMultipart()
            msg["Subject"] = subject
            bodycontent = MIMEText(body)
            msg.attach(bodycontent)
            for filename in textfilenames:
                # To read an image I think you need to specify 'rb'
                with open(filename, 'r') as file:
                    part = MIMEText(file.read())
                    part.add_header('Content-Disposition', 'attachment', filename=filename)
                    msg.attach(part)
            server.sendmail(senderemail, recepient, msg.as_string())
        print("Emails sent")

def mainworkflow():
    if not URL or not SENDER_EMAIL or not PASSWORD or not RECEIVER_ADDRESSES:
        print("PLEASE PROVIDE ALL 4 PARAMETERS - URL, SENDER_EMAIL, PASSWORD, RECEIVER_ADDRESSES")
        return
    for urlalias in URL:
        url = URL[urlalias]
        basefilename = createfilename(BASE_HTML_PREFIX, urlalias)
        savehtml(url, basefilename)
    while True:
        for urlalias in URL:
            url = URL[urlalias]
            basefilename = createfilename(BASE_HTML_PREFIX, urlalias)
            newfilename = createfilename(NEW_HTML_PREFIX, urlalias)
            filesaresame = comparehtml(url, basefilename, newfilename)
            if not filesaresame:
                sendemails(SENDER_EMAIL, PASSWORD, RECEIVER_ADDRESSES, "Hello",
                 "Sent from my script", [basefilename, newfilename])
            else:
                print("HTML files are the same")
        time.sleep(TIME_INTERVAL)

if __name__ == "__main__":
  mainworkflow()