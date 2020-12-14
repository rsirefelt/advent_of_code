#include "ctl.hh"

#include <assert.h>
#include <iostream>
#include <sys/time.h>

struct indata_t {
    int early;
    std::vector<long> sched;
};

indata_t parse(const std::string& filename) {
    auto x = split(read_file(filename), "\n");
    indata_t retval;
    retval.early = std::stoi(x[0]);
    retval.sched = map([](const std::string& s) -> long {
        if (s == "x") return -1;
        return (long)std::stoi(s);
    }, split(x[1], ","));
    return retval;
}

int check_bus(const indata_t& ind) {
    int bestbus = 0;
    int besttime = 0;

    for (const auto& s : ind.sched) {
        if (s > 0) {
            int t = (ind.early / s + 1) * s;
            if (besttime == 0 || t < besttime) {
                bestbus = s;
                besttime = t;
            }
        }
    }
    return (besttime - ind.early) * bestbus;
}

int t() {
    struct timeval tv;
    gettimeofday(&tv,NULL);
    return 1000000 * tv.tv_sec + tv.tv_usec;
}

std::vector<int> find_largest_group(const std::vector<std::pair<int64_t, int64_t>>& prs, int& group) {
    std::map<int, int> occurrences;
    int max = 0;
    for (int try_group = 0; try_group < 1000; ++try_group) {
        int members = 0;
        for (auto &x: prs) {
            int sched = x.first;
            int offset = x.second;
            if ((try_group - offset % sched) % sched == 0) {
                members++;
            }
        }
        if (members > max) {
            std::cout << "Found offset " << try_group << " with " << members << " buses" << std::endl;
            max = members;
            group = try_group;
        }
    }
    std::vector<int> retval;
    for (auto &x: prs) {
        if ((group - x.second % x.first) % x.first == 0) {
            retval.push_back(x.first);
        }
    }
    return retval;
}

int64_t check_bus2(const indata_t& ind) {
    std::vector<std::pair<int64_t, int64_t>> prs;
    for (size_t i = 0; i < ind.sched.size(); ++i) {
        if (ind.sched[i] > 0) {
            prs.push_back(std::make_pair<int64_t, int64_t>((int64_t)ind.sched[i], (int64_t)i));
        }
    }

    int offset;
    int64_t t_step = lcm(find_largest_group(prs, offset));
    std::cout << "LCM of busses in group " << offset << " is " << t_step << std::endl;
    int64_t n = 1;
    while(true) {
        bool found = true;
        int64_t time = t_step * n - offset;
        for (auto& x: prs) {
            if ((time + x.second) % x.first != 0) {
                found = false;
                break;
            }
        }
        if (found) {
            std::cout << "Found after " << n << " iterations." << std::endl;
            return time;
        }
        n++;
    }
    return 0;
}

int main(int argc, char** argv) {
    auto indata = parse("input");
    int part1 = check_bus(indata);
    assert(part1 == 3035);
    std::cout << "Part 1: " << part1 << std::endl;
    int64_t part2 = check_bus2(indata);
    std::cout << "Part 2: " << part2 << std::endl;

    return 0;
}
