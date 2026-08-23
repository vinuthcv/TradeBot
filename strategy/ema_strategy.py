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

        trend = (
            "BULLISH"
            if latest["ema9"] > latest["ema15"]
            else "BEARISH"
        )

        return {
            "trend": trend,
            "ema9": round(latest["ema9"], 2),
            "ema15": round(latest["ema15"], 2),
        }