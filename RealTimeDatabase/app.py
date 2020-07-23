import pyrebase
config = {
    apiKey: "AIzaSyDsRWUKzPSNBDWWScXH0nL0n3Sn_CD20xc",
    authDomain: "fir-project-f8aa4.firebaseapp.com",
    databaseURL: "https://fir-project-f8aa4.firebaseio.com",
    projectId: "fir-project-f8aa4",
    storageBucket: "fir-project-f8aa4.appspot.com",
    messagingSenderId: "582440646450",
    appId: "1:582440646450:web:6f529e373403e8d165092b",
    measurementId: "G-TE8BGX11BY"
  };

firebase = pyrebase.initialize_app(config)

db = firebase.database()

from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
	if request.method == 'POST':
		if request.form['submit'] == 'add':

			name = request.form['name']
			db.child("todo").push(name)
			todo = db.child("todo").get()
			to = todo.val()
			return render_template('index.html', t=to.values())
		elif request.form['submit'] == 'delete':
			db.child("todo").remove()
		return render_template('index.html')
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)


