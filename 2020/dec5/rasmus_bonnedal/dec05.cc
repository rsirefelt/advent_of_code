#include "ctl.hh"

#include <iostream>

using stringvec = std::vector<std::string>;

std::vector<std::string> parse(const std::string& filename) {
    return split(read_file(filename), "\n");
}

int calc_seat_id(const std::string& b) {
    int id = 0;
    for (char c: b) {
        id <<= 1;
        if (c == 'B' || c == 'R') {
            id += 1;
        }
    }
    return id;
}

int main(int argc, char** argv) {
    stringvec indata = parse("input");
    std::vector<int> id = map(calc_seat_id, indata);
    sort(id);
    std::cout << "Part 1: " << id.back() << std::endl;
    for (size_t i = 1; i + 1 < id.size(); ++i) {
        if (id[i + 1] - id[i] > 1) {
            std::cout << "Part 2: " << id[i] + 1 << std::endl;
        }
    }
    return 0;
}
