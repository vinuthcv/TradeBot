import pandas as pd

from indicators.atr import ATRIndicator
from strategy.ema_strategy import EMAStrategy
from strategy.pullback import PullbackDetector


class SignalBuilder:
    def __init__(self):
        self.strategy = EMAStrategy()

    def generate(self, df: pd.DataFrame) -> dict:
        """
        Generates a trading signal with
        - EMA Trend
        - Pullback Detection
        - ATR based SL & Target
        """

        df = df.copy()

        # Calculate EMAs
        df["ema9"] = df["close"].ewm(span=9, adjust=False).mean()
        df["ema15"] = df["close"].ewm(span=15, adjust=False).mean()

        # Calculate ATR
        df = ATRIndicator.calculate(df)

        # EMA Trend
        result = self.strategy.calculate(df)

        # Pullback
        bullish_pullback = PullbackDetector.is_bullish_pullback(df)

        latest = df.iloc[-1]

        atr = float(latest["atr"]) if pd.notna(latest["atr"]) else 0.0
        close = float(latest["close"])

        if bullish_pullback:
            entry = close
            stop_loss = round(entry - atr, 2)
            target = round(entry + (2 * atr), 2)
        else:
            entry = None
            stop_loss = None
            target = None

        result.update({
            "signal": bullish_pullback,
            "atr": round(atr, 2),
            "entry": entry,
            "stop_loss": stop_loss,
            "target": target,
        })

        return result