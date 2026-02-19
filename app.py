from flask import Flask
from werkzeug.security import generate_password_hash
from extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret-key-123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exam_tracker.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    from models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        from routes import main
        app.register_blueprint(main)
        db.create_all()

        if not User.query.filter_by(email="admin@test.com").first():
            hashed_pw = generate_password_hash("admin123", method='pbkdf2:sha256')
            db.session.add(User(email="admin@test.com", password=hashed_pw))
            db.session.commit()
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)