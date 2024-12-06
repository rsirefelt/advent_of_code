#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>
#include <regex>

using namespace std;
using namespace ctl;

struct vec2 {
    int x, y;
};

enum dir {
    UP,
    RIGHT,
    DOWN,
    LEFT
};

struct indata {
    vector<string> visited;
    vector<string> map;
    int width, height;
};

dir turn_right(dir d) {
    if (d == UP) return RIGHT;
    if (d == RIGHT) return DOWN;
    if (d == DOWN) return LEFT;
    if (d == LEFT) return UP;
    throw runtime_error("Invalid direction");
}

vec2 step(const vec2 p, const dir d) {
    if (d == UP) return vec2(p.x, p.y - 1);
    if (d == RIGHT) return vec2(p.x + 1, p.y);
    if (d == DOWN) return vec2(p.x, p.y + 1);
    if (d == LEFT) return vec2(p.x - 1, p.y);
    throw runtime_error("Invalid direction");
}

// return true if step outside
bool next_pos(vec2& p, dir& d, const indata& data) {
    vec2 p_next = step(p, d);
    if (p_next.x < 0 || p_next.y < 0 || p_next.x >= data.width || p_next.y >= data.height) {
        return true;
    }
    if (data.map[p_next.y][p_next.x] == '#') {
        d = turn_right(d);
    }
    else {
        p = p_next;
    }
    return false;
}

indata parse(const std::string& filename) {
    indata d;
    for (const auto& s : split(read_file(filename), "\n")) {
        d.map.push_back(s);
        d.visited.push_back(string(s.size(), ' '));
    }
    d.width = (int)d.map[0].size();
    d.height = (int)d.map.size();
    return d;
}

vec2 find_pos(const indata& d) {
    for (int y = 0; y < d.height; ++y) {
        for (int x = 0; x < d.width; ++x) {
            char c = d.map[y][x];
            if (c == '^') return vec2(x, y);
        }
    }
    throw runtime_error("Pos not found");
}

int count_visited(const indata& d) {
    int result = 0;
    for (int y = 0; y < d.height; ++y) {
        for (int x = 0; x < d.width; ++x) {
            if (d.visited[y][x] == 'X') result++;
        }
    }
    return result;
}

int64_t part1(const indata& data) {
    indata d = data;

    vec2 pos = find_pos(d);
    dir dr = UP;
    do {
        d.visited[pos.y][pos.x] = 'X';
    } while (!next_pos(pos, dr, d));

    return count_visited(d);
}

int64_t part2(const indata& data) {
    int64_t result = 0;

    const vec2 start_pos = find_pos(data);
    for (int y = 0; y < data.height; ++y) {
        for (int x = 0; x < data.width; ++x) {
            if (data.map[y][x] != '.') continue;
            indata d = data;
            d.map[y][x] = '#';
            vec2 pos = start_pos;
            dir dr = UP;
            int steps = 0;
            while (true) {
                if (next_pos(pos, dr, d)) {
                    break;
                }
                if (pos.x == start_pos.x && pos.y == start_pos.y && dr == UP) {
                    result++;
                    break;
                }
                // Probably a loop, lol
                if (steps > 10000) {
                    result++;
                    break;
                }
                steps++;
            }
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
