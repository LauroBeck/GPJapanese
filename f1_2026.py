grid = [
    {"driver": "A.K. Antonelli", "team": "Mercedes", "pos": 1, "time": "1:28.778"},
    {"driver": "G. Russell", "team": "Mercedes", "pos": 2, "time": "1:29.076"},
    {"driver": "O. Piastri", "team": "McLaren", "pos": 3, "time": "1:29.132"},
    {"driver": "C. Leclerc", "team": "Ferrari", "pos": 4, "time": "1:29.405"},
    {"driver": "L. Norris", "team": "McLaren", "pos": 5, "time": "1:29.409"},
    {"driver": "L. Hamilton", "team": "Ferrari", "pos": 6, "time": "1:29.567"}
]

print(f"{'POS':<4} | {'DRIVER':<18} | {'TEAM':<12} | {'TIME'}")
print("-" * 50)
for d in grid:
    print(f"{d['pos']:<4} | {d['driver']:<18} | {d['team']:<12} | {d['time']}")
