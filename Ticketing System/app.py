from flask import Flask
from flask_migrate import Migrate
from flask_session import Session
from routes.blueprint import blueprint
from model.machine import db

def create_app():
    app = Flask(__name__)
    app.secret_key = 'hirayamnl'
    app.config.from_object('config')
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/tixsys"
    app.config['JSON_SORT_KEYS'] = False
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_TYPE'] = "filesystem"

    Session(app)

    with app.test_request_context():
        db.init_app(app)
        
    with app.app_context():
        db.create_all()

    return app

app = create_app()
app.register_blueprint(blueprint, url_prefix='/tixsys')
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)