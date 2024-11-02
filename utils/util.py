from flask import request, jsonify
from datetime import datetime, timedelta
import jwt
import os
from dotenv import load_dotenv
from functools import wraps

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

def encode_token(user_id, role_names):
    payload = {
        'exp': datetime.now() + timedelta(days=1),
        'iat': datetime.now(),
        'sub': user_id,
        'role': role_names
    }
    token = jwt.encode(payload,SECRET_KEY,algorithm= 'HS256')
    return token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split(' ')[1]
                print("Token:", token)
                payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token has expired', 'error': 'Unauthorized' })
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalic token', 'error': 'Unauthorized'})
        if not token:
            return jsonify({'message': 'Authentication token is missing', 'error': 'Unauthorized'})
        
        return f(*args, **kwargs)
    
    return decorated

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = None
            if 'Authorization' in request.headers:
                token = request.headers['Authorization'].split(" ")[1]
            if not token:
                return jsonify({'message': 'token is missing'}), 401
            
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            except jwt.ExpiredSignatureError:
                return jsonify({'message': "token has expired"}), 401
            except jwt.InvalidTokenError:
                return jsonify({'message', 'invalid token'}), 401
            
            roles = payload["role"]

            if role not in roles:
                return jsonify({'message': 'User does not have the required role'}), 403
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator