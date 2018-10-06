import requests,json

url = "https://developer.api.yodlee.com:443/ysl/user/login"

payload = {"user": {"loginName": "sbMemd7b5f5124626746c0765654ebe2c85048a1","password": "sbMemd7b5f5124626746c0765654ebe2c85048a1#123", "locale": "en_US"}}
headers = {
    'Api-Version': "1.1",
    'Content-Type': "application/json",
    'Cobrand-Name': "restserver",
    'Authorization': "{cobSession=08062013_0:0ba7db6e6573371cfbb45af7cd97c81837feab68d4ca2fcddb04bdaf8e966ad6dc264348831bbd091acbb32d3e1b0fce8669b548c91dd4ee7c407d657a174736}",
    'Cache-Control': "no-cache",
    'Postman-Token': "7eb3c185-96b9-4ed4-8356-818ab4d2a987"
    }

response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

print(response.text)
