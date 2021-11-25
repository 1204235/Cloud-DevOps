from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello Airbus"

if __name__ == "__main__":
	app.run(host ='18.205.19.222', port = 5001, debug = True)
