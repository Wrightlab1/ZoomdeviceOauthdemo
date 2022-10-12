# PYTHON Device OAuth Demo

## Installation
Clone this project
```
git clone LINKHERE
```
Install dependencies
```
pip install -r requirements.txt
```

## Usage
This project is a demo of the Device oauth implimentation

You will need to create a ```.env``` file  in the root of the project with the following
```
LOGGING_LEVEL=DEBUG
CLIENTID = ""
CLIENTSECRET = ""
```
LOGGING_LEVEL must be an  upper-case string and can be set to INFO, DEBUG, or WARNING

## Logging
A logfile is generate for you in ``` ./logs/log.log```
This logfile will contain all of the information you need to debug your Zoom REST API requests