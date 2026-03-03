import base64
import hashlib
import hmac
import uuid
import pandas as pd
from datetime import datetime

import requests


def sign_request(method, pathAndQuery, body, apiKey, secret):
    verb = method.upper()
    utc_now = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S ") + "GMT"
    nonce = str(uuid.uuid4())

    content_digest = hashlib.sha256(str(body).encode("utf-8")).digest()
    content_hash = base64.b64encode(content_digest).decode("utf-8")

    string_to_sign = apiKey + ";" + pathAndQuery + ";" + verb + ";" + utc_now + ";" + nonce + ";" + content_hash

    decoded_secret = secret.encode("utf-8")
    digest = hmac.new(decoded_secret, str(string_to_sign).encode("utf-8"), hashlib.sha256).digest()

    signature = base64.b64encode(digest).decode("utf-8")

    return {
        "x-date": utc_now,
        "x-hmac256-signature": apiKey + ";" + nonce + ";" + signature,
        "x-content-sha256": content_hash,
    }


def get_trading_gain_loss(base_url, api_key, api_secret, nav_global_fund_id, report_date):
    method = "GET"
    #path = "/navapigateway/api/v1/" + api_root + "/" + api_call
    path = "/navapigateway/api/v1/FundReportData/GetTradingGainLossForFund?globalFundID=" + nav_global_fund_id + "&reportDate=" + report_date
    url = base_url + path

    body = ""  # GET: empty string

    headers = sign_request(method, path, body, api_key, api_secret)
    headers["Accept"] = "application/json"

    # Some gateways also require this even if docs don't; harmless to include:
    headers["Authorization"] = headers["x-hmac256-signature"]

    resp = requests.get(url, headers=headers, timeout=(10, 60))
    if not resp.ok:
        print("URL:", url)
        print("Status:", resp.status_code)
        print("Resp text:", resp.text[:500])
        print("x-date:", headers["x-date"])
        print("x-content-sha256:", headers["x-content-sha256"])
        print("x-hmac256-signature:", headers["x-hmac256-signature"])
        raise RuntimeError(f"HTTP {resp.status_code}: {resp.text[:1500]}")

    return pd.DataFrame(resp.json())


if __name__ == "__main__":
    BASE_URL = "https://api.navfundservices.com"
    API_KEY = "API-NT9KQUAP"
    API_SECRET = "JU5vRHRcBvgHYAJXmHSvsB2zY/aqDHGMDJoNI2qVIIA="
#    #API_ROOT = "ClientMasterData"
#    #API_CALL = "GetFundList"

    print(get_trading_gain_loss(BASE_URL, API_KEY, API_SECRET))