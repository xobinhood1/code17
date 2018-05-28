from flask import Flask, render_template,request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template("index.html")

@app.route('/submit',methods =['POST'])
def disp():

	nam=request.form["name"]
	f = request.files['file']
	f.save(secure_filename(f.filename))
	print(nam)
	lis={nam,f.filename}
	return render_template("page2.html",l=lis)

if __name__ == '__main__':
   app.run(debug=True)