#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>

using namespace std;
using stringvec = std::vector<std::string>;

struct board {
    stringvec data;

    char get(int x, int y) const {
        if (y < 0 || y >= height()) {
            return 0;
        }
        const string& row = data[y];
        if (x < 0 || x >= row.size()) {
            return 0;
        }
        return row[x];
    }

    int height() const {
        return (int)data.size();
    }

    int width() const {
        return (int)data[0].size();
    }

    bool is_symbol(int x, int y) const {
        char c = get(x, y);
        return c != 0 && c != '.' && (c < '0' || c > '9');
    }

    bool is_digit(int x, int y, int& digit) const {
        char c = get(x, y);
        if (c >= '0' && c <= '9') {
            digit = c - '0';
            return true;
        }
        return false;
    }

};

board parse(const std::string& filename) {
    board data;
    data.data = split(read_file(filename), "\n");
    return data;
}

bool adj_symbol(const board& data, const int x, const int y) {
    for (int yy = y - 1; yy <= (y + 1); ++yy) {
        for (int xx = x - 1; xx <= (x + 1); ++xx) {
            if (data.is_symbol(xx, yy)) {
                return true;
            }
        }
    }
    return false;
}


int part1(const board& data) {
    int sum = 0;

            
    for (int y = 0; y < data.height(); ++y) {
        bool adj = false;
        int number = 0;
        for (int x = 0; x < data.width(); ++x) {
            int digit;
            bool is_digit = data.is_digit(x, y, digit);
            if (is_digit) {
                number = number * 10 + digit;
                adj = adj || adj_symbol(data, x, y);
            }
            if (!is_digit || x == data.width() - 1) {
                if (adj && number > 0) {
                    sum += number;
                }
                number = 0;
                adj = false;
            }
        }
    }

    return sum;
}

struct number {
    int x1, x2, y;
    int num;
    bool operator<(const number& rhs) const {
        if (x1 != rhs.x1) return x1 < rhs.x1;
        if (x2 != rhs.x2) return x2 < rhs.x2;
        if (y != rhs.y) return y < rhs.y;
        if (num != rhs.num) return num < rhs.num;
        return false;
    }
};

int part2(const board& data) {
    vector<number> nums;

    for (int y = 0; y < data.height(); ++y) {
        bool adj = false;
        number num{ -1, -1, y, 0 };

        for (int x = 0; x < data.width(); ++x) {
            int digit;
            bool is_digit = data.is_digit(x, y, digit);
            if (is_digit) {
                if (num.x1 == -1) {
                    num.x1 = x;
                }
                num.num = num.num * 10 + digit;
                adj = adj || adj_symbol(data, x, y);
            }
            if (!is_digit || x == data.width() - 1) {
                if (adj && num.num > 0) {
                    num.x2 = x;
                    nums.push_back(num);
                }
                num = { -1, -1, y, 0 };
                adj = false;
            }
        }
    }
    int sum = 0;
    for (int y = 0; y < data.height(); ++y) {
        for (int x = 0; x < data.width(); ++x) {
            if (data.get(x, y) == '*') {
                set<number> gear_nums;
                for (int yy = y - 1; yy <= y + 1; ++yy) {
                    for (int xx = x - 1; xx <= x + 1; ++xx) {
                        int digit;
                        if (data.is_digit(xx, yy, digit)) {
                            for (const auto& num : nums) {
//                                print("checking ({}, {}) vs ({}-{}, {})", xx, yy, num.x1, num.x2, num.y);
                                if (num.y == yy && num.x1 <= xx && num.x2 >= xx) {
                                    gear_nums.insert(num);
//                                    print(": true\n");
                                }
                                else {
//                                    print(": false\n");
                                }
                            }
                        }
                    }
                }
                if (gear_nums.size() == 2) {
                    int prod = 1;
                    for (const auto& n : gear_nums) {
                        prod *= n.num;
                    }
                    sum += prod;
                }
            }
        }
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
