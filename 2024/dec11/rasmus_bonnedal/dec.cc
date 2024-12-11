#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>
#include <regex>

using namespace std;
using namespace ctl;

using indata = vector<uint64_t>;

indata parse(const std::string& filename) {
    indata d;
    for (const auto& s : split(read_file(filename), "\n")) {
        d = mapf(ctl::stoull, split(s, " "));
    }
    return d;
}

bool split_even(uint64_t a, uint64_t& o1, uint64_t& o2) {
    string s = to_string(a);
    if ((s.size() & 1) == 0) {
        size_t len = s.size() / 2;
        o1 = ctl::stoull(s.substr(0, len));
        o2 = ctl::stoull(s.substr(len));
        return true;
    }
    return false;
}

using cache_t = map<pair<uint64_t, int>, uint64_t>;

uint64_t calc(uint64_t v, int level) {
    static cache_t cache;
    auto p = make_pair(v, level);
    if (cache.count(p) > 0) {
        return cache[p];
    }
    if (level == 0) {
        return 1;
    }
    level--;
    uint64_t result = 0;
    uint64_t o1, o2;
    if (v == 0) {
        result += calc(1, level);
    }
    else if (split_even(v, o1, o2)) {
        result += (calc(o1, level) + calc(o2, level));
    }
    else {
        result += calc(v * 2024, level);
    }
    cache[p] = result;
    return result;
}

int64_t part1(const indata& data) {
    int64_t result = 0;
    for (auto v : data) {
        result += calc(v, 25);
    }
    return result;
}

int64_t part2(const indata& data) {
    int64_t result = 0;
    for (auto v : data) {
        result += calc(v, 75);
    }
    return result;
}

void test() {
}

int main(int argc, char** argv) {
    try {
        test();
        auto data = parse("..\\input.txt");
        print("part1: {}\n", part1(data));
        print("part2: {}\n", part2(data));
    }
    catch (const std::exception& e) {
        std::print("Error: {}\n", e.what());
    }
    return 0;
}
