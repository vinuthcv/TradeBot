from data.yahoo_provider import YahooProvider
from strategy.ema_strategy import EMAStrategy
from strategy.signal_builder import SignalBuilder

SYMBOL = "^NSEI"  # NIFTY 50
INTERVAL = "5m"


def main():
    provider = YahooProvider()
    builder = SignalBuilder()

    print("Fetching market data...")

    df = provider.get_candles(SYMBOL, INTERVAL)

    if df.empty:
        print("No market data received.")
        return

    print(df.columns)
    print(df.tail())

    result = builder.generate(df)    

    print("\n========== TradeBot ==========")
    print(f"Trend      : {result['trend']}")
    print(f"Close      : {result['close']}")
    print(f"EMA 9      : {result['ema9']}")
    print(f"EMA 15     : {result['ema15']}")
    print(f"ATR        : {result['atr']}")
    print(f"BUY        : {result['buy']}")
    print(f"SELL       : {result['sell']}")
    print(f"Signal     : {result['signal']}")

    if result["signal"]:
        print(f"Entry      : {result['entry']}")
        print(f"Stop Loss  : {result['stop_loss']}")
        print(f"Target     : {result['target']}")

    print("===============================")

    


if __name__ == "__main__":
    main()