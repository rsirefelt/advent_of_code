#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>

using namespace std;
using namespace ctl;

struct pos {
    int x, y;
};

enum dir {
    UP = 1,
    DOWN = 2,
    LEFT = 4,
    RIGHT = 8
};

const char UP_DOWN = '|';
const char LEFT_RIGHT = '-';
const char UP_RIGHT = 'L';
const char UP_LEFT = 'J';
const char LEFT_DOWN = '7';
const char DOWN_RIGHT = 'F';

struct indata {
    vector<string> board;
    vector<string> path;
    int width, height;
    char get(pos p) const {
        if (p.x < 0 || p.y < 0 || p.x >= width || p.y >= height) {
            return '.';
        }
        return board[p.y][p.x];
    }
    void set(pos p, char c) {
        if (p.x < 0 || p.y < 0 || p.x >= width || p.y >= height) {
            throw runtime_error("Outside board");
        }
        path[p.y][p.x] = c;
    }
    char get_path(pos p) const {
        if (p.x < 0 || p.y < 0 || p.x >= width || p.y >= height) {
            return 'X';
        }
        return path[p.y][p.x];
    }
};

indata parse(const std::string& filename) {
    indata data;
    data.board = split(read_file(filename), "\n");
    for (const auto& row : data.board) {
        print("'{}'\n", row);
    }
    data.height = (int)data.board.size();
    data.width = (int)data.board[0].size();
    for (int i = 0; i < data.height; ++i) {
        data.path.push_back(string(data.width, '.'));
    }
    return data;
}

pos find_pos(const indata& data) {
    pos p{ 0, 0 };
    for (const auto& row : data.board) {
        size_t f = row.find('S');
        if (f != string::npos) {
            p.x = (int)f;
            CHECK(data.get(p) == 'S');
            return p;
        }
        p.y++;
    }
    throw std::runtime_error("Could not find S");
}

pos step(pos p, dir d) {
    if (d & RIGHT) {
        p.x++;
    }
    if (d & DOWN) {
        p.y++;
    }
    if (d & LEFT) {
        p.x--;
    }
    if (d & UP) {
        p.y--;
    }
    return p;
}

dir flip(dir d) {
    if (d == LEFT) return RIGHT;
    if (d == RIGHT) return LEFT;
    if (d == UP) return DOWN;
    if (d == DOWN) return UP;
    throw std::runtime_error("Unknown dir");
}

dir get_other_dir(char c, dir d) {
    d = flip(d);
    if (d == RIGHT) {
        if (c == UP_RIGHT) return UP;
        if (c == LEFT_RIGHT) return LEFT;
        if (c == DOWN_RIGHT) return DOWN;
    }
    if (d == DOWN) {
        if (c == DOWN_RIGHT) return RIGHT;
        if (c == UP_DOWN) return UP;
        if (c == LEFT_DOWN) return LEFT;
    }
    if (d == LEFT) {
        if (c == LEFT_DOWN) return DOWN;
        if (c == LEFT_RIGHT) return RIGHT;
        if (c == UP_LEFT) return UP;
    }
    if (d == UP) {
        if (c == UP_LEFT) return LEFT;
        if (c == UP_DOWN) return DOWN;
        if (c == UP_RIGHT) return RIGHT;
    }
    throw std::runtime_error("Illegal dir to pos");
}

dir find_dir(const indata& data, pos p) {
    char c_left = data.get({ p.x - 1, p.y });
    if (c_left == LEFT_RIGHT || c_left == DOWN_RIGHT || c_left == UP_RIGHT) {
        return LEFT;
    }
    char c_down = data.get({ p.x, p.y + 1 });
    if (c_down == UP_LEFT || c_down == UP_DOWN || c_down == UP_RIGHT) {
        return DOWN;
    }
    char c_up = data.get({ p.x, p.y - 1 });
    if (c_up == LEFT_DOWN || c_up == DOWN_RIGHT || c_up == UP_DOWN) {
        return UP;
    }
    char c_right = data.get({ p.x + 1, p.y });
    if (c_right == LEFT_RIGHT || c_right == LEFT_DOWN || c_right == UP_LEFT) {
        return RIGHT;
    }
    throw std::runtime_error("Could not find suitable direction");
}

