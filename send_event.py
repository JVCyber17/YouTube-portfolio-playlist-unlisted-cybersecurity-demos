import requests
import json

url = "http://localhost:8088/services/collector/event"
token = "561dbecb-0840-4f6f-ac0b-ff440937281c" 

headers = {"Authorization": "Splunk " + token}

data = {
    "event": "Multiple failed login detected from 203.0.113.45",
    "sourcetype": "python_demo"
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.text)

