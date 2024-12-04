from flask import Flask, render_template, url_for, request, redirect, session

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
            return redirect('/register')
            
    else:
        return render_template("login.html")
    
@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        print("redirecting")
        return redirect("/")
        # get the form data
        
        # check that it meets requirements
            # try to add to the database
            # catch exception, display error message, return back to 
        
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)


