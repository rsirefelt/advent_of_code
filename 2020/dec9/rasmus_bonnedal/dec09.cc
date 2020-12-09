#include "ctl.hh"

#include <iostream>

using intvec = std::vector<int64_t>;

intvec parse(const std::string& filename) {
    return map(stol, split(read_file(filename), "\n"));
}

bool check_sum1(const intvec& v, int ix) {
    for (int i = 0; i < 25; ++i) {
        for (int j = 0; j < 25; ++j) {
            if (i == j) continue;
            if (v[ix-i-1] + v[ix-j-1] == v[ix]) return true;
        }
    }
    return false;
}

bool check_sum2(const intvec& v, int ix, int num, int& endrange) {
    int64_t sum = 0;
    for (endrange = ix; endrange < v.size(); ++endrange) {
        sum += v[endrange];
        if (sum == num && endrange > ix) return true;
        if (sum > num) return false;
    }
    return false;
}

int main(int argc, char** argv) {
    auto indata = parse("input");

    int64_t part1;
    for (int i = 25; i < indata.size(); ++i) {
        if (!check_sum1(indata, i)) {
            part1 = indata[i];
            break;
        }
    }

    int64_t part2;
    for (int i = 0; i < indata.size(); ++i) {
        int endrange;
        if (check_sum2(indata, i, part1, endrange)) {
            auto v = slice(indata, i, endrange + 1);
            part2 = min(v) + max(v);
            break;
        }
    }

    std::cout << "Part 1: " << part1 << std::endl;
    std::cout << "Part 2: " << part2 << std::endl;
    return 0;
}
