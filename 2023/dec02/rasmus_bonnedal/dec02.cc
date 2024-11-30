#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>

using namespace std;
using stringvec = std::vector<std::string>;

struct pick {
    int r = 0;
    int g = 0;
    int b = 0;
};

struct game {
    int id;
    vector<pick> picks;
};

using indata = vector<game>;

indata parse(const std::string& filename) {
    indata data;
    for (const auto& s : split(read_file(filename), "\n")) {
        game g;
        auto v = split(s, ":");
        g.id = stoi(split(v[0], " ")[1]);
        for (const auto& s : split(v[1], ";")) {
            pick p;
            for (const auto& s : split(s, ",")) {
                auto v = split(s, " ");
                if (v[1] == "red") {
                    p.r += stoi(v[0]);
                }
                else if (v[1] == "green") {
                    p.g += stoi(v[0]);
                }
                else if (v[1] == "blue") {
                    p.b += stoi(v[0]);
                }
                else {
                    throw std::runtime_error("Illegal color " + v[1]);
                }
            }
            g.picks.push_back(p);
        }
        data.push_back(g);
    }
    return data;
}

bool is_game_possible(const game& g, const pick& bag) {
    for (const auto& pick : g.picks) {
        if (pick.r > bag.r || pick.g > bag.g || pick.b > bag.b) {
            return false;
        }
    }
    return true;
}

pick fewest_cubes(const game& g) {
    pick result;
    for (auto& pick : g.picks) {
        result.r = max(result.r, pick.r);
        result.g = max(result.g, pick.g);
        result.b = max(result.b, pick.b);
    }
    return result;
}

int part1(const indata& data) {
    int sum = 0;
    pick bag{ 12, 13, 14 };
    for (const auto& g : data) {
        if (is_game_possible(g, bag)) {
            sum += g.id;
        }
    }
    return sum;
}

int part2(const indata& data) {
    int sum = 0;
    for (const auto& g : data) {
        pick fewest = fewest_cubes(g);
        sum += fewest.r * fewest.g * fewest.b;
    }
    return sum;
}

void test() {
}

int main(int argc, char** argv) {
    try {
        test();
        auto data = parse("..\\input.txt");
        std::print("part1: {}\n", part1(data));
        std::print("part2: {}\n", part2(data));
    }
    catch (const std::exception& e) {
        std::print("Error: {}\n", e.what());
    }
    return 0;
}
