#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>
#include <regex>

using namespace std;
using namespace ctl;

using indata = vector<map_t>;

indata parse(const std::string& filename) {
    indata d;
    map_t m;
    for (const auto& s : split(read_file(filename), "\n")) {
        if (s.empty()) {
            if (m.map.size() > 0) {
                d.push_back(m);
                m.map.clear();
            }
        }
        else {
            m.map.push_back(s);
        }
    }
    if (m.map.size() > 0) {
        d.push_back(m);
    }
    return d;
}

bool are_columns_equal(const map_t& data, int x0, int x1) {
    for (int y = 0; y < data.height(); y++) {
        if (data.get(vec2(x0, y)) != data.get(vec2(x1, y))) {
            return false;
        }
    }
    return true;
}

bool is_horiz_reflection(const map_t& data, int y) {
    int y0 = y - 1;
    int y1 = y;

    while (y0 >= 0 && y1 < data.height()) {
        if (data.map[y0] != data.map[y1]) {
            return false;
        }
        y0--;
        y1++;
    }
    return true;
}

bool is_vert_reflection(const map_t& data, int x) {
    int x0 = x - 1;
    int x1 = x;

    while (x0 >= 0 && x1 < data.width()) {
        if (!are_columns_equal(data, x0, x1)) {
            return false;
        }
        x0--;
        x1++;
    }
    return true;
}

int64_t find_reflection(const map_t& data, int skip_x = -1, int skip_y = -1) {
    for (int y = 1; y < data.height(); ++y) {
        if (y != skip_y && is_horiz_reflection(data, y)) {
            return 100 * y;
        }
    }
    for (int x = 1; x < data.width(); ++x) {
        if (x != skip_x && is_vert_reflection(data, x)) {
            return x;
        }
    }
    return 0;
}

int64_t find_reflection_smudge(const map_t& data) {
    int y_refl = -1;
    int x_refl = -1;
    for (int y = 1; y < data.height(); ++y) {
        if (is_horiz_reflection(data, y)) {
            y_refl = y;
        }
    }
    for (int x = 1; x < data.width(); ++x) {
        if (is_vert_reflection(data, x)) {
            x_refl = x;
        }
    }
    for (int y = 0; y < data.height(); ++y) {
        for (int x = 0; x < data.width(); ++x) {
            map_t dcopy = data;
            char c = dcopy.get(vec2(x, y));
            dcopy.map[y][x] = (c == '#') ? '.' : '#';
            int64_t v = find_reflection(dcopy, x_refl, y_refl);
            if (v > 0) {
                return v;
            }
        }
    }
    return 0;
}

int64_t part1(const indata& data) {
    int64_t result = 0;
    for (const auto& m : data) {
        result += find_reflection(m);
    }
    return result;
}

int64_t part2(const indata& data) {
    int64_t result = 0;
    for (const auto& m : data) {
        result += find_reflection_smudge(m);
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
