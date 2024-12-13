#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>
#include <regex>

using namespace std;
using namespace ctl;

struct machine {
    vec2 a, b, prize;
};

using indata = vector<machine>;

indata parse(const std::string& filename) {
    indata d;
    machine m;
    for (const auto& s : split(read_file(filename), "\n")) {
        auto s1 = split(s, " ");
        if (in("Button A", s)) {
            int x = stoint(strip(s1[2], "X+,"));
            int y = stoint(strip(s1[3], "Y+"));
            m.a = vec2(x, y);
        }
        else if (in("Button B", s)) {
            int x = stoint(strip(s1[2], "X+,"));
            int y = stoint(strip(s1[3], "Y+"));
            m.b = vec2(x, y);
        }
        else if (in("Prize", s)) {
            int x = stoint(strip(s1[1], "X=,"));
            int y = stoint(strip(s1[2], "Y="));
            m.prize = vec2(x, y);
            d.push_back(m);
        }
    }
    return d;
}

int64_t find_best(const machine& p, int64_t g = 10000000000000) {
    int64_t Cx = p.prize.x + g;
    int64_t Cy = p.prize.y + g;
    /*
    a * Ax + b * Bx = Cx
    a * Ay + b * By = Cy

    a = (Cx - b * Bx) / Ax

    (Cx - b * Bx) / Ax * Ay + b * By = Cy
    (Cx - b * Bx) * Ay + b * By * Ax = Cy * Ax
    - b * Bx * Ay + b * Ax * By = Cy * Ax - Cx * Ay
    b * (Ax * By - Ay * Bx) = Ax * Cy - Ay * Cx
    b = (Ax * Cy - Ay * Cx) / (Ax * By - Ay * Bx)
    */
    int64_t b = (p.a.x * Cy - p.a.y * Cx) / (p.a.x * p.b.y - p.a.y * p.b.x);
    int64_t a = (Cx - b * p.b.x) / p.a.x;
    if (a * p.a.x + b * p.b.x == Cx && a * p.a.y + b * p.b.y == Cy) {
        return a * 3 + b;
    }
    return 0;
}

int64_t part1(const indata& data) {
    int64_t result = 0;
    for (const auto& prize : data) {
        result += find_best(prize, 0);
    }
    return result;
}

int64_t part2(const indata& data) {
    int64_t result = 0;
    for (const auto& prize : data) {
        result += find_best(prize);
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
