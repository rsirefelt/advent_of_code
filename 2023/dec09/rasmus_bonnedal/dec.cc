#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>

using namespace std;
using namespace ctl;

struct indata {
    vector<vector<int>> values;
};

indata parse(const std::string& filename) {
    indata data;
    for (const auto& s : split(read_file(filename), "\n")) {
        data.values.push_back(ctl::map(stoint, split(s, " ")));
    }
    return data;
}

int part1(const indata& data) {
    int i = 0;
    for (const auto& v : data.values) {
        vector<int> cur = v;
        vector<int> next;
        int sum = 0;
        bool all_zeros;
        do {
            all_zeros = true;
            for (int i = 0; i < (cur.size() - 1); ++i) {
                int x = cur[i + 1] - cur[i];
                if (x) {
                    all_zeros = false;
                }
                next.push_back(x);
            }
            sum += cur.back();
            cur = next;
            next = {};
        } while (!all_zeros);
        i += sum;
    }
    return i;
}

// -966 not right
// 20244 too high
// 966

int part2(const indata& data) {
    int i = 0;
    for (const auto& v : data.values) {
        vector<int> cur = v;
        vector<int> next;
        int sum = 0;
        bool all_zeros;
        int sign = 1;
        do {
            all_zeros = true;
            for (int i = 0; i < (cur.size() - 1); ++i) {
                int x = cur[i + 1] - cur[i];
                if (x) {
                    all_zeros = false;
                }
                next.push_back(x);
            }
            sum += sign * cur.front();
            cur = next;
            next = {};
            sign = -sign;
        } while (!all_zeros);
        i += sum;
    }
    return i;
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
