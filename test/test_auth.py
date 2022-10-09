import unittest
import requests

from datetime import datetime
from trading import *
from trading.auth.auth import *
from trading.auth.models import *
from trading.auth.forms import *
from .test_engine import url

class TestAuth(unittest.TestCase):

    def test_signup(self):
        response = requests.post(url+"/signup")
        self.assertEqual(response.status_code, 200)
    
    def test_login(self):
        response = requests.post(url+"/")
        self.assertEqual(response.status_code, 200)
    
    def test_logout(self):
        response = requests.post(url+"/logout")
        self.assertEqual(response.status_code, 200)