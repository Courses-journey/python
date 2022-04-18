from flask import Flask

# every app should have a uniqe name
kottab_app = Flask(__name__)

# setup rounting
@kottab_app.route("/")
def homepage():
    return "Kottab Home"

@kottab_app.route("/about")
def aboutpage():
    return "Kottab About"

# run app if this file run directly
if __name__ == "__main__":
    kottab_app.run(debug=True)