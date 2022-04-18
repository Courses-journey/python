from flask import Flask,render_template

# every app should have a uniqe name
kottab_app = Flask(__name__)

# setup rounting
@kottab_app.route("/")
def homepage():
    return render_template("home.html",pagetitle="Hellop")

@kottab_app.route("/about")
def aboutpage():
    return render_template("about.html")

# run app if this file run directly
if __name__ == "__main__":
    kottab_app.run(debug=True)