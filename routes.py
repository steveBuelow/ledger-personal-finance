from flask import request, session, jsonify, render_template
from datetime import datetime, timedelta
import psycopg2
from db import get_db
from models import *

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/signup', methods=['POST'])
    def signup():
        data = request.get_json()
        try:
            create_user(data.get('username'), data.get('password'))
            return jsonify({"message": "Account created successfully!"}), 201
        except psycopg2.IntegrityError:
            return jsonify({"error": "User exists"}), 409
        
    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        user_id = find_user(data.get('username'), data.get('password'))
        if user_id:
            session.permanent = True
            session['user_id'] = user_id
            return jsonify({"status": "Logged in successfully!"}), 200
        return jsonify({"error": "Invalid login, please check credentials!"}), 401
    
