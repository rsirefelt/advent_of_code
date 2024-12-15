#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>
#include <regex>

using namespace std;
using namespace ctl;

struct indata {
    map_t map;
    string instructions;
};

indata parse(const std::string& filename) {
    indata d;
    for (const auto& s : split(read_file(filename), "\n")) {
        if (in("v", s)) {
            d.instructions.append(s);
        }
        else if (!s.empty()) {
            d.map.map.push_back(s);
        }
    }
    return d;
}

vec2 find_pos(const map_t& map) {
    for (auto it = map.cbegin(); it != map.cend(); ++it) {
        if (*it == '@') {
            return it.pos();
        }
    }
    throw runtime_error("Couldn't find @");
}

dir_t get_dir(char c) {
    if (c == '<') return LEFT;
    if (c == '>') return RIGHT;
    if (c == '^') return UP;
    if (c == 'v') return DOWN;
    throw runtime_error("Could find direction of " + c);
}

int64_t sum_gps(const map_t& map) {
    int64_t sum = 0;
    for (auto it = map.cbegin(); it != map.cend(); ++it) {
        if (*it == 'O' || *it == '[') {
            sum += it.pos().x + it.pos().y * 100;
        }
    }
    return sum;
}

map_t convert_map(const map_t& map) {
    map_t result;
    for (const auto& row: map.map) {
        string s;
        for (char c : row) {
            if (c == '#') {
                s.append("##");
            }
            else if (c == 'O') {
                s.append("[]");
            }
            else if (c == '.') {
                s.append("..");
            }
            else if (c == '@') {
                s.append("@.");
            }
            else {
                throw runtime_error("Unknown char " + c);
            }
        }
        result.map.push_back(s);
    }
    return result;
}

// Check if possible to move. Move if ok
bool check_push(map_t& map, vec2 pos1, vec2 pos2, dir_t dir, bool only_try) {
    if (map.get(pos1) != '[' || map.get(pos2) != ']') return false;
    if (dir == LEFT) {
        vec2 p1 = step(pos1, dir);
        char c = map.get(p1);
        if (c == '.' || (c == ']' && check_push(map, step(p1, dir), p1, dir, only_try))) {
            if (!only_try) {
                map.set(p1, '[');
                map.set(pos1, ']');
            }
            return true;
        }
        if (c == '#') {
            return false;
        }
        return false;
    }
    else if (dir == RIGHT) {
        vec2 p2 = step(pos2, dir);
        char c = map.get(p2);
        if (c == '.' || (c == '[' && check_push(map, p2, step(p2, dir), dir, only_try))) {
            if (!only_try) {
                map.set(pos2, '[');
                map.set(p2, ']');
            }
            return true;
        }
        if (c == '#') {
            return false;
        }
        return false;
    }
    else if (dir == UP || dir == DOWN) {
        vec2 p1 = step(pos1, dir);
        char c1 = map.get(p1);
        vec2 p1p1, p1p2;
        bool push1 = false;
        if (c1 == '[') {
            p1p1 = p1;
            p1p2 = step(p1, RIGHT);
            push1 = true;
        }
        else if (c1 == ']') {
            p1p1 = step(p1, LEFT);
            p1p2 = p1;
            push1 = true;
        }
        bool one_ok = (c1 == '.') || (push1 && check_push(map, p1p1, p1p2, dir, true));
        vec2 p2 = step(pos2, dir);
        char c2 = map.get(p2);
        vec2 p2p1, p2p2;
        bool push2 = false;
        if (c2 == '[') {
            p2p1 = p2;
            p2p2 = step(p2, RIGHT);
            push2 = true;
        }
        else if (c2 == ']') {
            p2p1 = step(p2, LEFT);
            p2p2 = p2;
            push2 = true;
        }
        bool two_ok = (c2 == '.') || (push2 && check_push(map, p2p1, p2p2, dir, true));
        if (one_ok && two_ok) {
            if (!only_try) {
                if (push1) {
                    check_push(map, p1p1, p1p2, dir, false);
                }
                if (push2) {
                    check_push(map, p2p1, p2p2, dir, false);
                }
                map.set(p1, '[');
                map.set(p2, ']');
                map.set(pos1, '.');
                map.set(pos2, '.');
            }
            return true;
        }
        else {
            return false;
        }
    }
    throw runtime_error("Illegal direction");
}

bool brk = false;

void push(map_t& map, vec2& pos, dir_t dir) {
    if (brk) {
        brk = false;
    }
    vec2 p12 = step(pos, dir);
    char c = map.get(p12);
    if (c == '#') return;

    bool ok = false;
    if (dir == LEFT) {
        ok = c == '.' || check_push(map, step(p12, dir), p12, dir, false);
    }
    else if (dir == RIGHT) {
        ok = c == '.' || check_push(map, p12, step(p12, dir), dir, false);
    }
    else if (dir == UP || dir == DOWN) {
        if (c == '.') ok = true;
        if (c == '[') {
            ok = check_push(map, p12, step(p12, RIGHT), dir, false);
        }
        if (c == ']') {
            ok = check_push(map, step(p12, LEFT), p12, dir, false);
        }
    }
    if (ok) {
        map.set(p12, '@');
        map.set(pos, '.');
        pos = p12;
    }
}

int64_t part1(const indata& data) {
    int64_t result = 0;
    indata d = data;
    vec2 pos = find_pos(d.map);

    for (char c : d.instructions) {
        dir_t dir = get_dir(c);
        const vec2 pos_z = pos;
        vec2 p = step(pos, dir);
        const vec2 pos_y = p;
        while (true) {
            char pc = d.map.get(p);
            if (pc == '#') {
                break;
            }
            if (pc == '.') {
                d.map.set(p, 'O');
                d.map.set(pos_y, '@');
                d.map.set(pos_z, '.');
                pos = pos_y;
                break;
            }
            if (pc != 'O') {
                throw runtime_error("Unexpected map char " + pc);
            }
            p = step(p, dir);
        }
    }
    result = sum_gps(d.map);
    return result;
}

int64_t part2(const indata& data) {
    int64_t result = 0;
    map_t d = convert_map(data.map);

    vec2 pos = find_pos(d);
    int i = 0;
    for (char c : data.instructions) {
        if (i == 21) brk = true;
        //print("Move: {} ({})\n", c, i);
        push(d, pos, get_dir(c));
        //print_map(d);
        //Sleep(100);
        i++;
    }
    result = sum_gps(d);
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
