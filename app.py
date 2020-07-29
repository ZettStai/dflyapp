# Zett Stai
# DFly is a software development platform that enables developers to seamlessly develop and deploy their applications to public cloud. For now, dfly offers its PaaS on AWS. To develop applications on dfly, it is expected that developers are familiar with Kubernetes ecosystem and basic usage of kubectl.
#**************************|**************************|**************************|**************************

#1. Candidate can develop their web applications on Java/NodeJS/Python/Golang or any programming language of their chouce. The purpose of that web application is to show the message "Welcome to Dragonfly" on the browser (It can be Nginx or Apache)

from flask import Flask

# create an app instance
app = Flask(__name__)

# Define end point

@app.route("/")
def welcome():
	return "Welcome to Dfly"

if __name__ == "__main__":
# Run flask app. This is where you can also enable debugging as one of the arguments to the run function.
	app.run()


