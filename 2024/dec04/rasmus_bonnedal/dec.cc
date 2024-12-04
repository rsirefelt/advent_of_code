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

enum Dir {
    LEFT = 1,
    RIGHT = 2,
    UP = 4,
    DOWN = 8
};

vec2 step(vec2 pos, Dir dir) {
    vec2 p = pos;
    if (dir & LEFT) p.x--;
    if (dir & RIGHT) p.x++;
    if (dir & UP) p.y--;
    if (dir & DOWN) p.y++;
    return p;
}

bool check_word(const indata& data, const string& word, const vec2 pos, const Dir dir) {
    vec2 p = pos;
    for (int i = 0; i < word.size(); ++i) {
        if (data.get(p) != word[i]) {
            return false;
        }
        p = step(p, dir);
    }
    return true;
}

int check_word(const indata& data, const string& word, const vec2 pos) {
    const Dir dirs[] = { UP, (Dir)(UP | RIGHT), RIGHT, (Dir)(RIGHT | DOWN), DOWN, (Dir)(DOWN | LEFT), LEFT, (Dir)(LEFT | UP) };
    int result = 0;
    for (int i = 0; i < 8; ++i) {
        if (check_word(data, word, pos, dirs[i])) {
            result++;
        }
    }
    return result;
}

int check_word(const indata& data, const string& word) {
    int result = 0;
    for (int y = 0; y < data.height; ++y) {
        for (int x = 0; x < data.width; ++x) {
            result += check_word(data, word, vec2(x, y));
        }
    }
    return result;
}

int check_mas(const indata& data, const vec2 pos) {
    if (data.get(pos) != 'A') return 0;
    char ul = data.get(step(pos, Dir(LEFT | UP)));
    char ur = data.get(step(pos, Dir(RIGHT | UP)));
    char dl = data.get(step(pos, Dir(LEFT | DOWN)));
    char dr = data.get(step(pos, Dir(RIGHT | DOWN)));

    if ((ul == 'M' && dr == 'S') || (ul == 'S' && dr == 'M')) {
        if ((ur == 'M' && dl == 'S') || (ur == 'S' && dl == 'M')) {
            return 1;
        }
    }
    return 0;
}

int check_mas(const indata& data) {
    int result = 0;
    for (int y = 0; y < data.height; ++y) {
        for (int x = 0; x < data.width; ++x) {
            result += check_mas(data, vec2(x, y));
        }
    }
    return result;
}


int64_t part1(const indata& data) {
    int64_t result = 0;
    result = check_word(data, "XMAS");
    return result;
}

int64_t part2(const indata& data) {
    int64_t result = 0;
    result = check_mas(data);
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
