from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello Airbus"


if __name__ == "__main__":
	app.run(host ='3.222.113.74', port = 5001, debug = True)
