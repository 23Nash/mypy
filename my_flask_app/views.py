from flask import Blueprint, request, jsonify, render_template, url_for

bp = Blueprint('main', __name__)

@bp.route('/home')
def home():
    return render_template('home.html')

@bp.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if username == 'admin' and password == 'password':
            return jsonify({"message": "Login successful!", "redirect": url_for('main.home')}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401
    return render_template('login.html')