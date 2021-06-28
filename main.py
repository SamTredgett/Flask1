''' short backend project utilising Flask '''
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "secret_key"
app.permanent_session_lifetime = timedelta(days=1)

@app.route("/")
def home():
    ''' the home function renders the index.html view, the basic landing page '''
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    ''' login handles the POST and GET HTTP method requests for the form '''
    if request.method == "POST":
        session.permanent = True
        current_user = request.form["nm"]
        session["user"] = current_user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    ''' the user function simply returns a users name that is added posted by
        the login function.'''
    if "user" in session:
        current_user = session["user"]
        return f"<h1>{current_user}</h1>"
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    ''' removes user from the session data on the client side '''
    session.pop("user",None)
    flash("You have been successfully logged out", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
