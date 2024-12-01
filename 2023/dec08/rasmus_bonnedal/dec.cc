#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>

using namespace std;
using namespace ctl;

struct node {
    string left;
    string right;
};


struct indata {
    string path;
    std::map<string, node> tree;
};

indata parse(const std::string& filename) {
    indata data;
    for (const auto& s : split(read_file(filename), "\n")) {
        if (data.path.empty()) {
            data.path = s;
        }
        else {
            auto a1 = split(s, "=");
            auto a2 = split(strip(a1[1], "()"), ",");
            string key = strip(a1[0]);
            string left = strip(a2[0]);
            string right = strip(a2[1]);
            data.tree[key] = node(left, right);
        }
    }
    return data;
}

int part1(const indata& data) {
    int i = 0;
    string next = "AAA";
    while (next != "ZZZ") {
        char dir = data.path[i % data.path.size()];
        if (dir == 'R') {
            next = data.tree.at(next).right;
        }
        else if (dir == 'L') {
            next = data.tree.at(next).left;
        }
        else {
            throw std::runtime_error("ASDSD");
        }
        i++;
    }
    return i;
}

uint64_t part2(const indata& data) {
    uint64_t result = 1;
    vector<string> nexts;
    for (const auto& [k, v] : data.tree) {
        if (k[2] == 'A') {
            nexts.push_back(k);
        }
    }

    for (auto& next : nexts) {
        uint64_t i = 0;
        while (next[2] != 'Z') {
            char dir = data.path[i % data.path.size()];
            if (dir == 'R') {
                next = data.tree.at(next).right;
            }
            else if (dir == 'L') {
                next = data.tree.at(next).left;
            }
            else {
                throw std::runtime_error("ASDSD");
            }
            i++;
        }
        result = lcm(result, i);
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
