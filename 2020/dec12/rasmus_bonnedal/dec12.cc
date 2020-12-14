#include "ctl.hh"

#include <assert.h>
#include <iostream>
#include <sys/time.h>

using indata_t = std::vector<std::pair<char, int>>;

indata_t parse(const std::string& filename) {
    return map([](const auto& s) {
        return std::make_pair(s[0], std::stoi(s.substr(1)));
    }, split(read_file(filename), "\n"));
}

int t() {
    struct timeval tv;
    gettimeofday(&tv,NULL);
    return 1000000 * tv.tv_sec + tv.tv_usec;
}

int64_t navigate(const indata_t& v) {
    int dir = 90;
    int64_t x = 0;
    int64_t y = 0;

    int dirx[4] = { 0, 1, 0, -1 };
    int diry[4] = { 1, 0, -1, 0 };

    for (auto& e: v) {
        switch(e.first) {
            case 'N': y += e.second; break;
            case 'S': y -= e.second; break;
            case 'E': x += e.second; break;
            case 'W': x -= e.second; break;
            case 'R': dir = (dir + e.second) % 360; break;
            case 'L': dir = (dir - e.second + 360) % 360; break;
            case 'F': {
                x += dirx[dir / 90] * e.second;
                y += diry[dir / 90] * e.second;
                break;
            }            
        }
    }
    return abs(x) + abs(y);
}

void rot(int deg, int& x, int& y) {
    for (int i = 0; i < ((deg + 360) % 360) / 90; ++i) {
        int xp = y;
        y = -x;
        x = xp;
    }
}

int64_t navigate2(const indata_t& v) {
    int dir = 90;
    int64_t x = 0;
    int64_t y = 0;
    int waypx = 10;
    int waypy = 1;

    // rotr: waypx' = waypy, waypy' = -waypx

    for (auto& e: v) {
        switch(e.first) {
            case 'N': waypy += e.second; break;
            case 'S': waypy -= e.second; break;
            case 'E': waypx += e.second; break;
            case 'W': waypx -= e.second; break;
            case 'R': rot(e.second, waypx, waypy); break;
            case 'L': rot(-e.second, waypx, waypy); break;
            case 'F': {
                x += waypx * e.second;
                y += waypy * e.second;
                break;
            }            
        }
    }
    return abs(x) + abs(y);
}

int main(int argc, char** argv) {
    auto indata = parse("input");
    int64_t part1 = navigate(indata);
    std::cout << "Part 1: " << part1 << std::endl;
    std::cout << "Part 2: " << navigate2(indata) << std::endl;


    return 0;
}
