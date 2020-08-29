# flask
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# env
from os.path import join, dirname
from dotenv import load_dotenv

# modules
from modules.auth import auth_module
from modules.truck import truck_module

app = Flask(__name__)
app.register_blueprint(auth_module, url_prefix='/auth')
app.register_blueprint(truck_module, url_prefix='/truck')

# load env vars
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app.config.from_object("config")
CORS(app)
jwt = JWTManager(app)

# test route
@app.route("/test")
def test():
    return {"message":"wellcome"}
    
if __name__ == '__main__':

    from db import db
    db.init_app(app)
    app.run(debug=True)