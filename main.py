from data.yahoo_provider import YahooProvider
from strategy.ema_strategy import EMAStrategy

SYMBOL = "^NSEI"  # NIFTY 50
INTERVAL = "5m"


def main():
    provider = YahooProvider()
    strategy = EMAStrategy()

    print("Fetching market data...")

    df = provider.get_candles(SYMBOL, INTERVAL)

    if df.empty:
        print("No market data received.")
        return

    print(df.columns)
    print(df.tail())

    result = strategy.calculate(df)

    print("\n========== TradeBot ==========")
    print(f"Trend   : {result['trend']}")
    print(f"Close   : {result['close']}")
    print(f"EMA 9   : {result['ema9']}")
    print(f"EMA 15  : {result['ema15']}")
    print(f"BUY     : {result['buy']}")
    print(f"SELL    : {result['sell']}")
    print("===============================")


if __name__ == "__main__":
    main()