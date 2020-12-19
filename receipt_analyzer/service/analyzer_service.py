# Service script to make calls to azure form analyzer
# to analyze the receipt and get the results

import json
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

# Method to the uploaded file data and get the results
def analyze_file(uploaded_file: Any):
    data_bytes = uploaded_file.read()
    try:
        # Make POST call for receipt analysis
        resp = post(url=post_url, data=data_bytes, headers=headers, params=params)
        if resp.status_code != 202:
            print("POST analyze failed:%s" % resp.text)
            return
        print("POST analyze succeeded:%s" % resp.headers)
        # Get the URL for the results
        get_url = resp.headers["operation-location"]

        # Get the analysis results
        resp_data = get_analyze_result_from_service(get_url)

        # remove unwanted field from JSON so only relevant data is returned
        resp_data = remove_unwanted_fields(resp_data)

        # Add analysis result id in response so it can be used later to get the results
        analysis_resp = {"analysis_result_id": resp.headers["apim-request-id"]}
        resp_data.update(analysis_resp)
        return resp_data
    except Exception as e:
        print("POST analyze failed:\n%s" % str(e))
        raise

# Method to get receipt analysis results
# using the id and filter and return only relevant fields
def get_analyze_result(analysis_result_id: string):
    # Get the analysis results
    analyze_result_url = analyze_result_base_url + analysis_result_id
    resp_data = get_analyze_result_from_service(analyze_result_url)

    # remove unwanted field from JSON so only relevant data is returned
    resp_data = remove_unwanted_fields(resp_data)

    # Add analysis result id in response so it can be used later to get the results
    analysis_resp = {"analysis_result_id": analysis_result_id}
    resp_data.update(analysis_resp)
    return resp_data

# Method to get receipt analysis raw results
def get_analyze_raw_result(analysis_result_id: string):
    # Get the analysis results
    analyze_result_url = analyze_result_base_url + analysis_result_id
    return get_analyze_result_from_service(analyze_result_url)

# Method to make call to get receipt analysis results
def get_analyze_result_from_service(analyze_result_url: string):
    n_tries = 10
    n_try = 0
    wait_sec = 6
    while n_try < n_tries:
        try:
            # Make GET call to get the analysis results
            resp = get(url=analyze_result_url, headers={"Ocp-Apim-Subscription-Key": apim_key})
            resp_json = json.loads(resp.text)
            if resp.status_code != 200:
                print("GET Receipt results failed:%s" % resp_json)
                return resp_json
            status = resp_json["status"]
            if status == "succeeded":
                print("Receipt Analysis succeeded:%s" % resp_json)
                return resp_json
            if status == "failed":
                print("Analysis failed:%s" % resp_json)
                return resp_json
            # Analysis still running. Wait and retry.
            time.sleep(wait_sec)
            n_try += 1
        except Exception as e:
            msg = "GET analyze results failed:\n%s" % str(e)
            print(msg)
            raise

# Method to remove fields from JSON to keep is small
# and have only relevant fields
def remove_unwanted_fields(data):
    if not isinstance(data, (dict, list)):
        return data
    if isinstance(data, list):
        return [remove_unwanted_fields(v) for v in data]
    return {k: remove_unwanted_fields(v) for k, v in data.items()
            if k not in {'readResults', 'boundingBox', 'elements'}}
