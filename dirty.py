import pandas as pd
import ccxt
from pathlib import Path
from tenacity import retry, retry_if_exception_type

OHLC_COLUMNS = ['open', 'high', 'low', 'close']
OHLCV_COLUMNS = ['open', 'high', 'low', 'close', 'volume']
OHLCVD_COLUMNS = ['open', 'high', 'low', 'close', 'volume', 'date']
DOHLCV_COLUMNS = ['date', 'open', 'high', 'low', 'close', 'volume']

EXCHANGE = 'GDAX'

@retry(retry=retry_if_exception_type(AssertionError))
def get_dataframe():
    exchange = ccxt.gdax()
    ohlcv = exchange.fetch_ohlcv('BTC/USD', '1d')
    assert len(ohlcv) == 300
    df = pd.DataFrame(ohlcv, columns=DOHLCV_COLUMNS)
    df['date'] = pd.to_datetime(df['date'], unit='ms')
    df = df.set_index('date')
    return df

def get_pickle():
    return pd.read_pickle('gdax_btc.pickle')
