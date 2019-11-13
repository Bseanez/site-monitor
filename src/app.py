#!/usr/bin/python 
import time
import requests


listOfWebsites = ['https://citethis.net/', 'https://12yearoldsimulator.com/']
while True:
	for site in listOfWebsites:
		print(site)
		r = requests.get(site)
		print(r.status_code)
		time.sleep(5)
