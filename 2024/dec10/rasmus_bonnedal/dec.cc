#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>
#include <regex>

using namespace std;
using namespace ctl;

using indata = map_t;

indata parse(const std::string& filename) {
    indata d;
    for (const auto& s : split(read_file(filename), "\n")) {
        d.map.push_back(s);
    }
    return d;
}

void _count_paths(const indata& data, const vec2 pos, set<vec2>& goals, int& paths) {
    char cur = data.get(pos);
    if (cur == '9') {
        goals.insert(pos);
        paths++;
        return;
    }
    char cur_next = cur + 1;
    for (dir_t i = UP; i <= RIGHT; i = (dir_t)(i + 1)) {
        vec2 next_pos = step(pos, i);
        if (data.get(next_pos) == cur_next) _count_paths(data, next_pos, goals, paths);
    }
}

int count_paths(const indata& data, const vec2 pos, bool distinct) {
    if (data.get(pos) != '0') return 0;
    int paths = 0;
    set<vec2> goals;
    _count_paths(data, pos, goals, paths);
    return distinct ? paths : (int)goals.size();
}

void print_map(const indata& data) {
    for (auto it = data.cbegin(); it != data.cend(); ++it) {
        print("{}", *it);
        if (it.end_row()) {
            print("\n");
        }
    }
}

int64_t part1(const indata& data) {
    int64_t result = 0;
    for (auto it = data.cbegin(); it != data.cend(); ++it) {
        result += count_paths(data, it.pos(), false);
    }
    return result;
}

int64_t part2(const indata& data) {
    int64_t result = 0;
    for (auto it = data.cbegin(); it != data.cend(); ++it) {
        result += count_paths(data, it.pos(), true);
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
