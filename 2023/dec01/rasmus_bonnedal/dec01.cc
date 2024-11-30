#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>

using namespace std;
using stringvec = std::vector<std::string>;

stringvec parse(const std::string& filename) {
    return split(read_file(filename), "\n");
}

int part1(const stringvec& v) {
    const std::string digits = "0123456789";
    int sum = 0;
    for (const auto& s : v) {
        int number = (s[s.find_first_of(digits)] - '0') * 10 + (s[s.find_last_of(digits)] - '0');
        sum += number;
    }
    return sum;
}

int find_first_digit(string_view s) {
    const vector<string> digits = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
    const std::string digits2 = "0123456789";
    int best_pos = -1;
    int digit = -1;

    for (int i = 0; i < digits.size(); ++i) {
        size_t pos = s.find(digits[i]);
        if (pos != std::string::npos && (best_pos == -1 || pos < best_pos)) {
            best_pos = (int)pos;
            digit = i;
        }
    }
    size_t pos = s.find_first_of(digits2);
    if (pos != std::string::npos && (best_pos == -1 || pos < best_pos)) {
        digit = s[pos] - '0';
    }
    if (digit < 0 || digit > 9) {
        throw std::runtime_error(std::format("Invalid digit value {} in {}\n", digit, s));
    }
    return digit;
}

int find_last_digit(string_view s) {
    const vector<string> digits = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
    const std::string digits2 = "0123456789";
    int best_pos = -1;
    int digit = -1;

    for (int i = 0; i < digits.size(); ++i) {
        size_t pos = s.rfind(digits[i]);
        if (pos != std::string::npos && (int)pos > best_pos) {
            best_pos = (int)pos;
            digit = i;
        }
    }
    size_t pos = s.find_last_of(digits2);
    if (pos != std::string::npos && (int)pos > best_pos) {
        digit = s[pos] - '0';
    }
    if (digit < 0 || digit > 9) {
        throw std::runtime_error(std::format("Invalid digit value {} in {}\n", digit, s));
    }
    return digit;
}

int part2(const stringvec& v) {
    int sum = 0;
    for (const auto& s : v) {
        sum += find_first_digit(s) * 10 + find_last_digit(s);
    }
    return sum;
}

void test() {
    CHECK(find_first_digit("xone2") == 1);
    CHECK(find_first_digit("xtwoone3") == 2);
    CHECK(find_first_digit("8one") == 8);
    CHECK(find_first_digit("xninex") == 9);
    CHECK(find_first_digit("threetwo") == 3);
    CHECK(find_first_digit("xtwxtwxtwfour") == 4);

    CHECK(find_last_digit("xone2") == 2);
    CHECK(find_last_digit("xtwoone3") == 3);
    CHECK(find_last_digit("8one") == 1);
    CHECK(find_last_digit("xninex") == 9);
    CHECK(find_last_digit("threetwo") == 2);
    CHECK(find_last_digit("xtwxtwxtwfour") == 4);
}

int main(int argc, char** argv) {
    try {
        test();
        auto indata = parse("..\\input.txt");
        std::print("part1: {}\n", part1(indata));
        std::print("part2: {}\n", part2(indata));
    }
    catch (const std::exception& e) {
        std::print("Error: {}\n", e.what());
    }
    return 0;
}
