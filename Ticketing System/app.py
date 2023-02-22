from flask import Flask
from flask_migrate import Migrate
from routes.blueprint import blueprint
from model.machine import db

def create_app():
    app = Flask(__name__, template_folder="view/templates")
    
    app.config.from_object('config')

    with app.test_request_context():
        db.init_app(app)
        
    with app.app_context():
        db.create_all()

    return app

app = create_app()
app.register_blueprint(blueprint, url_prefix='/auth')
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)