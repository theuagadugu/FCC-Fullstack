from flask import Flask
print("hola")

app=Flask(__name__)

@app.route("/")

def helloWorld():
	return "<p> hello worlds</p>"

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)