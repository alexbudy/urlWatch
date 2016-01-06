# the simplest solution - simply run this script at startup 
# - output will go to console and alert if there is a diff
# For first run will compare with specified html file
# 	or create new one if nonexistant
import time
import urllib.request as ur
from sys import argv
import os.path

### default params, can be passed as flags to change
secondsToSleep = 5 # default value = 1 hour. Override with flag
urlToCheck = "blh"
fileToWrite = "sourceOfLastRun.html" # stored in same folder as script by default
sendEmail = False
emailDest = ""
verbose = True
###

def checkUrl():
	with ur.urlopen(urlToCheck) as openedUrl:
		fetchedHtml = str(openedUrl.read().decode('utf-8'))

	if (os.path.isfile(fileToWrite)):
		currentFileHtml = open(fileToWrite).read()
		if (currentFileHtml == fetchedHtml):
			print("same")
		else:
			print("diff")

	else:
		f = open(fileToWrite, 'w')
		f.write(fetchedHtml)
		print("not a file")
	
	

if __name__ == "__main__":
	while True:
		checkUrl()
		time.sleep(secondsToSleep) 
