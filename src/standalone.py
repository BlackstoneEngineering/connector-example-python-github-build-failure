import mbed_connector_api
import requests as r
import json
from time import sleep 
import traceback

# Configure your app
token = "ChangeMe"      # replace with your API token
owner	= 'mbedmicro'	# github user name
repo	= 'mbed'	    # github repo name
ref     = 'master'		# branch name or commit ID

# Settings for Endpoint, copy from your client code
endpoint	= '68a330dc-6f0f-4dd1-a292-59d90a79dbdc' # replace with name of your endpoint to blink LED on
buttonResource = "/3200/0/5501" 
ledResource = "/3201/0/5850"
blinkResource = "/3201/0/5853"


def main():
    connector = mbed_connector_api.connector(token)
    #connector.debug(True,"INFO") # uncomment for debugging of messages
    connector.startLongPolling()
    connector.putResourceValue(endpoint,blinkResource,"5000:1000:5000:1000:5000") # set blink pattern for LED
    while(True):
        # grab data from github
        data = r.get('https://api.github.com/repos/'+owner+'/'+repo+'/commits/'+ref+'/status')
        # parse data for info about the status, 'success' or 'failure'
        data = json.loads(data.content)
        if 'statuses' not in data.keys():
            print("Could not find build status on given page: ")
            print(data)
            return
        else:
            status = data['statuses'][0]['state'] # grab status of build from repo page
            if status == 'failure':
                print "Repo is Failing, turn on the light"
                e = connector.postResource(endpoint,ledResource)
            elif status == 'success':
                  print "Repo is working well, turn off the light"
            elif status == 'error':
                  print "Repo is in Error"
            elif status == 'pending':
                print "Repo is pending changes, wait a bit and try again"
            else:
                print "Current Status is : "+status+"\r\n\r\n"+json.dumps(json.loads(data.content),indent=4,separators=(',',': '))
        sleep(120) # turn on the light every 2 minutes

main() # trigger main function