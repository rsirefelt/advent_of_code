#include "ctl.hh"

#include <iostream>

using indata_t = std::vector<int>;

int calc(const indata_t& indata, int turns) {
    // map from number to turn
    std::vector<int> m(turns, 0);

    int turn = 1;
    for (auto x: indata) {
        m[x] = turn++;
    }
    int last = indata.back();
    int next = 0;
    for (; turn <= turns; ++turn) {
        last = next;
        if (m[next] == 0) {
            next = 0;
        } else {
            next = turn - m[next];
        }
        m[last] = turn;
    }
    return last;
}

int main(int argc, char** argv) {
    indata_t indata = {18,8,0,5,4,1,20};
    int part1 = calc(indata, 2020);
    std::cout << "Part 1: " << part1 << std::endl;
    int part2 = calc(indata, 30000000);
    std::cout << "Part 2: " << part2 << std::endl;
    return 0;
}
