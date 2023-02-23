from flask import Flask, render_template
print("hola")

app=Flask(__name__)
TITOL="TestWeb"
JOBS=[
	{
	'id':1,
	'title':'Data analyst',
	'ubi':"Balsa",
	'salary':'30k'
	},
	{
	'id':2,
	'title':'Data Scientits',
	'ubi':"Barcelona",
	'salary':'40k'
	},
	{
	'id':3,
	'title':'Frontend dev',
	'ubi':"Remotes",
	'salary':'45k'
	},
	{
	'id':4,
	'title':'Backend dev',
	'ubi':"Navas",
	'salary':None 
	},
]

@app.route("/")

def helloWorld():
	return render_template("home.html",jobs=JOBS,titol=TITOL)

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)