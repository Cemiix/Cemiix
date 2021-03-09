from flask import Flask

web = Flask(__name__)

@web.route("/")
def home():
	return "ok"
  
web.run(host="0.0.0.0")
