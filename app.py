from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
	"DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/postgres"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Item(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
	email = db.Column(db.String(80), nullable=False)

with app.app_context():
	db.create_all()

	if not Item.query.first():
		item1 = Item(name="anderson", email="anderson@gmail.com")
		db.session.add_all([item1])
		db.session.commit()
		print("Se agrego un dato inicial a la tabla")

@app.route("/")
def home():
	return jsonify({"message": "Flask Api funcionando con postgreSQL"})

@app.route("/items")
def get_items():
	items = Item.query.all()
	return jsonify([{"id": item.id, "name": item.name, "email": item.email} for item in items])

@app.route("/add_item", methods=["POST"])
def add_item():
	data = request.get_json()
	if "name" not in data or "email" not in data:
		return jsonify({"message": "Error: faltan datos"})
	new_item = Item(name=data["name"], email=data["email"])
	db.session.add(new_item)
	db.session.commit()
	return jsonify({"message": "Se agrego correctamente"}), 201

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)


