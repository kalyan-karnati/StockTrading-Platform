import unittest
import requests
from apscheduler.schedulers.background import BackgroundScheduler

from trading import create_app
from trading import db

sched = BackgroundScheduler(daemon=True)


url="https://3f24-2600-1700-7e0-7f70-f9c3-8666-cff4-9bb9.ngrok.io/"
