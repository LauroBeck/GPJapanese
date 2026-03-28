def get_intel():
    return {
        "ticker": "MSFT",
        "price": 356.77,
        "ytd": "-24.6%",
        "fx_pair": "USD/JPY",
        "fx_rate": 159.48,
        "fx_alert_level": 160.00,
        "p1_driver": "Kimi Antonelli",
        "p1_team": "Mercedes-AMG",
        "p1_time": "1:28.778"
    }

d = get_intel()
print(f"\n[SYSTEM INTEL] MSFT @ ${d['price']} | USD/JPY @ {d['fx_rate']}")
print(f"Suzuka Pole: {d['p1_driver']} ({d['p1_team']}) - {d['p1_time']}")
