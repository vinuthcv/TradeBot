import yfinance as yf

from data.market_data import MarketDataProvider


class YahooProvider(MarketDataProvider):

    def get_candles(self, symbol: str, interval: str):
        df = yf.download(
            symbol,
            period="5d",
            interval=interval,
            progress=False,
            auto_adjust=False,
        )

        # Flatten MultiIndex columns if present
        if hasattr(df.columns, "levels"):
            df.columns = df.columns.get_level_values(0)

        # Lowercase column names
        df.columns = [c.lower() for c in df.columns]

        return df