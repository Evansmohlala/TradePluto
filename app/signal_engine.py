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

        try:

            data = yf.download(
                symbol,
                period="5d",
                interval="1h",
                progress=False
            )

            # Skip empty data
            if data.empty:
                results.append({
                    "market": name,
                    "price": "N/A",
                    "signal": "NO DATA"
                })
                continue

            close_prices = data["Close"]

            # Convert Series safely
            if hasattr(close_prices, "values"):
                close_prices = close_prices.values.flatten()

            if len(close_prices) < 10:
                results.append({
                    "market": name,
                    "price": "N/A",
                    "signal": "NO DATA"
                })
                continue

            latest_price = float(close_prices[-1])

            fast_ma = sum(close_prices[-5:]) / 5
            slow_ma = sum(close_prices[-10:]) / 10

            signal = "NO TRADE"

            if fast_ma > slow_ma:
                signal = "BUY"

            elif fast_ma < slow_ma:
                signal = "SELL"

            results.append({
                "market": name,
                "price": round(latest_price, 2),
                "signal": signal
            })

        except Exception as e:

            results.append({
                "market": name,
                "price": "ERROR",
                "signal": "ERROR"
            })

    return results
