---
layout: home
title: "ATBS: Texting"
permalink: /bookclubbot
---

# HOW TO:

(Inspired by ATBS Ch. 16)

1. Use python script to text the people
2. Use Node + express + heroku to make an endpoint for twilio webhook
3. Check twilio's page

---

## SEND OUT TEXT:

NOTE: LOCALLY PROJECTS/TWILIO

```python
from twilio.rest import Client
accountSID = "MY_ACCOUNT_SID"
authToken = "MY_AUTH_TOKEN"
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+xxxx'

# ONE MESSAGE
myCellPhone = '+xxxxxx'
message = twilioCli.messages.create(body="BOOKCLUB BOT: Does this upcoming Tuesday at 1PST/4EST work for you? Simply reply 'yes' or 'no'!", from_=myTwilioNumber, to=myCellPhone)

# MANY MESSAGES:
# numbers = ['+xxxxx', '+xxxxx', '+xxxxx', '+xxxxx']
numbers = ['+xxxxxxx']

for number in numbers:
    twilioCli.messages.create(body="BOOKCLUB BOT: Does this upcoming Tuesday at 1PST/4EST work for you? Simply reply 'yes' or 'no'!", from_=myTwilioNumber, to=number)
    print(number)
```

## TEXT HITS ENDPOINT

NOTE: Endpoint is the tinest express app on heroku.

[Puma Pants Texting](https://pumapantstexting.herokuapp.com/)
^ Literally nothing there because we only care about the endpoint which sends a response back to the text
