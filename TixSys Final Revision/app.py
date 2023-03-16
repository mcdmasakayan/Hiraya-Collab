from flask import Flask
from flask_migrate import Migrate
from flask_sessionstore import Session
from routes.blueprint import bp
from model.init_db import db
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    Session(app)
    CORS(app)
    
    with app.test_request_context():
        db.init_app(app)
        
    with app.app_context():
        db.create_all()

    return app

app = create_app()
app.register_blueprint(bp, url_prefix='/tixsys')
Migrate(app, db)

if __name__ == '__main__':
    app.run()