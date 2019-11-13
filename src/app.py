#!/usr/bin/python 
import time
import requests
import json
import os


#send slack message 
def slackmessage():
	slackUrl = "https://hooks.slack.com/services/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"
	data = {
		'token': os.environ['SLACK_TOKEN'],
		'channel': 'uptimebot',
		'text': 'hello'
	}
	headers = {
		'Content-type': 'application/json'
	}
	requests.post(slackUrl, data=json.dumps(data), headers=headers)


listOfWebsites = ['https://citethis.net/', 'https://12yearoldsimulator.com/', 'https://kristianwindsor.com/', 'https://passgen.site/', 'https://siliconvalleydrugs.com/']
while True:
	for site in listOfWebsites:
		print(site)
		try:
			r = requests.get(site)
			print(r.status_code)
			if r.status_code != 200:
				slackmessage()
		except:
			print('expired cert')
			slackmessage()
		time.sleep(5)
