import unittest
import requests

from datetime import datetime
from trading import *
from trading.errors.errors import *
from test_engine import app
from test_engine import url

class Testerrors(unittest.TestCase):

    def test_error_400(self):
        tester = app.test_client(self)
        response = requests.post(url+"/error_400.html")
        self.assertEqual(response.status_code, 200)
    
    def test_error_404(self):
        tester = app.test_client(self)
        response = requests.post(url+"/error_404.html")
        self.assertEqual(response.status_code, 200)
    
    def test_error_403(self):
        tester = app.test_client(self)
        response = requests.post(url+"/error_403.html")
        self.assertEqual(response.status_code, 200)
    
    def test_error_503(self):
        tester = app.test_client(self)
        response = requests.post(url+"/error_503.html")
        self.assertEqual(response.status_code, 200)
    
    def test_error_500(self):
        tester = app.test_client(self)
        response = requests.post(url+"/error_500.html")
        self.assertEqual(response.status_code, 200)


