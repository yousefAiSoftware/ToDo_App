from functools import wraps
from flask import jsonify , request , current_app
import jwt
from models.user import User





def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' not in request.headers:
            return jsonify({'message': 'Authorization header is missing!'}), 401
        try:
            auth_header = request.headers['Authorization'] # {"Authorization" : "Bearer y7246u28693jtk"} the letters after Bearer is the token we needed so i will split them 
            split_auth_value = auth_header.split(" ")
            token = split_auth_value[1]
        except IndexError:
            return jsonify({'message': 'Malformed token format!'}), 401
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.get(data['user_id'])
            if current_user is None:
                return jsonify({'message': 'User with this token not found! , Register Now?'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated