from strategy.ema_strategy import EMAStrategy
from strategy.pullback import PullbackDetector


class SignalBuilder:
    def __init__(self):
        self.strategy = EMAStrategy()

    def generate(self, df):
        result = self.strategy.calculate(df)

        # Calculate EMAs on the DataFrame so pullback can use them
        df = df.copy()
        df["ema9"] = df["close"].ewm(span=9, adjust=False).mean()
        df["ema15"] = df["close"].ewm(span=15, adjust=False).mean()

        bullish_pullback = PullbackDetector.is_bullish_pullback(df)

        return {
            **result,
            "signal": bullish_pullback,
        }