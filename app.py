from flask import Flask, render_template;

app = Flask(__name__);

@app.route("/", methods=["GET"])

def welcome():
    return render_template("home.html", name = "Parker" )

@app.route("/about", methods=["GET"])

def about():
    return render_template("about.html")

@app.route("/shop", methods=["GET"])
def shop():
    cart= ["12oz Medium Roast", "24oz French Roast", "96oz Whole Beans"]
    return render_template("shop.html", cart=cart)
@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")
