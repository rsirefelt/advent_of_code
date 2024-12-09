#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>
#include <regex>

using namespace std;
using namespace ctl;

struct indata {
    vector<int> map;
};

indata parse(const std::string& filename) {
    indata d;
    bool is_free = false;
    int file_id = 0;
    for (const auto& s : split(read_file(filename), "\n")) {
        for (char c : s) {
            if (c >= '0' && c <= '9') {
                int count = c - '0';
                if (is_free) {
                    for (int i = 0; i < count; ++i) {
                        d.map.push_back(-1);
                    }
                    is_free = false;
                }
                else {
                    for (int i = 0; i < count; ++i) {
                        d.map.push_back(file_id);
                    }
                    is_free = true;
                    file_id++;
                }
            }
        }
    }
    return d;
}

int first_free(const indata& data) {
    for (int i = 0; i < data.map.size(); ++i) {
        if (data.map[i] == -1) {
            return i;
        }
    }
    throw runtime_error("No free found");
}

bool first_free_of_size(const indata& data, const int size, int& ofs) {
    for (int i = 0; i <= (data.map.size() - size); ++i) {
        bool found = true;;
        for (int j = i; j < i + size && found; ++j) {
            if (data.map[j] != -1) {
                found = false;
            }
        }
        if (found) {
            ofs = i;
            return true;
        }
    }
    return false;
}

bool find_file(const indata& data, int& max_file_id, int& pos, int& len) {
    pos--;
    while (pos >= 0 && (data.map[pos] == -1 || data.map[pos] > max_file_id)) {
        pos--;
    }
    if (pos < 0) {
        return false;
    }
    int num = data.map[pos];
    len = 1;
    while (pos >= 0 && data.map[pos] == num) {
        pos--;
        len++;
    }
    max_file_id = num - 1;
    pos++;
    len--;
    return true;
}

int last_block(const indata& data) {
    for (size_t i = data.map.size() - 1; i >= 0; --i) {
        if (data.map[i] != -1) {
            return (int)i;
        }
    }
    throw runtime_error("No block found");
}

int64_t calc_checksum(const indata& data) {
    int64_t result = 0;
    for (int i = 0; i < data.map.size(); ++i) {
        int x = data.map[i];
        if (x >= 0) {
            result += x * i;
        }
    }
    return result;
}

void print_map(const indata& data) {
    for (int i = 0; i < data.map.size(); ++i) {
        int x = data.map[i];
        if (x < 0) {
            print(" . ");
        }
        else {
            print(" {} ", x);
        }
    }
    print("\n");
}

int64_t part1(const indata& data) {
    indata d = data;
    int64_t result = 0;
    while (true) {
        int last = last_block(d);
        int first = first_free(d);
        if (first > last) {
            break;
        }
        swap(d.map[last], d.map[first]);
    }
    result = calc_checksum(d);
    return result;
}

int64_t part2(const indata& data) {
    int64_t result = 0;
    print_map(data);
    indata d = data;

    int max_file_id = 0x7fffffff;
    int ofs = (int)data.map.size();
    int len;
    while (find_file(d, max_file_id, ofs, len)) {
        int ofs_free;
        if (first_free_of_size(d, len, ofs_free)) {
            if (ofs_free < ofs) {
                for (int i = 0; i < len; ++i) {
                    swap(d.map[ofs + i], d.map[ofs_free + i]);
                }
            }
        }
    }
    result = calc_checksum(d);
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
