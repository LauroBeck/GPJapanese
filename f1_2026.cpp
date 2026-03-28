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
