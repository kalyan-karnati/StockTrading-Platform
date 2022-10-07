import random
from datetime import datetime

from sqlalchemy import extract, or_, and_

from .. import scheduler
from ..admin.models import db, Stocks, MarketHours, MarketHolidays
from ..auth.models import User
from ..user.models import StockTransaction, LimitTransaction, Portfolio, CashTransaction
from ..user.user import isMarketOpen


def create_market_settings_data():
    if len(MarketHours.query.all()) == 0:
        data = MarketHours(
            startHour=datetime(2022, 3, 28, 9, 30, 0, 0),
            endHour=datetime(2022, 3, 28, 16, 0, 0, 0)
        )
        db.session.add(data)
        db.session.commit()

    # data2 = MarketHolidays(
    #     day=datetime(2022, 3, 28)
    # )
    # db.session.add(data2)
    # db.session.commit()


@scheduler.task('interval', id='job_1', seconds=5, misfire_grace_time=900)
def job1():
    with scheduler.app.app_context():
        current_date = datetime.now()
        market_hours = MarketHours.query.all()
        market_holidays = MarketHolidays.query.with_entities(MarketHolidays.day).filter(
            extract('month', MarketHolidays.day) == current_date.month,
            extract('day', MarketHolidays.day) == current_date.day).all()
        # MarketHolidays.query.with_entities(MarketHolidays.day).filter(
        # extract('month', MarketHolidays.day) >= datetime.today().month,
        # func.extract('dow', MarketHolidays.day) == 6).all()

        # check for weekday, check for time in market hours, check for if today is one of the market holidays
        if current_date.weekday() < 5 and market_hours[0].startHour.time() <= current_date.time() <= market_hours[
            0].endHour.time() and len(market_holidays) == 0:

            inc = random.choice([True, False])
            if inc:
                val = random.uniform(0.0155, 0.795)
            else:
                val = random.uniform(0.0155, 1.295)
            stocks = Stocks.query
            # stocks.update(
            #     dict(currentPrice=Stocks.currentPrice + (val * Stocks.id) if inc else Stocks.currentPrice - (val*Stocks.id),
            #          ))
            for stock in stocks:
                if not inc and round(stock.currentPrice - (val * stock.id), 3) < 0.001:
                    stock.currentPrice = round(stock.currentPrice + (val * stock.id), 3)
                else:
                    stock.currentPrice = round(stock.currentPrice + (val * stock.id), 3) if inc else round(
                        stock.currentPrice - (val * stock.id), 3)
                priceTriggers(stock, current_date)
            db.session.commit()
            print("Stock Price Update at - ", current_date)
        elif not current_date.weekday() < 5:
            print("Stock Market Closed on Weekends")
        elif not market_hours[0].startHour.time() <= current_date.time() <= market_hours[0].endHour.time():
            print("Stock Market open only in admin specified hours")
        else:
            print("Stock Market is closed today as a holiday")


def update_transaction_status(tran_id, status, log):
    new = StockTransaction.query.filter(StockTransaction.id == tran_id).update(
        {StockTransaction.status: status, StockTransaction.log: log, StockTransaction.updatedDateTime: datetime.now()})
    db.session.commit()


def update_cash_transaction(userID, transaction_type, amount, is_credit):
    tran = CashTransaction(
        userID=userID,
        transactionType=transaction_type,
        amount=amount if is_credit else -amount,
        dateTime=datetime.now()
    )
    db.session.add(tran)
    db.session.commit()

