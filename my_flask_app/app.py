from flask import Flask
from flask_cors import  CORS
from views import bp as main_bp

app = Flask(__name__, template_folder='templates')
CORS(app)

app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)

