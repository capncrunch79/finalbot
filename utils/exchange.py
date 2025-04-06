import ccxt
import os

def get_exchange():
    return ccxt.kraken({
        'apiKey': os.getenv("KRAKEN_API_KEY"),
        'secret': os.getenv("KRAKEN_SECRET_KEY")
    })
