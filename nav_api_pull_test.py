import base64
import hashlib
import hmac
from datetime import datetime
import uuid

def sign_request(
 method, # GET, PUT, POST, DELETE, GET
 pathAndQuery, # Path+Query e.g., /navapigateway/api/v1/InvestorMasterData/GetInvestorListByFund?globalFundID=12345
 body, # Request body 
 apiKey, # Access Key ID
 secret): # Access Key Value
 verb = method.upper()
 utc_now = str(datetime.now().strftime("%a, %d %b %Y %H:%M:%S ")) + "GMT"
 nonce = str(uuid.uuid4())

 content_digest = hashlib.sha256(str(body).encode("utf-8")).digest()
 content_hash = base64.b64encode(content_digest).decode("utf-8")
 
 # String-To-Sign
 string_to_sign = apiKey +";"+ pathAndQuery +";"+ verb +";"+ utc_now +";"+ nonce +";"+ content_hash

 # Please note: /navapigateway should be a part of the url here, as shown in the example (in comment) above.

 # Decode secret
 decoded_secret = secret.encode()
 digest = hmac.new(decoded_secret, str(string_to_sign).encode("utf-8"), hashlib.sha256).digest()

 # Signature
 signature = base64.b64encode(digest).decode("utf-8")
 
 # Result request headers
 return {
 "x-date": utc_now,
 "x-hmac256-signature": apiKey +";"+ nonce +";"+ signature,
 "x-content-sha256": content_hash
 }

x = sign_request("GET", "/api/v1/ClientMasterData/GetFundList","test","API-NT9KQUAP","JU5vRHRcBvgHYAJXmHSvsB2zY/aqDHGMDJoNI2qVIIA=")
print(x)