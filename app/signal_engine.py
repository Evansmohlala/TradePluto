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

            if data.empty:

                results.append({
                    "market": name,
                    "price": "N/A",
                    "signal": "NO DATA"
                })

                continue

            closes = data["Close"].tolist()

            if len(closes) < 10:

                results.append({
                    "market": name,
                    "price": "N/A",
                    "signal": "NO DATA"
                })

                continue

            latest_price = closes[-1]

            fast_ma = sum(closes[-5:]) / 5
            slow_ma = sum(closes[-10:]) / 10

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

        except Exception:

            results.append({
                "market": name,
                "price": "ERROR",
                "signal": "ERROR"
            })

    return results
