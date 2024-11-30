#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>

using namespace std;
using namespace ctl;

struct indata {
    vector<int> times;
    vector<int> distances;
    uint64_t t1;
    uint64_t d1;
};

indata parse(const std::string& filename) {
    indata data;
    auto s = split(read_file(filename), "\n");
    data.times = ctl::map(stoint, split(split(s[0], ":")[1], " "));
    data.distances = ctl::map(stoint, split(split(s[1], ":")[1], " "));
    data.t1 = ctl::stoull(filter(split(s[0], ":")[1], [](char c) { return c != ' '; }));
    data.d1 = ctl::stoull(filter(split(s[1], ":")[1], [](char c) { return c != ' '; }));
    return data;
}

int part1(const indata& data) {
    int result = 1;
    int races = (int)data.times.size();

    for (int i = 0; i < races; ++i) {
        int ways = 0;
        int time = data.times[i];
        int distance = data.distances[i];
        for (int t = 0; t < time; ++t) {
            int d = (time - t) * t;
            if (d > distance) {
                ways++;
            }
        }
        result *= ways;

    }
    return result;
}

int part2(const indata& data) {
    int result = 0;
    for (uint64_t t = 0; t < data.t1; ++t) {
        uint64_t d = (data.t1 - t) * t;
        if (d > data.d1) {
            result++;
        }
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
