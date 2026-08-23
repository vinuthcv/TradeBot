import pandas as pd


class EMAStrategy:
    def __init__(self, fast=9, slow=15):
        self.fast = fast
        self.slow = slow

    def calculate(self, df: pd.DataFrame):
        """
        Expects DataFrame with:
        open, high, low, close
        """

        df = df.copy()

        df["ema9"] = df["close"].ewm(span=self.fast, adjust=False).mean()
        df["ema15"] = df["close"].ewm(span=self.slow, adjust=False).mean()

        latest = df.iloc[-1]

        ema9 = float(latest["ema9"])
        ema15 = float(latest["ema15"])
        close = float(latest["close"])

        trend = "BULLISH" if ema9 > ema15 else "BEARISH"

        return {
            "trend": trend,
            "ema9": round(ema9, 2),
            "ema15": round(ema15, 2),
            "close": round(close, 2),
            "buy": ema9 > ema15,
            "sell": ema9 < ema15,
        }