#!/bin/bash

# 1. Create Python Script (Mercedes / McLaren / Ferrari)
cat << 'EOF' > f1_2026.py
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
EOF

# 2. Create C++ Source (Mercedes / McLaren / Ferrari)
cat << 'EOF' > f1_2026.cpp
#include <iostream>
#include <iomanip>
#include <vector>

struct Entry { std::string d; std::string t; int p; };

int main() {
    std::vector<Entry> top = {
        {"A.K. Antonelli", "Mercedes", 1},
        {"G. Russell", "Mercedes", 2},
        {"O. Piastri", "McLaren", 3}
    };
    std::cout << "\n[C++] Top 3 Qualifiers - Suzuka 2026\n";
    for(const auto& e : top) 
        std::cout << "P" << e.p << ": " << std::left << std::setw(15) << e.d << " (" << e.t << ")\n";
    return 0;
}
EOF

# 3. Create C Source (Mercedes / McLaren / Ferrari)
cat << 'EOF' > f1_2026.c
#include <stdio.h>

int main() {
    printf("\n[C] Scored Grid Status:\n");
    printf("P1: Antonelli (MER) | P4: Leclerc (FER) | P6: Hamilton (FER)\n");
    return 0;
}
EOF

# --- Execution Block ---
echo "Executing F1 Grid Data (2026 Japanese GP)..."
echo "-------------------------------------------"

# Run Python
python3 f1_2026.py

# Compile and Run C++
g++ f1_2026.cpp -o f1_cpp && ./f1_cpp

# Compile and Run C
gcc f1_2026.c -o f1_c && ./f1_c

# Cleanup binary files
rm f1_cpp f1_c
