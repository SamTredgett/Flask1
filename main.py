''' short backend project '''
from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "secret_key"
@app.route("/")
def home():
    ''' the home function renders the index.html view, the basic landing page '''
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"]) 
def login():
    if request.method == "POST":
        user = request.form["nm"] 
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("login.html")

@app.route("/user") 
def user():
    ''' the user function simply returns a users name that is added posted by 
        the login function.'''
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>" 
    else:
        return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug=True)

