#!/usr/bin/python 
import time
import requests


listOfWebsites = ['https://citethis.net/', 'https://12yearoldsimulator.com/', 'https://kristianwindsor.com/', 'https://passgen.site/', 'https://siliconvalleydrugs.com/']
while True:
	for site in listOfWebsites:
		print(site)
		try:
			r = requests.get(site)
			print(r.status_code)
		except:
			print('expired cert')
		time.sleep(5)
