import unittest
import requests

from datetime import datetime
from trading import *
from trading.user.user import *
from trading.user.models import *
from trading.user.forms import *
from .test_engine import url

class TestUser(unittest.TestCase):

    def test_dashboard(self):
         
        marketHoursData = {'startHour': '15:30', 'endHour': '12:30'}
        response = requests.post(url+"/userdashboard", data=marketHoursData)
        self.assertEqual(response.status_code, 200)
        response = requests.get(url+"/userdashboard")
        self.assertEqual(response.status_code, 200)

    def test_transaction_history(self):
         
        response = requests.get(url+"/transaction_history")
        self.assertEqual(response.status_code, 200)
    
    def test_get_portfolio(self):
         
        response = requests.get(url+"/get/portfolio")
        self.assertEqual(response.status_code, 200)
    
    def test_cancel_transaction(self):
         
        response = requests.post(url+"/post/cancel_transaction/<tranid>")
        self.assertEqual(response.status_code, 200)
    
    def test_cash(self):
         
        response = requests.post(url+"/cash")
        self.assertEqual(response.status_code, 200)
    
    def test_cashDeposit(self):
         
        response = requests.post(url+"/cashDeposit")
        self.assertEqual(response.status_code, 200)
    
    def test_cashWithdraw(self):
         
        response = requests.post(url+"/cashWithDraw")
        self.assertEqual(response.status_code, 200)
    
    def test_viewstocks(self):
         
        response = requests.post(url+"/ViewStocks")
        self.assertEqual(response.status_code, 200)
    
    def test_buy_sell(self):
         
        response = requests.post(url+"/buy_sell")
        self.assertEqual(response.status_code, 200)

if __name__=="__main__":
    unittest.main()
