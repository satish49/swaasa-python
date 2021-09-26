from flask import Flask
import swaasa


app = Flask(__name__)
api_client = swaasa.ApiClient()
web_api = swaasa.WebApi(api_client)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

import localswaasa