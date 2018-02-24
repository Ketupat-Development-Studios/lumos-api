import os
import pyrebase
from flask import Flask
from config import FIREBASE_CONFIG
from api.device_blueprint import construct_device_blueprint
from api.area_blueprint import construct_area_blueprint
from api.action_blueprint import construct_action_blueprint

app = Flask(__name__)
firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
database = firebase.database()

app.register_blueprint(construct_device_blueprint(database))

app.register_blueprint(construct_area_blueprint(database))
app.register_blueprint(construct_action_blueprint(database))


# lumos-web
@app.route('/', methods=['GET'])
def serve_lumos_web_index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=os.environ.get('DEBUG', True)
    )
