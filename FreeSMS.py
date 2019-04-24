#GET Method

import requests

url = "https://www.fast2sms.com/dev/bulk"

API_KEY = 'ewzjER9x1hbY3uvLmkZPAHVFy2NO7aMTWCi6lXUp80GntQoD4ccaY7PICAO2k8oW5v3UqsQRBpmV0J9G'
msg = "Successfully sent SMS. Do not share it with others. N.B-This is a test message"
numbers = "8972666690,903866668"
querystring = {"authorization":API_KEY,"sender_id":"FSTSMS","message": msg,"language":"english","route":"p","numbers":numbers}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
