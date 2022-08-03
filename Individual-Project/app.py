from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

Config = {
  "apiKey": "AIzaSyAUPQTMIVupHhftwx1NgpbgcFY93rWyegM",
  "authDomain": "y2-project-b3ffb.firebaseapp.com",
  "projectId": "y2-project-b3ffb",
  "storageBucket": "y2-project-b3ffb.appspot.com",
  "messagingSenderId": "951219977529",
  "appId": "1:951219977529:web:fc1f8b4a10317131ca3ce8",
  "measurementId": "G-XPM1J4KDST",
  "databaseURL":"https://console.firebase.google.com/project/y2-project-b3ffb/database/y2-project-b3ffb-default-rtdb/data/~2F"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


app = Flask(  
    __name__,
    template_folder='templates',  
    static_folder='static'  

)
app.config['SECRET_KEY'] = 'super-secret-key'



@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = python3auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('signin'))
            return render_template("signin.html")





@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        Fullname = request.form['fullname']
        email = request.form['email']
        Name = request.form['name']
        password = request.form['password']
        try:
        login_session['user'] = python3auth.create_user_with_email_and_password(email, password)
        user = {"name": Name, "bio": Bio, "full name": Fullname}
        db.child("user").child(login_session['user']['localId']).set(user)
        return redirect(url_for('index'))
        except:
            error = "Authentication failed"
            return error
    return render_template('signup.html')


@app.route('/signin')
def signin():
    return render_template("signin.html")



@app.route('/fashion')
def fashion():
    return render_template("fashion.html")





if __name__ == '__main__':
    app.run(debug=True)