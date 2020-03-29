from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    from app.link.views import link_bp
    app.register_blueprint(link_bp, url_prefix='/link')

    from app.models import SQLHelper
    db_manager = SQLHelper()

    @app.route('/')
    def index_page():
        return render_template('index.html')

    return app







