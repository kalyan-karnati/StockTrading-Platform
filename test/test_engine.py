import os
from trading import create_app

app=create_app()

def test_development_config():
    app.config.from_object('config.DevConfig')
    assert app.config['DEBUG']
    assert app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///stockTrading_db.sqlite3'

def test_production_config():
    app.config.from_object('config.ProdConfig')
    assert not app.config['DEBUG']
    assert not app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///stockTrading_db_prod.sqlite3'