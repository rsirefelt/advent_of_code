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

bool step_north(indata& data) {
    int moves = 0;

    for (int y = 1; y < data.height(); ++y) {
        for (int x = 0; x < data.width(); ++x) {
            char c0 = data.get(vec2(x, y - 1));
            char c1 = data.get(vec2(x, y));
            if (c0 == '.' && c1 == 'O') {
                data.map[y - 1][x] = c1;
                data.map[y][x] = c0;
                moves++;
            }
        }
    }
    return moves > 0;
}

bool step_west(indata& data) {
    int moves = 0;

    for (int x = 1; x < data.width(); ++x) {
        for (int y = 0; y < data.height(); ++y) {
            char c0 = data.get(vec2(x - 1, y));
            char c1 = data.get(vec2(x, y));
            if (c0 == '.' && c1 == 'O') {
                data.map[y][x - 1] = c1;
                data.map[y][x] = c0;
                moves++;
            }
        }
    }
    return moves > 0;
}

bool step_east(indata& data) {
    int moves = 0;

    for (int x = data.width() - 2; x >= 0; --x) {
        for (int y = 0; y < data.height(); ++y) {
            char c0 = data.get(vec2(x + 1, y));
            char c1 = data.get(vec2(x, y));
            if (c0 == '.' && c1 == 'O') {
                data.map[y][x + 1] = c1;
                data.map[y][x] = c0;
                moves++;
            }
        }
    }
    return moves > 0;
}

bool step_south(indata& data) {
    int moves = 0;

    for (int y = data.height() - 2; y >= 0; --y) {
        for (int x = 0; x < data.width(); ++x) {
            char c0 = data.get(vec2(x, y + 1));
            char c1 = data.get(vec2(x, y));
            if (c0 == '.' && c1 == 'O') {
                data.map[y + 1][x] = c1;
                data.map[y][x] = c0;
                moves++;
            }
        }
    }
    return moves > 0;
}

void rotate(indata& data) {
    while (step_north(data));
    while (step_west(data));
    while (step_south(data));
    while (step_east(data));
}

int64_t count(const indata& data) {
    int64_t result = 0;
    int y = data.height();
    for (const auto& row : data.map) {
        result += count(row.begin(), row.end(), 'O') * y--;
    }
    return result;
}

int64_t checksum(const indata& data) {
    int64_t result = 0; {
        for (auto it = data.cbegin(); it != data.cend(); ++it) {
            if (*it == 'O') {
                result += it.pos().x + it.pos().y * data.width();
            }
        }
    }
    return result;
}

int64_t part1(const indata& data) {
    int64_t result = 0;
    indata d = data;
    while (step_north(d));
    result = count(d);
    return result;
}

int64_t part2(const indata& data) {
    map<int64_t, int64_t> cache;
    int64_t result = 0;
    indata d = data;
    const int64_t iters = 1000000000;

    for (int64_t i = 0; i < iters; ++i) {
        rotate(d);
        int64_t cs = checksum(d);
        if (cache.count(cs) > 0) {
            int64_t period = i - cache[cs];
            int64_t iters_left = iters - i - 1;
            if (iters_left % period == 0) {
                return count(d);
            }
        }
        cache[cs] = i;
    }
    result = count(d);
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
