import pandas as pd


class PullbackDetector:
    @staticmethod
    def is_bullish_pullback(df: pd.DataFrame) -> bool:
        """
        Bullish pullback:
        - EMA9 > EMA15
        - Previous candle touches EMA9
        - Current candle closes above previous high
        """

        if len(df) < 3:
            return False

        prev = df.iloc[-2]
        curr = df.iloc[-1]

        if prev["ema9"] <= prev["ema15"]:
            return False

        touched_ema = prev["low"] <= prev["ema9"] <= prev["high"]
        bullish_break = curr["close"] > prev["high"]

        return touched_ema and bullish_break