import unittest
import requests

from datetime import datetime
from trading import *
from trading.admin.admin import *
from trading.admin.models import *
from trading.admin.forms import *
from .test_engine import url

class TestAdmin(unittest.TestCase):

    def test_dashboard(self):
         
        marketHoursData = {'startHour': '15:30', 'endHour': '12:30'}
        response = requests.post(url+"dashboard", data=marketHoursData)
        self.assertEqual(response.status_code, 200)
    
    def test_get_market_holidays(self):
         
        response = requests.post(url+"get/market_holidays")
        self.assertEqual(response.status_code, 200)
    
    def test_get_stocks(self):
         
        response = requests.post(url+"get/stocks")
        self.assertEqual(response.status_code, 200)
    
    def test_get_update_stocks(self):
         
        response = requests.post(url+"get/update_stocks")
        self.assertEqual(response.status_code, 200)
    
    def test_changeMarketHours(self):
         
        response = requests.post(url+"changeMarketHours")
        self.assertEqual(response.status_code, 200)
    
    def test_cancel_transaction(self):
         
        response = requests.post(url+"post/delete_holiday/<id>")
        self.assertEqual(response.status_code, 200)
    
    def test_changeMarketHoidays(self):
         
        response = requests.post(url+"/post/changeMarketHolidays")
        self.assertEqual(response.status_code, 200)

if __name__=="__main__":
    unittest.main()
