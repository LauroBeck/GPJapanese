def get_msft_intel():
    return {
        "ticker": "MSFT",
        "last_close": 356.77,
        "change_pct": "-2.51%",
        "market_cap": "$2.65T",
        "next_earnings": "2026-04-29",
        "capex_focus": "AI/Azure Infrastructure"
    }

def get_suzuka_pole():
    return {
        "p1": "Kimi Antonelli", "team": "Mercedes", "lap": "1:28.778",
        "p2": "George Russell", "margin": "+0.298s"
    }

m = get_msft_intel()
f = get_suzuka_pole()

print(f"\n[FINANCIAL TELEMETRY] {m['ticker']} Status")
print(f"Price: ${m['last_close']} | Change: {m['change_pct']} | CapEx: $37.5B")
print(f"Strategic Outlook: {m['next_earnings']} Reporting Cycle")
print("-" * 55)
print(f"[RACE DATA] Suzuka Qualifying Results")
print(f"POLE: {f['p1']} ({f['team']}) - Time: {f['lap']}")
print(f"P2  : {f['p2']} (Mercedes) - Delta: {f['margin']}")
