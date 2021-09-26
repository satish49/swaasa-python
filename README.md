# Swaasa-Python API Library

Swaasa-Python library will help you to integrate Swaasa REST API's directly using Object
## Features
- Authorization
- Assessment
- Verion
- Health

## Tech
Tested on Python 3.8

## Installation
Documentation Available here: 

For installation, follow the steps

Extract the tar.gz and perform following commands
 ```sh
 cd swaasa-python
python setup.py install --user
```

And use ```import swaasa``` for integration

## Testing
Created sample app [swaasa-test] with main.py and test_swaasa.py files
To test this, run following
```
pip install -r requirements.txt
python main.py
```

# Update Parametes
Currently all variables hard coded for testing. 

[Login]: emails and password
[Assessment]: sample values mentioned. Change based on your requirement


## Testing URL's
1. Admin login: /adminlogin
   a. returns access token
2. Assessment: /assessment
  a. retures status and assessment id if success
3. Version: /version
  a. returns version of the backend system
4. Health: /health
  a. returns server health


Full API documet available: http://restunited.com/docs/u9h2kmckoexm