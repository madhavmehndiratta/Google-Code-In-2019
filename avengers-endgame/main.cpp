#include "bits/stdc++.h"
#include <iostream>
#include <cmath>

int main(){
std::ios_base::sync_with_stdio(0);
std::cin.tie(nullptr);
long long n;
std::cin >> n;

while (n--)
{
    double power;
    std::cin >> power;
    double x;
    x = (-1 + std::sqrt(1 + 2 * power)) / 2;

    if (x == floor(x))
        x--;

    x = floor(x);
    long long DAYS = (x * (4 + 4 * x)) / 2;
    long long d = 4 + (x) * 4;

    if (DAYS <= power && power <= DAYS + d / 2)
        std::cout << "IRON MAN\n";

    else
        std::cout << "CAPTAIN AMERICA\n";
}

return 0;
}
