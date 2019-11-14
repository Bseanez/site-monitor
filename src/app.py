#!/usr/bin/python 
import time
import requests
import json
import os


#send slack message 
def slackmessage(message):
	data = {
		'token': os.environ['SLACK_TOKEN'],
		'channel': 'uptimebot',
		'text': message
	}
	headers = {
		'Content-type': 'application/json'
	}
	r = requests.post(os.environ['SLACK_URL'], data=json.dumps(data), headers=headers)
	print(r)



listOfWebsites = ['https://citethis.net/', 'https://12yearoldsimulator.com/', 'https://kristianwindsor.com/', 'https://passgen.site/', 'https://siliconvalleydrugs.com/']
while True:
	for site in listOfWebsites:
		print(site)
		try:
			r = requests.get(site)
			print(r.status_code)
			if r.status_code != 200:
				slackmessage(site)
		except:
			print('expired cert')
			slackmessage(site)
		time.sleep(20)
