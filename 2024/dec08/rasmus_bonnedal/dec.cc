#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>
#include <regex>

using namespace std;
using namespace ctl;

struct vec2 {
    int64_t x, y;
};

struct indata {
    vector<string> map;
};

indata parse(const std::string& filename) {
    indata d;
    for (const auto& s : split(read_file(filename), "\n")) {
        d.map.push_back(s);
    }
    return d;
}

using pairs = std::map<char, vector<vec2>>;

pairs get_pairs(const indata& data) {
    pairs ps;
    for (int64_t y = 0; y < (int64_t)data.map.size(); ++y) {
        for (int64_t x = 0; x < (int64_t)data.map[y].size(); ++x) {
            char c = data.map[y][x];
            if (c != '.') {
                ps[c].push_back(vec2(x, y));
            }
        }
    }
    return ps;
}

using result_map = vector<string>;

vec2 operator+(const vec2& lhs, const vec2& rhs) {
    return vec2(lhs.x + rhs.x, lhs.y + rhs.y);
}

vec2 operator-(const vec2& lhs, const vec2& rhs) {
    return vec2(lhs.x - rhs.x, lhs.y - rhs.y);
}

result_map init_result(const indata& data) {
    return result_map(data.map.size(), string(data.map[0].size(), '.'));
}

bool set_char(result_map& res_map, const vec2& pos, char c) {
    if (pos.x >= 0 && pos.y >= 0 && pos.x < (int64_t)res_map[0].size() && pos.y < (int64_t)res_map.size()) {
        res_map[pos.y][pos.x] = c;
        return true;
    }
    return false;
}

void find_pairs(const vector<vec2>& pairs, result_map& res_map) {
    for (int i = 0; i < pairs.size(); ++i) {
        for (int j = i + 1; j < pairs.size(); j++) {
            vec2 a = pairs[i];
            vec2 b = pairs[j];
            vec2 diff = b - a;
            vec2 antinode_1 = b + diff;
            vec2 antinode_2 = a - diff;
            set_char(res_map, antinode_1, '#');
            set_char(res_map, antinode_2, '#');
        }
    }
}
void find_pairs_2(const vector<vec2>& pairs, result_map& res_map) {
    for (int i = 0; i < pairs.size(); ++i) {
        for (int j = i + 1; j < pairs.size(); j++) {
            vec2 a = pairs[i];
            vec2 b = pairs[j];
            vec2 diff = b - a;
            vec2 antinode_1 = b;
            vec2 antinode_2 = a;
            while (set_char(res_map, antinode_1, '#')) {
                antinode_1 = antinode_1 + diff;
            }
            while (set_char(res_map, antinode_2, '#')) {
                antinode_2 = antinode_2 - diff;
            }
        }
    }
}



int64_t count_map(const result_map& res_map) {
    int64_t result = 0;
    for (const auto& row : res_map) {
        for (char c : row) {
            if (c == '#') {
                result++;
            }
        }
    }
    return result;
}

int64_t part1(const indata& data) {
    int64_t result = 0;
    auto ps = get_pairs(data);
    auto res_map = init_result(data);
    for (const auto& [k, v] : ps) {
        find_pairs(v, res_map);
    }
    result = count_map(res_map);
    return result;
}

int64_t part2(const indata& data) {
    int64_t result = 0;
    auto ps = get_pairs(data);
    auto res_map = init_result(data);
    for (const auto& [k, v] : ps) {
        find_pairs_2(v, res_map);
    }
    result = count_map(res_map);
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
