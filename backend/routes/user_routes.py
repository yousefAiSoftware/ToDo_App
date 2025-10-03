from flask import Blueprint , request , jsonify , current_app
from werkzeug.security import generate_password_hash , check_password_hash
from models.database import db
from models.user import User
import datetime
import jwt
from config import Config

users_db = Blueprint("users",__name__)

@users_db.route("/register",methods=["POST"])
def register_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error":"Missing data"}),400
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"error":"User already registered, Login? "}),409
    else:
        password_hash = generate_password_hash(password)
        new_user = User(username=username, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"Message" : "User Created Successfully"}),201
    
@users_db.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error":"Missing data"}),400
    existing_user = User.query.filter_by(username=username).first()
    if not existing_user or not check_password_hash(existing_user.password_hash,password):
        return jsonify({"error":"Invalid username or password, check it again."}),401
    payload = { "user_id" : existing_user.id, "exp" : datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)}
    token = jwt.encode(payload,current_app.config["SECRET_KEY"],algorithm="HS256")
    return jsonify({"token" : token})