import json

def get_msft_intel():
    return {
        "ticker": "MSFT",
        "last_close": 356.77,
        "ytd_change": "-24.6%",
        "capex_q2": "$37.5B",
        "next_earnings": "2026-04-29",
        "status": "Correction / High AI Spend"
    }

def get_suzuka_pole():
    return {
        "p1": "Kimi Antonelli", "team": "Mercedes", "lap": "1:28.778",
        "p2": "George Russell", "margin": "+0.298s"
    }

m = get_msft_intel()
f = get_suzuka_pole()

print(f"\n[SYSTEM INTEL] {m['ticker']} Market Entry")
print(f"Price: ${m['last_close']} | YTD: {m['ytd_change']} | CapEx: {m['capex_q2']}")
print(f"Strategic Cycle: {m['next_earnings']} Earnings Target")
print("-" * 60)
print(f"[RACE DATA] 2026 Japanese GP Qualifying")
print(f"POLE: {f['p1']} ({f['team']}) - {f['lap']}")
print(f"P2  : {f['p2']} (Mercedes) - {f['margin']}")
