from flask import Flask, render_template, url_for, request, redirect, session

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        print("helloe")
        if 'submit' in request.form and request.form['submit'] == 'Submit':
            print("submit")
            return render_template('index.html')
        else:
            redirect('/register')

        #check to see what button they pressed, submit or register new user
        #if submit is pressed
            # check to see if the username is in the database
            # if the user is in the database, check if the password is correct

                # if username and password are correct
                    # go to index.html
                # else
                    # return to login.html with message saying that password is incorrect
            #else
                #return to login.html saying that username is not in the database
        return render_template('index.html')
    else:
        return render_template("login.html")
    
@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)