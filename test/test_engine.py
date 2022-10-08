import unittest
import requests

from trading import create_app
from trading import db

app=create_app()
db=db.init_app(app)
  