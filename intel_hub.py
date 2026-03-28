import json

def get_msft_intel():
    return {
        "ticker": "MSFT",
        "last_close": 356.77,
        "change_pct": "-2.51%",
        "capex_q2": "$37.5B",
        "next_earnings": "2026-04-29 (Est.)",
        "ai_infrastructure_focus": "Azure & Copilot Scaling"
    }

def get_suzuka_grid():
    return [
        {"p": 1, "driver": "A.K. Antonelli", "team": "Mercedes", "time": "1:28.778"},
        {"p": 2, "driver": "G. Russell", "team": "Mercedes", "time": "1:29.076"},
        {"p": 4, "driver": "C. Leclerc", "team": "Ferrari", "time": "1:29.405"}
    ]

m = get_msft_intel()
g = get_suzuka_grid()

print(f"\n[SYSTEM INTEL] {m['ticker']} Portfolio Status")
print(f"Price: ${m['last_close']} ({m['change_pct']}) | CapEx: {m['capex_q2']}")
print(f"Strategic Outlook: {m['ai_infrastructure_focus']}")
print("-" * 55)
print(f"{'POS':<4} | {'CONSTRUCTOR':<12} | {'DRIVER':<18} | {'LAP'}")
for d in g:
    print(f"P{d['p']:<3} | {d['team']:<12} | {d['driver']:<18} | {d['time']}")
