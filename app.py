from flask import Flask
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template("index.html")

@app.route('/submit',methods =['POST'])
def disp():
	nam=request.form['name']
	f = request.files['file']
	lis={nam,f.filename}
    f.save(secure_filename(f.filename))
    return render_template('show.html',l=lis)

if __name__ == '__main__':
   app.run()