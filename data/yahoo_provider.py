import yfinance as yf

from data.market_data import MarketDataProvider


class YahooProvider(MarketDataProvider):
    def get_candles(self, symbol: str, interval: str):
        df = yf.download(
            tickers=symbol,
            period="5d",
            interval=interval,
            progress=False,
            auto_adjust=False,
        )

        df = df.rename(columns=str.lower)
        return df