from flask import Flask, render_template, url_for, redirect, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "gigachad"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chads.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form['submit-btn'] == 'sign-up':
            user = request.form["nm"]
            uname = request.form["uname"]
            pwd = request.form["pwd"]            

            if(user != "" and user != "" and pwd != ""):
                chad = users(name=user, username=uname, password=pwd)
                db.session.add(chad)
                db.session.commit()

                flash("Sign-Up Succcesful")
                return redirect(url_for("login"))
            else:
                flash("riempi tutti i campi")
                return redirect(url_for("login"))
            
        elif request.form['submit-btn'] == 'login':
            uname = request.form["unm"]
            pwd = request.form["pass"]            
            
            if (uname != "" and pwd != ""):
                found_user = users.query.filter_by(username=uname).first()
                if(found_user.username == uname and found_user.password == pwd):
                    session["username"] = uname
                    session["password"] = pwd 
                    return redirect(url_for("home"))  
                else:
                    flash("Username o password sbagliata.")
                    return render_template("login.html")                            
            else:
                flash("Riempi tutti i campi.")
                return render_template("login.html")             
    else:
        if "username" in session:
            flash("You are already logged in")
            return redirect(url_for("view"))

        return render_template("login.html")  

@app.route("/view")
def view():
        return render_template("view.html", values=users.query.all())

@app.route("/logout")
def logout():
    #found_user = users.query.filter_by(username='').first() #per eliminare un campo dal database
    #db.session.delete(found_user)
    #db.session.commit()
    session.pop("username", None)
    session.pop("password", None)
    return redirect(url_for("login"))

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

if __name__ =="__main__":
    db.create_all()
    app.run(debug=True)