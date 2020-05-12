"""
Fetches OnCall data from the PagerDuty API then uses the pymsteams library to compose a message and 
"""

import requests
import json
import pymsteams  # Library used to integrate with MS Teams

URL = "https://api.pagerduty.com/oncalls?schedule_ids[]=specific_schedule_id"
apiKey = "API Token"

headers = {
    'accept': "application/vnd.pagerduty+json;version=2",
    'authorization': apiKey
}

response = requests.request("GET", URL, headers=headers)
data = response.json()
#data2 = json.dumps(data, indent=2)

for item in data['oncalls']:
    execOnCall = item['user']['summary']

if execOnCall == "Person 1":
    execPhone = "Contact Number"
    execEmail = "person1@company.com"
elif execOnCall == "Person 2":
    execPhone = "Contact Number"
    execEmail = "person2@company.com"
elif execOnCall == "Person 3":
    execPhone = "Contact Number"
    execEmail = "person3@company.com"
elif execOnCall == "Person 4":
    execPhone = "Contact Number"
    execEmail = "person4@company.com"
else:
    execPhone = "ERROR"
    execEmail = "ERROR"

# Start composing message for MS Teams
# Teams channel webhook URL
webhook = "Webhook Link"

# disable Certificate validation // You must create the connectorcard object with the Microsoft Webhook URL
msg = pymsteams.connectorcard(webhook, verify=False)

# Building the Card Section to be added to the main message
myMessageSection = pymsteams.cardsection()
myMessageSection2 = pymsteams.cardsection()
myMessageSection3 = pymsteams.cardsection()
myMessageSection4 = pymsteams.cardsection()

myMessageSection.text(execOnCall)
myMessageSection2.text(execPhone)
myMessageSection3.text(execEmail)
myMessageSection4.title("Standby Schedule")

# Add text to the message
msg.summary("Retreiving the OnCall schedule for Execs")
msg.addSection(myMessageSection4)
msg.addSection(myMessageSection)
msg.addSection(myMessageSection2)
msg.addSection(myMessageSection3)
msg.addLinkButton("View PD Schedule",
                  "https://derivco.pagerduty.com/schedules#P2RZ9GZ")

# send the message
# msg.printme()
msg.send()
