import unittest
import requests

from trading import create_app
from trading import db

app=create_app()
db=db.init_app(app)

url="https://3f24-2600-1700-7e0-7f70-f9c3-8666-cff4-9bb9.ngrok.io/"
  