#get account balance
#URL: https://api.kraken.com/0/private/Balance

#for private request, must have request headers and user agent string
"""
Get server time
URL: https://api.kraken.com/0/public/Time

Result: Server's time

unixtime =  as unix timestamp
rfc1123 = as RFC 1123 time format
Note: This is to aid in approximating the skew time between the server and client.
"""
# importing the requests library 
import requests 
  
# api-endpoint 
URL = "https://api.kraken.com/0/public/Time"
  
# location given here 
#location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API 
#PARAMS = {'address':location} 
  
# sending get request and saving the response as response object 
#r = requests.get(url = URL, params = PARAMS) 
r = requests.get(url = URL) 

# extracting data in json format 
data = r.json() 


private_balance_url = "https://api.kraken.com/0/private/Balance"
headers = {'API-key': API_key, 'API-sign' : }

requests.get(url = private_balance_url, headers=headers)

API Key 4wYNY5f9BHIpXXgPwyJ9/zmL5HERrxVZc8tZYhNSBayKc9gU/+vxoeLo
private key E7WVxzKa5tiSGPd+/0x9dCCGTBVwrsmuEdxR3omgLigp5BVykg+P7VXoWIAI69/U9JLHRqH9gFwLLCsgEPMIzw==

Private methods must use POST and be set up as follows:
HTTP header:
API-Key = API key
API-Sign = Message signature using HMAC-SHA512 of (URI path + SHA256(nonce + POST data)) and base64 decoded secret API key


POST data:
nonce = always increasing unsigned 64 bit integer
otp = two-factor password (if two-factor enabled, otherwise not required)

from time import time
import urllib.parse
import hashlib
import hmac

APIkey = b'AAA-BBB-CCC'
secret = b'123abc'

payload = {
    'command': 'returnBalances',
    'nonce': int(time() * 1000),
}

paybytes = urllib.parse.urlencode(payload).encode('utf8')
print(paybytes)

sign = hmac.new(secret, paybytes, hashlib.sha512).hexdigest()
print(sign)
signature = hmac.new(private_key,  hashlib.sha512).hexdigest()