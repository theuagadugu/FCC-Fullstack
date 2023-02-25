from flask import Flask, render_template, jsonify
import MySQLdb
import ssl
import os
from database import load_jobs_from_db
print("hola")

app=Flask(__name__)
TITOL="TestWeb"


@app.route("/")
def helloWorld():
	return render_template("home.html",jobs=load_jobs_from_db(),titol=TITOL)

@app.route("/api/jobs") #així és crea una api
def list_jobs():
	return(jsonify(load_jobs_from_db()))



if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)