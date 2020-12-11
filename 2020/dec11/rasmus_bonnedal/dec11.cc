#include "ctl.hh"

#include <assert.h>
#include <iostream>
#include <sys/time.h>

using indata_t = std::vector<std::string>;

indata_t parse(const std::string& filename) {
    return split(read_file(filename), "\n");
}

indata_t iter(const indata_t& v, bool& changed, int& occ) {
    changed = false;
    occ = 0;
    indata_t retval = v;
    for (int y = 0; y < v.size(); ++y) {
        for (int x = 0; x < v[0].size(); ++x) {
            int empties = 0;
            int occupied = 0;
            for (int yy = -1; yy <= 1; ++yy) {
                size_t yp = y + yy;
                if (yp < 0 || yp >= v.size()) continue;
                for (int xx = -1; xx <= 1; ++xx) {
                    size_t xp = x + xx;
                    if (xp < 0 || xp >= v[0].size()) continue;
                    if (yy == 0 && xx == 0) continue;
                    char seat = v[yp][xp];
                    if (seat == 'L') empties++;
                    if (seat == '#') occupied++;
                }                
            }
            char seat = v[y][x];
            if (seat == 'L' && occupied == 0) {
                changed = true;
                retval[y][x] = '#';
            } else if (seat == '#' && occupied >= 4) {
                changed = true;
                retval[y][x] = 'L';
            }
            if (retval[y][x] == '#') occ++;
        }
    }
    return retval;
}

char scan(const indata_t& v, int x, int y, int xx, int yy) {
    int height = v.size();
    int width = v[0].size();
    while(true) {
        x += xx;
        y += yy;
        if (x < 0 || y < 0 || x >= width || y >= height) return '.';
        char s = v[y][x];
        if (s != '.') return s;
    }
}

indata_t iter2(const indata_t& v, bool& changed, int& occ) {
    changed = false;
    occ = 0;
    indata_t retval = v;
    for (int y = 0; y < v.size(); ++y) {
        for (int x = 0; x < v[0].size(); ++x) {
            int empties = 0;
            int occupied = 0;
            for (int yy = -1; yy <= 1; ++yy) {
                for (int xx = -1; xx <= 1; ++xx) {
                    if (yy == 0 && xx == 0) continue;
                    char seat = scan(v, x, y, xx, yy);
                    if (seat == 'L') empties++;
                    if (seat == '#') occupied++;
                }                
            }
            char seat = v[y][x];
            if (seat == 'L' && occupied == 0) {
                changed = true;
                retval[y][x] = '#';
            } else if (seat == '#' && occupied >= 5) {
                changed = true;
                retval[y][x] = 'L';
            }
            if (retval[y][x] == '#') occ++;
        }
    }
    return retval;
}

int t() {
    struct timeval tv;
    gettimeofday(&tv,NULL);
    return 1000000 * tv.tv_sec + tv.tv_usec;
}

int main(int argc, char** argv) {
    auto indata = parse("input");

    auto indata1 = indata;
    bool changed = true;
    int occupied;
    while(changed) {
        indata1 = iter(indata1, changed, occupied);
    }
    std::cout << "Part 1: " << occupied << std::endl;

    changed = true;
    while(changed) {
        indata = iter2(indata, changed, occupied);
    }
    std::cout << "Part 2: " << occupied << std::endl;


    return 0;
}
