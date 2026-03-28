teams = {
    "Mercedes": [("A.K. Antonelli", 1, "1:28.778"), ("G. Russell", 2, "1:29.076")],
    "McLaren": [("O. Piastri", 3, "1:29.132"), ("L. Norris", 5, "1:29.409")],
    "Ferrari": [("C. Leclerc", 4, "1:29.405"), ("L. Hamilton", 6, "1:29.567")]
}
print(f"{'TEAM':<12} | {'DRIVER':<18} | {'GRID'}")
print("-" * 40)
for team, drivers in teams.items():
    for name, pos, time in drivers:
        print(f"{team:<12} | {name:<18} | P{pos} ({time})")
