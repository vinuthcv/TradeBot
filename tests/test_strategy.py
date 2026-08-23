import pandas as pd

from strategy.ema_strategy import EMAStrategy


def test_ema_strategy():
    data = {
        "open":  [100,101,102,103,104,105,106,107,108,109],
        "high":  [101,102,103,104,105,106,107,108,109,110],
        "low":   [99,100,101,102,103,104,105,106,107,108],
        "close": [100,101,102,103,104,105,106,107,108,109],
    }

    df = pd.DataFrame(data)

    strategy = EMAStrategy()

    result = strategy.calculate(df)

    print(result)


if __name__ == "__main__":
    test_ema_strategy()