# Python Form Recognizer Async Receipt

import json
import logging
import string
import time
from typing import Any

from requests import get, post

# Endpoint URL
endpoint = r"https://psreceiptrecognizer.cognitiveservices.azure.com/"
apim_key = "60f777467efb43dc8eee6f07fa646f7a"
post_url = endpoint + "/formrecognizer/v2.0/prebuilt/receipt/analyze"
analyze_result_base_url = endpoint + "/formrecognizer/v2.0/prebuilt/receipt/analyzeResults/"
headers = {
    # Request headers
    'Content-Type': 'image/jpeg',
    'Ocp-Apim-Subscription-Key': apim_key,
}

params = {
    "includeTextDetails": True
}

log = logging.getLogger(__name__)

def analyze_file(uploaded_file: Any):
    data_bytes = uploaded_file.read()
    try:
        resp = post(url=post_url, data=data_bytes, headers=headers, params=params)
        if resp.status_code != 202:
            log.error("POST analyze failed:%s" % resp.text)
            return
        log.info("POST analyze succeeded:%s" % resp.headers)
        get_url = resp.headers["operation-location"]
        return get_analyze_result(get_url)
    except Exception as e:
        print("POST analyze failed:\n%s" % str(e))
        raise

def get_analyze_result(id: string):
    return get_analyze_raw_result(id)

def get_analyze_raw_result(id: string):
    analyze_result_url = analyze_result_base_url + id
    return get_analyze_result(analyze_result_url)

def get_analyze_result(analyze_result_url: string):
    n_tries = 10
    n_try = 0
    wait_sec = 6
    while n_try < n_tries:
        try:
            resp = get(url=analyze_result_url, headers={"Ocp-Apim-Subscription-Key": apim_key})
            resp_json = json.loads(resp.text)
            if resp.status_code != 200:
                log.info("GET Receipt results failed:%s" % resp_json)
                return resp_json
            status = resp_json["status"]
            if status == "succeeded":
                log.info("Receipt Analysis succeeded:%s" % resp_json)
                return resp_json
            if status == "failed":
                log.info("Analysis failed:%s" % resp_json)
                return resp_json
            # Analysis still running. Wait and retry.
            time.sleep(wait_sec)
            n_try += 1
        except Exception as e:
            msg = "GET analyze results failed:\n%s" % str(e)
            log.error(msg)
            raise

