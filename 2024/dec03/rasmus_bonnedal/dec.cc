#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>
#include <regex>

using namespace std;
using namespace ctl;

typedef string indata;

int64_t process(const string& s, bool use_do) {
    int64_t result = 0;
    bool enable = true;
    auto start = s.begin();
    smatch res;
    regex exp("mul\\((\\d{1,3})\\,(\\d{1,3})\\)|do\\(\\)|don't\\(\\)");
    while (regex_search(start, s.end(), res, exp)) {
        char third = res[0].str()[2];
        if (third == 'l') { // "mul(nnn,nnn)"
            if (!use_do || enable) {
                result += stoint(res[1]) * stoint(res[2]);
            }
        }
        else if (third == '(') { // "do()"
            enable = true;
        }
        else if (third == 'n') { // "don't()"
            enable = false;
        }
        start = res.suffix().first;
    }
    return result;
}


indata parse(const std::string& filename) {
    return read_file(filename);
}

int64_t part1(const indata& data) {
    return process(data, false);
}

int64_t part2(const indata& data) {
    return process(data, true);
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
