#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>
#include <regex>

using namespace std;
using namespace ctl;

struct robot {
    vec2 p, v;
};
using indata = vector<robot>;

indata parse(const std::string& filename) {
    indata d;
    for (const auto& s : split(read_file(filename), "\n")) {
        auto s1 = split(s, " ");
        auto s2 = split(split(s1[0], "=")[1], ",");
        auto s3 = split(split(s1[1], "=")[1], ",");
        d.push_back({ vec2(stoint(s2[0]), stoint(s2[1])), vec2(stoint(s3[0]), stoint(s3[1])) });
    }
    return d;
}

vec2 wrap(vec2 p, vec2 size) {
    while (p.x < 0) {
        p.x += size.x;
    }
    p.x %= size.x;
    while (p.y < 0) {
        p.y += size.y;
    }
    p.y %= size.y;
    return p;
}

void simulate(indata& data, const vec2 map_size) {
    for (auto& rob : data) {
        rob.p = wrap(rob.p + rob.v, map_size);
    }
}

struct def_int {
    int i = 0;
};

int64_t sum_quads(const indata& data, const vec2 map_size) {
    vec2 mid = { map_size.x / 2, map_size.y / 2 };
    map<vec2, def_int> pos;
    for (const auto& rob : data) {
        pos[rob.p].i++;
    }
    int64_t q0 = 0, q1 = 0, q2 = 0, q3 = 0;
    for (const auto& [k, v] : pos) {
        if (k.y < mid.y) {
            if (k.x < mid.x) {
                q0 += v.i;
            }
            else if (k.x > mid.x) {
                q1 += v.i;
            }
        }
        else if (k.y > mid.y) {
            if (k.x < mid.x) {
                q2 += v.i;
            }
            else if (k.x > mid.x) {
                q3 += v.i;
            }
        }
    }
    return q0 * q1 * q2 * q3;
}

int64_t part1(const indata& data) {
    int64_t result = 0;
    const vec2 map_size = (data.size() < 15) ? vec2{ 11, 7 } : vec2{ 101, 103 };
    indata robots = data;
    for (int i = 0; i < 100; i++) {
        simulate(robots, map_size);
    }
    result = sum_quads(robots, map_size);
    return result;
}

bool operator<(vec2 lhs, vec2 rhs) {
    if (lhs.y != rhs.y) {
        return lhs.y < rhs.y;
    }
    return lhs.x < rhs.x;
}

float calc_symmetry2(const indata& robots, const vec2 map_size) {
    vector<vec2> left, right;
    int mid = map_size.x / 2;
    for (const auto& robot : robots) {
        if (robot.p.x < mid) {
            left.push_back(robot.p);
        }
        else {
            right.push_back({ map_size.x - 1 - robot.p.x, robot.p.y });
        }
    }
    sort(left);
    sort(right);
    float diff = 0.0f;
    int li = 0;
    int ri = 0;
    for (int i = 0; i < min(left.size(), right.size()); ++i) {
        vec2 d = left[i] - right[i];
        diff += sqrt(d.x * d.x + d.y * d.y);
    }
    return diff;
}

int64_t part2(const indata& data) {
    int64_t result = 0;
    const vec2 map_size = (data.size() < 15) ? vec2{ 11, 7 } : vec2{ 101, 103 };
    indata robots = data;
    float min_s;

    for (int i = 0; i < 12000; ++i) {
        map_t map;
        for (int y = 0; y < map_size.y; ++y) {
            map.map.push_back(string(map_size.x, '0'));
        }
        for (const auto& rob : robots) {
            map.set(rob.p, map.get(rob.p) + 1);
        }
        float s = calc_symmetry2(robots, map_size);
        if (i == 0) {
            min_s = s;
        }
        if (s < min_s) {
            min_s = s;
            print("New min ({}): {}\n", i, min_s);
            print_map(map);
        }

        //Sleep(200);
        simulate(robots, map_size);
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
