#include <iostream>
#include <iomanip>

int main() {
    double msft_volatility = 0.34;
    double merc_lap_time = 88.778; // 1:28.778 in seconds

    std::cout << "\n[C++] Engineering & Asset Correlation:" << std::endl;
    std::cout << "Mercedes P1 Delta: " << std::fixed << std::setprecision(3) << merc_lap_time << "s" << std::endl;
    std::cout << "MSFT Risk Premium: " << (msft_volatility * 100) << "%" << std::endl;
    return 0;
}