int part1(indata& data) {
    int i = 0;
    pos p = find_pos(data);
    dir d = find_dir(data, p);

    int steps = 0;
    while (true) {
        data.set(p, '#');
        p = step(p, d);
        steps++;
        char c = data.get(p);
        if (c == 'S') break;
        d = get_other_dir(c, d);
    }
    return steps >> 1;
}

vector<dir> get_inside(char c, dir d) {
    if (d == RIGHT) {
        if (c == LEFT_RIGHT) { //  S -
            return { DOWN };
        }
        if (c == UP_LEFT) {    // S J
            return { DOWN, RIGHT, (dir)(DOWN | RIGHT)};
        }
        if (c == LEFT_DOWN) {  // S 7
            return { (dir)(LEFT | DOWN) };
            // DL
        }
    }
    if (d == DOWN) {
        if (c == UP_DOWN) { //     S
            return { LEFT };
        }
        if (c == UP_RIGHT) {          // S
            return { DOWN, LEFT, (dir)(DOWN | LEFT) };
            // LEFT, DOWN, DOWN_LEFT  // L
        }
        if (c == UP_LEFT) {   // S
            return { (dir)(LEFT | UP) };
            // UP_LEFT        // J
        }
    }
    if (d == LEFT) {
        if (c == LEFT_RIGHT) {   //   - S
            return { UP };
        }
        if (c == UP_RIGHT) {  //   L S
            return { (dir)(UP | RIGHT) };
            // UP_RIGHT
        }
        if (c == DOWN_RIGHT) { //  F S
            return { UP, LEFT, (dir)(UP | LEFT) };
            // UP LEFT UP_LEFT
        }
    }
    if (d == UP) {
        if (c == UP_DOWN) { //    |
            return { RIGHT };
        }
        if (c == DOWN_RIGHT) {   //  F
            return { (dir)(RIGHT | DOWN) };
            // DOWN_RIGHT        //  S
        }
        if (c == LEFT_DOWN) {     // 7
            return { RIGHT, UP, (dir)(RIGHT | UP) };
            // RIGHT UP RIGHT_UP  // S
        }
    }
    throw runtime_error("Illegal dir / char combo");
}

void flood_fill(indata& data) {
    int fills = 100;
    while (fills > 0) {
        fills = 0;
        pos p;
        for (p.y = 0; p.y < data.height; ++p.y) {
            for (p.x = 0; p.x < data.width; ++p.x) {
                char c = data.get_path(p);
                if (c == 'I') {
                    pos pp = step(p, DOWN);
                    if (data.get_path(pp) == '.') {
                        data.set(pp, 'I');
                        fills++;
                    }
                }
            }
        }
    }
}

int count_inside(indata& data) {
    int result = 0;
    pos p;
    for (p.y = 0; p.y < data.height; ++p.y) {
        for (p.x = 0; p.x < data.width; ++p.x) {
            if (data.get_path(p) == 'I') {
                result++;
            }
        }
    }
    return result;
}

int part2(indata& data) {
    pos p = find_pos(data);
    dir d = find_dir(data, p);

    int steps = 0;
    while (true) {
        p = step(p, d);
        steps++;
        char c = data.get(p);
        if (c == 'S') break;
        auto dirs = get_inside(c, d);
        for (auto dd : dirs) {
            pos pd = step(p, dd);
            if (data.get_path(pd) == '.') {
                data.set(pd, 'I');
            }
        }
        d = get_other_dir(c, d);
    }
    flood_fill(data);
    for (const auto& row : data.path) {
        print("'{}'\n", row);
    }

    return count_inside(data);
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
