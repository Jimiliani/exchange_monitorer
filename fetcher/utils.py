import requests

from api import models

from monitorer.settings import EXCHANGE_URL


def fetch_open_exchange_rates(from_currency, to_currency):  # BTC USD
    currency, created = models.Cryptocurrency.objects.get_or_create(symbol=to_currency)
    url = EXCHANGE_URL.format(from_currency=from_currency, to_currency=to_currency)
    response = requests.get(url)
    try:
        r = response.json()['Realtime Currency Exchange Rate']
        models.PriceStamp.objects.create(ask_price=r['9. Ask Price'], bid_price=r['8. Bid Price'],
                                         cryptocurrency=currency)
        return 0
    except KeyError as e:
        return 1
