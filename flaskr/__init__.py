import os

from flask import Flask
from .controller import api


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        
        
    )
    if test_config is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    app.register_blueprint(api, url_prefix='/api')
    
    @app.route('/')
    def hello():
        return 'Hello World!'
    
    return app
    