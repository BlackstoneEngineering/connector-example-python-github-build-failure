import web      # web.py framework for webapp
import mdc_api  # mbed Device Connector Library to talk to device
import requests as r
import json

# Configure your app
token = "CHXKYI7AN334D5WQI9DU9PMMDR8G6VPX3763LOT6"
connector = mdc_api.connector(token)
owner	= 'mbedmicro'		# github user name
repo	= 'mbed'			# github repo name
ref 	= 'master'			# branch name or commit ID

endpoint	= '145da9b5-a76a-486f-b25a-3a190effb596'
resource	= '/led/0/red'
led_off		= 1
led_on		= 0

# map URL to class to handle requests
urls = (
	'/', 'index',
)

class index:
	def GET(self):
		# grab info about repo from github statuses api
		data = r.get('https://api.github.com/repos/'+owner+'/'+repo+'/commits/'+ref+'/status')
		# parse data for info about the status, 'success' or 'failure'
		status = json.loads(data.content)['statuses'][0]['state']
		if status == 'failure':
			print "Repo is Failing, turn on the light"
			e = connector.postResource(endpoint,resource,led_on)
		elif status == 'success':
			print "Repo is working well, turn off the light"
			e = connector.postResource(endpoint,resource,led_off)
		elif status == 'error':
			print "Repo is in Error"
		elif status == 'pending':
			print "Repo is pending changes, wait a bit and try again"
		return "Current Status is : "+status+"\r\n\r\n"+json.dumps(json.loads(data.content),indent=4,separators=(',',': '))

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
	connector.debug(True)
	connector.startLongPolling()
	
