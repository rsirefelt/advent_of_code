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
    vector<string> table;
    int width;
    int height;

    char get(vec2 v) const {
        if (v.x < 0 || v.x >= width || v.y < 0 || v.y >= height) {
            return '.';
        }
        return table[v.y][v.x];
    }

};

indata parse(const std::string& filename) {
    indata d;
    for (const auto& s : split(read_file(filename), "\n")) {
        d.table.push_back(s);
    }
    d.width = (int)d.table[0].size();
    d.height = (int)d.table.size();
    return d;
}

bool is_col_empty(const indata& data, int col) {
    for (int y = 0; y < data.height; ++y) {
        if (data.get(vec2(col, y)) == '#') {
            return false;
        }
    }
    return true;
}

bool is_row_empty(const indata& data, int row) {
    for (int x = 0; x < data.width; ++x) {
        if (data.get(vec2(x, row)) == '#') {
            return false;
        }
    }
    return true;
}

int64_t distance(vec2 a, vec2 b) {
    return abs(a.x - b.x) + abs(a.y - b.y);
}

vector<vec2> get_pairs(const indata& data) {
    vector<vec2> pairs;
    for (int y = 0; y < data.height; y++) {
        for (int x = 0; x < data.width; x++) {
            vec2 v(x, y);
            if (data.get(v) == '#') {
                pairs.push_back(v);
            }
        }
    }
    return pairs;
}

int64_t sum_pairs(const vector<vec2>& pairs) {
    int64_t result = 0;
    for (int i = 0; i < pairs.size(); ++i) {
        for (int j = (i + 1); j < pairs.size(); ++j) {
            result += distance(pairs[i], pairs[j]);
        }
    }
    return result;
}

void expand(const indata& data, vector<vec2>& points, int64_t times) {
    for (int y = (data.height - 1); y >= 0; --y) {
        if (is_row_empty(data, y)) {
            for (auto& p : points) {
                if (p.y > y) {
                    p.y += (times - 1);
                }
            }
        }
    }
    for (int x = (data.width - 1); x >= 0; --x) {
        if (is_col_empty(data, x)) {
            for (auto& p : points) {
                if (p.x > x) {
                    p.x += (times - 1);
                }
            }
        }
    }
}

int64_t part1(const indata& data) {
    auto points = get_pairs(data);
    expand(data, points, 2);
    return sum_pairs(points);
}

int64_t part2(const indata& data) {
    auto points = get_pairs(data);
    expand(data, points, 1000000);
    return sum_pairs(points);
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
