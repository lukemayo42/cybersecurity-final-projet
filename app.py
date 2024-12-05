from flask import Flask, render_template, url_for, request, redirect, session
import re
import random
import string
import hashlib
from setup import run_sql


app = Flask(__name__)
app.secret_key = "not_so_secret_key" # for session

# global varaible to keep track of login attemps
login_attempts = 0
@app.before_request
def setup_counter():
    global counter


@app.route('/', methods = ['POST', 'GET'])
def login():
    global login_attempts
    if request.method == 'POST':
        # login attempt
        if 'submit' in request.form:
            login_attempts += 1 
            print(login_attempts)
            if login_attempts >= 3:
                return render_template('login-limit.html')
            
            assert('username' in request.form)
            # get form data
            username = request.form.get('username')
            password = request.form.get('password')
            print(username)
            print(password)

            # check to see if the username  is in the database
            query = '''SELECT password, access_level FROM users WHERE username = ?'''
            params = (username,)
            data = run_sql(query, params)
            print(data)
            # if the user is in the database, check if the password is correct
            if len(data) > 0:
                #hash the password with the salt from the password in the database
                print(data[0][0])
                salt = data[0][0][:40]  
                stored_hash = data[0][0][40:] 
                hashable = salt + password  # concatenate hash and plain text
                hashable = hashable.encode('utf-8')  # convert to bytes
                this_hash = hashlib.sha1(hashable).hexdigest()  # hash and digest
                
                # if username and password are correct
                # go to index.html
                if this_hash == stored_hash:
                    return render_template('index.html')
                else:
                    return render_template('login.html', message = "incorrect password", login_attempts = login_attempts)
            else:
                return render_template("login.html", message = "username not found", login_attempts = login_attempts)
 
        # register new user
        elif 'register1' in request.form:
            return render_template('login.html', login_attempts = login_attempts)
        
        else:
            return redirect('/register')
            
    else:
        return render_template("login.html", login_attempts = login_attempts)
    
@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        if 'register1' in request.form:
            # register button press
            assert('username' in request.form)
            # get the form data
            username:str = request.form.get('username')
            print(username)
            password:str = request.form.get('password')
            c_pass:str = request.form.get('confirm-password')

            if password != c_pass:
                return render_template("register.html", message = "passwords do not match")
            
            # check that it meets requirements
            if len(password) < 8 or len(password) > 25:
                return render_template('register.html', message = "password must be in between 8 and 25 characters long")
            
            #regex to check if it characters, numbers, and special characters
            has_letter = bool(re.search(r'[a-zA-Z]', password))
            has_number = has_number = bool(re.search(r'\d', password))
            has_special_char = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
            if not (has_letter and has_number and has_special_char):
                return render_template("register.html", message = "password must contain at least 1 letter, 1 number, and one special character")
            
            # hash and salt the password to be stored
            salt = ''.join(random.choices(string.ascii_letters +string.digits, k=40))
            hashable = salt + password
            hashable = hashable.encode('utf-8')
            this_hash = hashlib.sha1(hashable).hexdigest()
            password_hash = salt + this_hash
            # add to the database
            # use parameterized queries to protect from sql injection
            query = ''' INSERT INTO users(username, password, access_level) values (?, ?, ?) '''
            params = (username, password_hash, "technical")
            if run_sql(query, params):
                return render_template("login.html", message = "registered new user")
            else:
                return render_template("register.html", message = "unable to register new user")
            
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


