import json
from termcolor import cprint


def printJSON(data):
    parsed = json.loads(data)
    cprint(json.dumps(parsed, indent=4), "blue")
