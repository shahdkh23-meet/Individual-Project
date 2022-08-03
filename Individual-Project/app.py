from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


app = Flask(  
    __name__,
    template_folder='templates',  
    static_folder='static'  

)
app.config['SECRET_KEY'] = 'super-secret-key'



@app.route('/' ,  methods=['GET', 'POST'])# '/' for the default page
def login():
    if request.method == 'POST':
        username2 = request.form['username']
        password2 = request.form['password']
        if username2 == username and password2 == password :
            return redirect(url_for('signin'))
        else:
            return render_template('signin.html')
    else:
        return render_template('signin.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")




@app.route('/', methods=['GET', 'POST'])
def design():
    return render_template("index.html")





@app.route('/fashion')
def fashion():
    return render_template("fashion.html")





if __name__ == '__main__':
    app.run(debug=True)