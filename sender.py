import requests

webhook_url = 'http://localhost:8000/webhook'

data = {
  'name': 'Jan du `plessis',
  'user_id': 1235678906789045,
  'description': "this is a test",
}

response = requests.post(webhook_url, json=data)
print(response)
