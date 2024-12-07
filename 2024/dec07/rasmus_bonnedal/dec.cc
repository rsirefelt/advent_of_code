#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>
#include <regex>

using namespace std;
using namespace ctl;

struct line {
    int64_t result;
    vector<int64_t> values;
};

struct indata {
    vector<line> lines;
};

indata parse(const std::string& filename) {
    indata d;
    for (const auto& s : split(read_file(filename), "\n")) {
        auto v = split(s, ":");
        d.lines.push_back(line{ ctl::stoll(v[0]), ctl::map(ctl::stoll, split(v[1], " ")) });
    }
    return d;
}

bool has_solution(int64_t sum, int index, const line& line) {
    if (index == line.values.size()) {
        return sum == line.result;
    }
    if (index == 0) {
        return has_solution(line.values[index], index + 1, line) ||
            has_solution(line.values[index], index + 1, line);
    }
    else {
        return has_solution(sum * line.values[index], index + 1, line) ||
            has_solution(sum + line.values[index], index + 1, line);
    }
}

int64_t combine(int64_t v, int64_t v2) {
    int64_t x = ctl::stoll(to_string(v) + to_string(v2));
    //print("combine({}, {}) = {}\n", v, v2, x);
    return x;
}

bool has_solution3(int64_t sum, int index, const line& line) {
    if (index == line.values.size()) {
        return sum == line.result;
    }
    if (index == 0) {
        return has_solution3(line.values[index], index + 1, line);
    }
    else {
        return has_solution3(sum * line.values[index], index + 1, line) ||
            has_solution3(sum + line.values[index], index + 1, line) ||
            has_solution3(combine(sum, line.values[index]), index + 1, line);
    }
}

int64_t part1(const indata& data) {
    int64_t result = 0;
    for (const auto& line : data.lines) {
        if (has_solution(0, 0, line)) {
            result += line.result;
        }
    }
    return result;
}

int64_t part2(const indata& data) {
    int64_t result = 0;
    for (const auto& line : data.lines) {
        if (has_solution3(0, 0, line)) {
            result += line.result;
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
