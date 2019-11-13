#!/usr/bin/python 
import time
import requests


#send slack message 
def slackmessage():
	print("hi")
	#slack_token = os.environ["SLACK_API_TOKEN"]
				#client = slack.WebClient(token=slack_token)

				#client.chat_postMessage(
				 # channel="site",
				 # text="404 error"
				#)


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
