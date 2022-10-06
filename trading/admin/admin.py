import json
from datetime import datetime

import pandas as pd
from flask import Blueprint, render_template, make_response, request, jsonify, redirect, url_for
from flask_login import login_required
from sqlalchemy import extract
from sqlalchemy.exc import IntegrityError

from .forms import CreateStock, UpdateMarketHours, CreateMarketHolidays
from .models import Stocks, db, MarketHours, MarketHolidays

# Blueprint Configuration
admin_bp = Blueprint(
    'admin_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/admin'
)


@admin_bp.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    error = ''
    form = CreateStock()
    marketHoursform = UpdateMarketHours()
    marketHolidaysform = CreateMarketHolidays()
    stocksData = Stocks.query
    marketHours = MarketHours.query.first()
    marketHoursData = {'startHour': marketHours.startHour.time(), 'endHour': marketHours.endHour.time()}
    if request.method == 'POST':
        if form.validate_on_submit():
            stock = Stocks(
                companyName=form.companyName.data,
                ticker=form.ticker.data,
                volume=form.volume.data,
                initialPrice=form.initialPrice.data,
                currentPrice=form.initialPrice.data,
                openPrice=0,
                dayHigh=0,
                dayLow=form.initialPrice.data,
                lastTradedDay=datetime(1990, 1, 1, 0, 0, 0, 0)
            )
            db.session.add(stock)
            try:
                db.session.commit()
            except IntegrityError:
                error = 'Company Name or stock ticker already exists'
                db.session.rollback()

    return render_template("/dashboard.html", error=error, form=form, stocks=stocksData, marketHours=marketHoursData,
                           marketHoursform=marketHoursform, marketHolidaysform=marketHolidaysform)
