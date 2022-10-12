# IMPORT
from base64 import b64encode
from utils.log import *
from utils.req import *
from utils.printJSON import *
import webbrowser
from dotenv import load_dotenv
import os
import base64
from termcolor import colored, cprint
from pyfiglet import Figlet
import qrcode
import qrcode.image.svg
from glob import glob
import urllib

qr = True
f = Figlet(font='big')
print(f.renderText('Ford Demo'))

# auth data for getting server to server OAuth Token requires appropriate scopes
load_dotenv()
clientid = os.environ.get("CLIENTID")
clientsecret = os.environ.get("CLIENTSECRET")

# SETUP LOGGING
create_log()


def basic_auth():
    message = "%s:%s" % (clientid, clientsecret)
    auth = base64.b64encode(message.encode()).decode()
    return auth


def get_verification_uri():
    logging.info("Fetching URI")
    cprint("Fetching Verification URL and redirecting to browser", "green")
    message = "%s:%s" % (clientid, clientsecret)
    auth = basic_auth()
    data = {}
    url = "https://zoom.us/oauth/devicecode?client_id=%s" % clientid
    headers = {'authorization': 'Basic %s' % auth}
    action = "post"
    response = send_request(action, url, data, headers)
    d = json.loads(response)
    v_uri = d["verification_uri_complete"]
    device_code = d["device_code"]
    return [v_uri, device_code]


def get_access_token(device_code):
    logging.info("Fetching Oauth access token")
    cprint("using device code to fetch Oauth Token", "green")
    url = "https://zoom.us/oauth/token?grant_type=urn:ietf:params:oauth:grant-type:device_code&device_code=%s" % device_code
    action = "post"
    auth = basic_auth()
    data = {}
    headers = {'authorization': 'Basic %s' % auth}
    response = send_request(action, url, data, headers)
    data = json.loads(response)
    access_token = data["access_token"]
    cprint("Access Token: %s" % access_token, "blue")
    return access_token


def get_user(access_token):
    logging.info("Fetching User Info")
    cprint("Using Oauth Access token to get user info from REST API", "green")
    url = "https://api.zoom.us/v2/users/me"
    headers = {'authorization': 'Bearer %s' % access_token,
               'content-type': 'application/json'}
    data = {}
    action = "get"
    response = send_request(action, url, data, headers)
    printJSON(response)


def get_users_zak(access_token):
    logging.info("Fetching users Zak Token")
    cprint("Using Oauth Access token to Get users zak", "green")
    url = "https://api.zoom.us/v2/users/me/zak"
    headers = {'authorization': 'Bearer %s' % access_token,
               'content-type': 'application/json'}
    data = {}
    action = "get"
    response = send_request(action, url, data, headers)
    printJSON(response)


def load(fill=0):
    template = ""
    img = [i for i in glob("*.svg")]
    for i in img:
        if fill:
            template += f"<center><img src='{i}' style='width:100%; height:100%'></center>"
        else:
            template += f"<center><img src='{i}'></center>"

    return template


def cleanup():
    logging.info("cleaning up from last session")
    # delete svg file
    os.remove("qr.svg")
    # delete html doc
    os.remove("loader.html")


def oauth_demo():
    html = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta charset="utf-8">
<style>
</style>
    <title></title>
</head>
<body>
<<template>>
</body>
</html>"""
    logging.info("Starting Demo...")
    cprint("Starting Demo", "yellow")
    data = get_verification_uri()
    v_uri = data[0]
    device_code = data[1]
    if qr == True:
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(v_uri, image_factory=factory)
        type(img)  # qrcode.image.pil.PilImage
        img.save("qr.svg")
        html = html.replace("<<template>>", load(fill=0))
        with open("loader.html", "w") as file:
            file.write(html)
            url = "file:// + /Users/JeremyWright/Documents/Projects/Python/Ford_Demo/device_oauth_demo/loader.html"
            webbrowser.open_new(url)
    else:
        webbrowser.open_new(v_uri)
    input("Press Enter to continue...")
    token = get_access_token(device_code)
    input("Press Enter to continue...")
    get_user(token)
    input("Press Enter to continue...")
    get_users_zak(token)
    cleanup()


oauth_demo()
