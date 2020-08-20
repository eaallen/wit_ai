import requests
import json


headers = {
    'Authorization': 'Bearer NDE5TQ3JWRA327RQF2USO4TIQ7SW234B',
}

params = (
    ('v', '20200819'),
    ('q', 'what is the tempatare'),
)

response = requests.get('https://api.wit.ai/message', headers=headers, params=params)

rsp = json.loads(response.text)

print(rsp['intents'])



# curl \
#  -H 'Authorization: Bearer NDE5TQ3JWRA327RQF2USO4TIQ7SW234B' \
#  'https://api.wit.ai/message?v=20200819&q=what%27s%20the%20temperature%20in%20there%3F'
