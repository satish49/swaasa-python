from flask import Flask
from pprint import pprint

import swaasa
from swaasa.rest import ApiException


app = Flask(__name__)
api_client = swaasa.ApiClient()
web_api = swaasa.WebApi(api_client)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/adminlogin")
def adminLogin():
    pprint("in adminLogin")
    pprint("set email and password")
    email = "email_id"  # email
    password = "password"  # password

    try:
        pprint("call admin login api")
        # return AdminLogin (model)
        response:AdminLoginAPI = web_api.admin_login(email, password)    

        pprint(response)
        pprint(response.access_token)
        accessToken = response.access_token
        pprint("end of adminLogin")
        return {"status": True, "token": accessToken}

    except ApiException as e:
        pprint("error while calling admin login")
        print(e)
        return {"status": False}


@app.route("/assessment/<accessToken>")
def assessmentTest(accessToken=None):
    # authentication setting using api key/token
    pprint("in assessmentTest")
    pprint("configure inputs")
    pprint("token")
    pprint(accessToken)
    coughsoundfile = "<file location>" #file location
    age = 18  # age
    gender = 1  # gender
    assessment_id = "sample_assessment_id"  # assessmentId
    symptoms = "{\"frequent_cough\":1, \"sputum\":0, \"cough_at_night\":0, \"wheezing\":0, \"pain_in_chest\":0, \"shortness_of_breath\":0}"  # symptoms

    try:
        pprint("call assessment api")
        response = web_api.assessment(coughsoundfile, age, gender, assessment_id, symptoms, access_token=accessToken)
        pprint("print response")
        pprint(response)
        pprint("end of assessmentTest")
        return {"status": True, "assessment_id": response.assessment_id}
    except ApiException as e:
        pprint("error while assessment")
        print(e)
        pprint("end of assessmentTest")
        return {"status": False}

@app.route("/health")
def appHealth():
    try:
        pprint("in appHealth")
        pprint("calling health api")
        response = web_api.health()    

        pprint(response)
        pprint("end of appHealth")
        return {"status": True, "health": response.status}
    except ApiException as e:
        pprint("error while calling health api")
        print(e)
        pprint("end of appHealth")
        return {"status": False}

@app.route("/version")
def appVersion():
    try:
        pprint("in appVersion")
        pprint("call api version")
        response = web_api.version()   

        pprint(response)
        pprint("end of appVersion")
        return {"status": True, "version": response.version, "wavkit":response.wavkit}
    except ApiException as e:
        pprint("error while calling version api")
        print(e)
        pprint("end of appVersion")
        return {"status": False}




