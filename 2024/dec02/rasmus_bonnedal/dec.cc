#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>

using namespace std;
using namespace ctl;

struct report {
    vector<int> levels;
};

struct indata {
    vector<report> reports;
};

indata parse(const std::string& filename) {
    indata data;

    for (const auto& s : split(read_file(filename), "\n")) {
        data.reports.push_back({ ctl::map(stoint, split(s, " ")) });
    }
    return data;
}

bool is_grad_inc(const vector<int>& level) {
    int last = level[0] - 1;
    for (const auto& r : level) {
        if (r <= last || (r - last) > 3) {
            return false;
        }
        last = r;
    }
    return true;
}

bool is_grad_dec(const vector<int>& level) {
    int last = level[0] + 1;
    for (const auto& r : level) {
        if (r >= last || (last - r) > 3) {
            return false;
        }
        last = r;
    }
    return true;
}

bool is_grad_inc_dec_tol(const report& rep) {
    if (is_grad_inc(rep.levels)) return true;
    if (is_grad_dec(rep.levels)) return true;
    vector<int> copy;
    int n = (int)rep.levels.size();
    for (int j = 0; j < n; ++j) {
        copy = rep.levels;
        copy.erase(copy.begin() + j);
        if (is_grad_inc(copy) || is_grad_dec(copy)) {
            return true;
        }
    }
    return false;
}

int64_t part1(const indata& data) {
    int64_t result = 0;
    for (const auto& r : data.reports) {
        if (is_grad_inc(r.levels) || is_grad_dec(r.levels)) {
            result++;
        }
        else {
        }
    }
    return result;
}

int part2(const indata& data) {
    int result = 0;

    for (const auto& r : data.reports) {
        if (is_grad_inc_dec_tol(r)) {
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
