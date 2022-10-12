import logging
import requests
import json


BASE_URL = 'https://api.zoom.us/v2/'

# FUNCTION TO SEND REQUESTS TO THE ZOOM REST API


def send_request(action, url, data, headers):
    d = json.dumps(data)
    logging.debug("'URL: {0}', 'headers: {1}', 'body: {2}'".format(
        url, headers, d))
    if action == "post":
        r = requests.post(url, headers=headers, data=d)
    elif action == "patch":
        r = requests.patch(url, headers=headers, data=d)
    elif action == "put":
        r = requests.put(url, headers=headers, data=d)
    elif action == "get":
        r = requests.get(url, headers=headers, data=d)
    elif action == "delete":
        r = requests.delete(url, headers=headers, data=d)
    if str(r.status_code).startswith('2'):
        logging.info("'Status: {0}', 'RESPONSE: {1}'".format(
            r.status_code, r.content))
    else:
        logging.warning("'Status: {0}', 'RESPONSE: {1}'".format(
            r.status_code, r.content))
    return r.content
