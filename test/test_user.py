import unittest
import requests

from datetime import datetime
from trading import *
from trading.user.user import *
from trading.user.models import *
from trading.user.forms import *
from .test_engine import app

class TestUser(unittest.TestCase):

    def test_dashboard(self):
        tester = app.test_client(self)
        marketHoursData = {'startHour': '15:30', 'endHour': '12:30'}
        response = requests.post("http://127.0.0.1:80/userdashboard", data=marketHoursData)
        self.assertEqual(response.status_code, 200)
        response = requests.get("http://127.0.0.1:80/userdashboard")
        self.assertEqual(response.status_code, 200)

    def test_transaction_history(self):
        tester = app.test_client(self)
        response = requests.get("http://127.0.0.1:80/transaction_history")
        self.assertEqual(response.status_code, 200)
    
    def test_get_portfolio(self):
        tester = app.test_client(self)
        response = requests.get("http://127.0.0.1:80/get/portfolio")
        self.assertEqual(response.status_code, 200)
    
    def test_cancel_transaction(self):
        tester = app.test_client(self)
        response = requests.post("http://127.0.0.1:80/post/cancel_transaction/<tranid>")
        self.assertEqual(response.status_code, 200)
    
    def test_cash(self):
        tester = app.test_client(self)
        response = requests.post("http://127.0.0.1:80/cash")
        self.assertEqual(response.status_code, 200)
    
    def test_cashDeposit(self):
        tester = app.test_client(self)
        response = requests.post("http://127.0.0.1:80/cashDeposit")
        self.assertEqual(response.status_code, 200)
    
    def test_cashWithdraw(self):
        tester = app.test_client(self)
        response = requests.post("http://127.0.0.1:80/cashWithDraw")
        self.assertEqual(response.status_code, 200)
    
    def test_viewstocks(self):
        tester = app.test_client(self)
        response = requests.post("http://127.0.0.1:80/ViewStocks")
        self.assertEqual(response.status_code, 200)
    
    def test_buy_sell(self):
        tester = app.test_client(self)
        response = requests.post("http://127.0.0.1:80/buy_sell")
        self.assertEqual(response.status_code, 200)

