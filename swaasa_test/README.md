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
Download Swaasa-Python library from [http://files1.restunited.com/libraries/traceplus_sandbox_swaasa_ai_064900/dev/0/0/2/sw/Swaasa-dev-0.0.2-python.tar.gz]

Extract the tar.gz and perform following commands
 ```sh
 cd Swaasa-python
python setup.py install --user
```
## Testing
Created sample app with main.py and test_swaasa.py files
To test this, run following
```
pip install -r requirements.txt
python main.py
```

# Set Parameters
Login: emails and password
Assessment: sample values mentioned. Change based on your requirement


## Testing URL's
1. Admin login: /adminlogin
   a. It returns access token
2. Assessment: /assessment
  a. all parameters hard coded. You need to update
  b. it will return status and assessment id if success
3. Version /version
4. Health /health


Full API documet available: http://restunited.com/docs/u9h2kmckoexm