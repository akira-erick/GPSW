from flask import Flask
from modules.projects import projects_bp
from modules.candidates import candidates_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(projects_bp)
    app.register_blueprint(candidates_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)