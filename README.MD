# PYTHON ZOOM REST API SCRIPT TEMPLATE

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
CLIENTID = "l70mg2aVQRib9JDww4yD2Q"
CLIENTSECRET = "9WmVQ1N7e4Go1WGafL9nGJMJcAtmUzhS"
```
LOGGING_LEVEL must be an  upper-case string and can be set to INFO, DEBUG, or WARNING

## Logging
A logfile is generate for you in ``` ./logs/log.log```
This logfile will contain all of the information you need to debug your Zoom REST API requests