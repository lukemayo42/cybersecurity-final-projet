from flask import Flask, render_template, url_for, request, redirect, session
import re
import random
import string

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        print("helloe")
        # login attempt
        if 'submit' in request.form: 
            # check to see if the username is in the database
            # if the user is in the database, check if the password is correct

                # if username and password are correct
                    # go to index.html
                # else
                    # return to login.html with message saying that password is incorrect
            #else
                #return to login.html saying that username is not in the database:
            print("submit")
            # check to see if the username is in the database
            # if the user is in the database, check if the password is correct

                # if username and password are correct
                    # go to index.html
                # else
                    # return to login.html with message saying that password is incorrect
            #else
                #return to login.html saying that username is not in the database
            return render_template('index.html')
        # register new user
        elif 'register1' in request.form:
            return render_template('login.html')
        
        else:
            print("register!!!")
            return redirect('/register')
            
    else:
        return render_template("login.html")
    
@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        if 'register1' in request.form:
            print("redirecting")
            
            # get the form data
            username:str = request.form.get('username')
            print(username)
            password:str = request.form.get('password')
            c_pass:str = request.form.get('confirm-password')
            if password != c_pass:
                print("ppop")
                return render_template("register.html", message = "passwords do not match")
            # check that it meets requirements
            if len(password) < 8 or len(password) > 25:
                return render_template('register.html', message = "password must be in between 8 and 25 characters long")
            has_letter = bool(re.search(r'[a-zA-Z]', password))
            has_number = has_number = bool(re.search(r'\d', password))
            has_special_char = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
            if not (has_letter and has_number and has_special_char):
                return render_template("register.html", message = "password must contain at least 1 letter, 1 number, and one special character")
                # try to add to the database
                # catch exception, display error message, return back to 
            return redirect("/")
        elif 'strong-password' in request.form:
            print("strong password")
            strong_password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=25))
            return render_template("register.html", strong_password = strong_password)
    return render_template("register.html")

@app.route('/department/<department>')
def department(department):
    return render_template('department.html', department = department)

@app.route("/index")
def index():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)


