import logging
import requests
import json
import base64
from dotenv import load_dotenv
import os
from lib.token import *


BASE_URL = 'https://api.zoom.us/v2/'

# FUNCTION TO SEND REQUESTS TO THE ZOOM REST API


def send_request(action, url, data):
    t = token()
    FINAL_URL = BASE_URL+url
    headers = {'authorization': 'Bearer %s' % t,
               'content-type': 'application/json'}
    logging.debug("'URL: {0}', 'headers: {1}', 'body: {2}'".format(
        FINAL_URL, headers, data))
    if action == "post":
        r = requests.post(FINAL_URL, headers=headers, data=data)
    elif action == "patch":
        r = requests.patch(FINAL_URL, headers=headers, data=data)
    elif action == "put":
        r = requests.put(FINAL_URL, headers=headers, data=data)
    elif action == "get":
        r = requests.get(FINAL_URL, headers=headers, data=data)
    elif action == "delete":
        r = requests.delete(FINAL_URL, headers=headers, data=data)
    if str(r.status_code).startswith('2'):
        logging.info("'Status: {0}', 'RESPONSE: {1}'".format(
            r.status_code, r.content))
    else:
        logging.warning("'Status: {0}', 'RESPONSE: {1}'".format(
            r.status_code, r.content))
    return r.content