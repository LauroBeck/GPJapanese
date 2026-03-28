#include <iostream>
#include <random>
#include <iomanip>
#include <cmath>

int main() {
    double start_price = 356.77;
    double volatility = 0.3536; 
    int sims = 100000;
    double total = 0;

    std::random_device rd;
    std::mt19937 gen(rd());
    std::normal_distribution<> d(0.0002, volatility / sqrt(252));

    for(int i = 0; i < sims; ++i) {
        total += start_price * exp(d(gen));
    }

    std::cout << "\n[C++] Monte Carlo Projection (n=" << sims << ")" << std::endl;
    std::cout << ">> MSFT Projected Mean: $" << std::fixed << std::setprecision(2) << (total / sims) << std::endl;
    return 0;
}
