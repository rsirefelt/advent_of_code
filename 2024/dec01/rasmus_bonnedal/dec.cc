#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>

using namespace std;
using namespace ctl;

struct indata {
    vector<int64_t> lhs, rhs;
};

indata parse(const std::string& filename) {
    indata data;
    for (const auto& s : split(read_file(filename), "\n")) {
        auto v = ctl::map([](const string& s) {return std::stoll(s); }, split(s, " "));
        data.lhs.push_back(v[0]);
        data.rhs.push_back(v[1]);
    }
    return data;
}

int64_t part1(const indata& data) {
    int64_t result = 0;
    auto lhs = sorted(data.lhs);
    auto rhs = sorted(data.rhs);
    for (int i = 0; i < lhs.size(); ++i) {
        result += abs(lhs[i] - rhs[i]);
    }
    return result;
}

struct count_t {
    int64_t i = 0;
};

int part2(const indata& data) {
    int result = 0;
    std::map<int64_t, count_t> hist;
    for (auto i : data.rhs) {
        hist[i].i++;
    }
    for (auto i : data.lhs) {
        result += i * hist[i].i;
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
