#include <iostream>
#include <iomanip>
int main() {
    std::cout << "\n[C++ Output] Starting Grid Top 3:\n";
    std::cout << std::left << std::setw(15) << "Mercedes:" << "P1 Antonelli / P2 Russell" << std::endl;
    std::cout << std::left << std::setw(15) << "McLaren:" << "P3 Piastri / P5 Norris" << std::endl;
    std::cout << std::left << std::setw(15) << "Ferrari:" << "P4 Leclerc / P6 Hamilton" << std::endl;
    return 0;
}
