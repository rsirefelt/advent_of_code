#include "ctl.hh"

#include <iostream>

using indata_t = std::vector<std::vector<std::vector<bool>>>;

indata_t parse(const std::string& filename) {
    indata_t retval(1);
    auto lines = split(read_file(filename), "\n");
    for (auto& line: lines) {
        retval[0].push_back(map([](auto c) { return c == '#'; }, line));
    }
    return retval;
}

int print(const indata_t& indata) {
    int c = 0;
    for (auto& z: indata) {
        for (auto& y: z) {
            for (auto x: y) {
                if (x) c++;
                std::cout << (x ? "#" : ".");
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
    }
    return c;
}

indata_t expand(const indata_t& d) {
    indata_t retval;
    retval.resize(d.size() + 2);
    for (auto& y: retval) {
        y.resize(d[0].size() + 2);
        for (auto& line: y) {
            line.resize(d[0][0].size() + 2, false);
        }
    }
    return retval;
}

bool get(const indata_t& d, int x, int y, int z) {
    int n_z = d.size();
    int n_y = d[0].size();
    int n_x = d[0][0].size();

    if (z < 0 || z >= n_z) return false;
    if (y < 0 || y >= n_y) return false;
    if (x < 0 || x >= n_x) return false;
    return d[z][y][x];
}

int count(const indata_t& d, int ix, int iy, int iz) {
    int n_z = d.size();
    int n_y = d[0].size();
    int n_x = d[0][0].size();

    int c = 0;
    for (int z = iz - 1; z <= iz + 1; ++z) {
        for (int y = iy - 1; y <= iy + 1; ++y) {
            for (int x = ix - 1; x <= ix + 1; ++x) {
                if (x != ix || y != iy || z != iz) {
                    if (get(d, x, y, z)) c++;
                }
            }
        }
    }
    return c;
}

indata_t step(const indata_t& d) {
    indata_t retval = expand(d);
    int n_z = retval.size();
    int n_y = retval[0].size();
    int n_x = retval[0][0].size();

    count(d, 1, 1, 0);

    for (int z = 0; z < n_z; z++) {
        for (int y = 0; y < n_y; y++) {
            for (int x = 0; x < n_x; x++) {
                int c = count(d, x - 1, y - 1, z - 1);
                if (get(d, x - 1, y - 1, z - 1)) {
                    if (c == 2 || c == 3) retval[z][y][x] = true;
                } else {
                    if (c == 3) retval[z][y][x] = true;
                }
            }
        }
    }

    std::cout << "Active: " << print(retval) << std::endl;
    return retval;
}

int part1(const indata_t& indata) {
    indata_t state = indata;
    return 0;
}


int main(int argc, char** argv) {
    auto indata = parse("input");
    auto s = indata;
    for (int i = 1; i <= 6; ++i) {
        std::cout << "After " << i << " cycles:" << std::endl;
        s = step(s);

    }

    return 0;
}
