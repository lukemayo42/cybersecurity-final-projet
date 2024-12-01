from flask import Flask, render_template, url_for, request, redirect, session

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        return render_template('index.html')
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)