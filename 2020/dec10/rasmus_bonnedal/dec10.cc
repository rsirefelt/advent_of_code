#include "ctl.hh"

#include <assert.h>
#include <iostream>

using intvec = std::vector<int64_t>;

intvec parse(const std::string& filename) {
    return sorted(map(stol, split(read_file(filename), "\n")));
}

// Calculate the number of ways a set of connectors
// with one jolt difference can be combined
int64_t calc_ones(int length) {
    int n_minus_3 = 0;
    int n_minus_2 = 0;
    int n_minus_1 = 1;
    int n = 1;

    for (int i = 1; i < length; ++i) {
        n_minus_3 = n_minus_2;
        n_minus_2 = n_minus_1;
        n_minus_1 = n;
        n += n_minus_2 + n_minus_3;
    }
    return n;
}

// Store the length of groups with differences of 1
intvec group_ones(const intvec& v) {
    int cur_jolt = 0;
    int cur_count = 0;
    intvec retval;
    for (size_t i = 0; i < v.size(); ++i) {
        if (v[i] - cur_jolt == 1) {
            cur_count++;
        } else {
            retval.push_back(cur_count);
            cur_count = 0;
        }
        cur_jolt = v[i];
    }
    retval.push_back(cur_count);
    return retval;
}

int main(int argc, char** argv) {
    auto indata = parse("input");
    auto groups = group_ones(indata);
    std::cout << "Part 1: " << sum(groups) * groups.size() << std::endl;    
    std::cout << "Part 2: " << prod(map(calc_ones, groups)) << std::endl;
    return 0;
}
