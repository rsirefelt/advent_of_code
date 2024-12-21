#define _CRT_SECURE_NO_WARNINGS
#include "ctl.hh"

#include <chrono>
#include <ctime>
#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>
#include <regex>
#include <unordered_set>

using namespace std;
using namespace ctl;


struct indata {
    vector<vec2> coords;
};

indata parse(const std::string& filename) {
    indata d;
    for (const auto& s : split(read_file(filename), "\n")) {
        auto v = mapf(stoint, split(s, ","));
        d.coords.push_back({ v[0], v[1] });
    }
    return d;
}

void find_closest(map_t& map, intmap& intmap, vec2 pos, int steps) {
    if (!intmap.isinside(pos) || map.get(pos) == '#') {
        return;
    }
    int& v = intmap.get(pos);
    if (v != -1 && v <= steps) {
        return;
    }
    v = steps;
//    map.set(pos, 'X');
//    print_map(map);
    map.set(pos, 'o');
    for (auto dir : DIRS) {
        find_closest(map, intmap, step(pos, dir), steps + 1);
    }
}

void fill(const indata& d, map_t& map, intmap& intmap, int coordslow, int coordshigh) {
    vec2 size;
    size_t coords;
    
    if (d.coords.size() > 100) {
        size = vec2(71, 71);
        coords = coordshigh;
    }
    else {
        size = vec2(7, 7);
        coords = coordslow;
    }
    map.init(size, '.');
    intmap.init(size, -1);

    for (size_t i = 0; i < coords; ++i) {
        map.set(d.coords[i], '#');
    }
}

int64_t part1(const indata& data) {
    int64_t result = 0;
    map_t map;
    intmap intmap;
    fill(data, map, intmap, 12, 1024);
    find_closest(map, intmap, vec2(70, 70), 0);
    result = intmap.get({ 0, 0 });
    return result;
}

vec2 part2(const indata& data) {
    int64_t result = 0;
    map_t map;
    for (int i = 2048; i < (int)data.coords.size(); ++i) {
        intmap intmap;
        fill(data, map, intmap, 12, i);
        find_closest(map, intmap, vec2(70, 70), 0);
        if (intmap.get({ 0, 0 }) == -1) {
            return data.coords[i - 1];
        }
    }
    return{ -1, -1 };
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
