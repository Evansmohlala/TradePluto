import yfinance as yf

markets = {
    "BTC-USD": "BTC-USD",
    "GOLD": "GC=F",
    "EURUSD": "EURUSD=X",
    "GBPUSD": "GBPUSD=X"
}

def get_signals():

    results = []

    for name, symbol in markets.items():

        data = yf.download(symbol, period="2d", interval="15m")

        data['MA_FAST'] = data['Close'].rolling(5).mean()
        data['MA_SLOW'] = data['Close'].rolling(10).mean()

        latest_fast = data['MA_FAST'].iloc[-1]
        latest_slow = data['MA_SLOW'].iloc[-1]

        latest_price = float(data['Close'].iloc[-1])

        signal = "NO TRADE"

        if latest_fast > latest_slow:
            signal = "BUY"

        elif latest_fast < latest_slow:
            signal = "SELL"

        results.append({
            "market": name,
            "price": round(latest_price, 2),
            "signal": signal
        })

    return results
