from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


app = Flask(  
    __name__,
    template_folder='templates',  
    static_folder='static'  

)
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = python3auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('index_tweet'))
        except:
            error = "Authentication failed"
    return render_template("signin.html")


@app.route('/', methods=['GET', 'POST'])
def design():
    return render_template("index.html")







if __name__ == '__main__':
    app.run(debug=True)