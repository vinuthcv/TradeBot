from abc import ABC, abstractmethod
import pandas as pd


class MarketDataProvider(ABC):
    @abstractmethod
    def get_candles(self, symbol: str, interval: str) -> pd.DataFrame:
        """Return OHLC candle data."""
        pass