#include <iostream>
#include <iomanip>

int main() {
    float msft_price = 356.77f;
    float merc_p1_time = 88.778f; // 1:28.778

    std::cout << "\n[C++] Performance Metrics Initialized..." << std::endl;
    std::cout << ">> Mercedes Lead Margin: " << std::fixed << std::setprecision(3) << merc_p1_time << "s" << std::endl;
    std::cout << ">> MSFT Market Entry: $" << msft_price << std::endl;
    return 0;
}
