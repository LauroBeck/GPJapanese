import json

def get_market_data():
    return {
        "ticker": "MSFT",
        "price": 356.78,
        "ytd_return": "-24.0%",
        "quarterly_capex": "$37.5B",
        "next_earnings": "2026-04-29"
    }

def get_grid_data():
    return [
        {"pos": 1, "driver": "A.K. Antonelli", "team": "Mercedes", "status": "POLE"},
        {"pos": 2, "driver": "G. Russell", "team": "Mercedes", "status": "FRONT ROW"},
        {"pos": 4, "driver": "C. Leclerc", "team": "Ferrari", "status": "ROW 2"}
    ]

market = get_market_data()
grid = get_grid_data()

print(f"\n[MARKET TELEMETRY] {market['ticker']} @ ${market['price']}")
print(f"AI Infrastructure Spend: {market['quarterly_capex']} | Next Report: {market['next_earnings']}")
print("-" * 60)
print(f"{'GRID':<5} | {'DRIVER':<18} | {'TEAM':<12} | {'STRATEGY'}")
for d in grid:
    print(f"P{d['pos']:<4} | {d['driver']:<18} | {d['team']:<12} | {d['status']}")
