#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

struct line {
    int min, max;
    char letter;
    std::string str;
};

std::vector<line> parse_vec(const std::string& filename) {
    std::vector<line> retval;
    std::ifstream ifs(filename);
    if (ifs.fail()) {
        throw std::runtime_error("Could not open file");
    }
    line l;
    char x;
    while(ifs >> l.min >> l.max >> l.letter >> x >> l.str) {
        l.max = -l.max;
        retval.push_back(l);
    }
    return retval;
}

bool verify1(const line& l) {
    size_t n = std::count(l.str.begin(), l.str.end(), l.letter);
    return n >= l.min && n <= l.max;
}

bool verify2(const line& l) {
    return (l.str[l.min - 1] == l.letter) !=
        (l.str[l.max - 1] == l.letter);
}

template<typename T>
int check_list(const std::vector<line>& input, T f) {
    int matches = 0;
    for (const auto& l : input) {
        if (f(l)) {
            matches++;
        }
    }
    return matches;
}

int main(int argc, char** argv) {
    auto indata = parse_vec("input");
    std::cout << "Part 1: " << check_list(indata, verify1) << std::endl;
    std::cout << "Part 2: " << check_list(indata, verify2) << std::endl;
    return 0;
}
