import unittest
import requests

from datetime import datetime
from trading import *
from trading.errors.errors import *
from .test_engine import app

class Testerrors(unittest.TestCase):

    def test_error_400(self):
        tester = app.test_client(self)
        response = requests.post("http://127.0.0.1:80/error_400.html")
        self.assertEqual(response.status_code, 200)
    
    def test_error_404(self):
        tester = app.test_client(self)
        response = requests.post("http://127.0.0.1:80/error_404.html")
        self.assertEqual(response.status_code, 200)
    
    def test_error_403(self):
        tester = app.test_client(self)
        response = requests.post("http://127.0.0.1:80/error_403.html")
        self.assertEqual(response.status_code, 200)
    
    def test_error_503(self):
        tester = app.test_client(self)
        response = requests.post("http://127.0.0.1:80/error_503.html")
        self.assertEqual(response.status_code, 200)
    
    def test_error_500(self):
        tester = app.test_client(self)
        response = requests.post("http://127.0.0.1:80/error_500.html")
        self.assertEqual(response.status_code, 200)


