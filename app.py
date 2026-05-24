from flask import Flask, render_template, request, jsonify
from forms import RegistrationForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.'
# store the database in an object 
db = SQLAlchemy(app)
# create a table
class User(db.Model):
    # column creation 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return f'User {self.username}'

class ShippingInfo(db.Model):
    ship_id = db.Column(
        db.Integer,
        primary_key=True)
    full_name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"))

    def __repr__(self):
    	return f"{self.full_name}'s address is {self.address}."

with app.app_context():
    db.create_all()
    db.session.commit()


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
    json_data = request.get_json()
    user_match = User.query.filter_by(username=json_data['uname']).first()
    if user_match:
        return jsonify({'Message': 'User already exists!'})

    new_user = User(username = json_data['uname'], password = json_data['pword'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'Message': 'A new user was created!'}) 
@app.route("/admin", methods=["GET"])
def admin():
    users = User.query.all()
    shippers = ShippingInfo.query.all()
    return render_template("admin.html", users=users, shippers=shippers)