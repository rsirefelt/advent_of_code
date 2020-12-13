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
    std::vector<std::string> y = filter(split(x[1], ","),
        [](const auto& s) { return s != "x"; });
    retval.sched = map(stol, y);
    return retval;
}

indata_t parse2(const std::string& filename) {
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


//    int t = 11;
//    int b = 3;
//    leave at 12;

    for (const auto& s : ind.sched) {
        int t = (ind.early / s + 1) * s;
        if (besttime == 0 || t < besttime) {
            bestbus = s;
            besttime = t;
        }
    }
    return (besttime - ind.early) * bestbus;
}

int t() {
    struct timeval tv;
    gettimeofday(&tv,NULL);
    return 1000000 * tv.tv_sec + tv.tv_usec;
}

int64_t check_bus2(const indata_t& ind) {
    std::vector<std::pair<int64_t, int64_t>> prs;
    for (size_t i = 0; i < ind.sched.size(); ++i) {
        if (ind.sched[i] > 0) prs.push_back(std::make_pair<int64_t, int64_t>((int64_t)ind.sched[i], (int64_t)i));
    }
//    sort(prs);
    for (auto& x: prs) {
        x.second = x.second % x.first;
    }
/*
    LCM(19, 41, 449) = 349771
    349771 - 17 = 349754
    349771 * 17 = 5946107
    At least 100 000 000 000 000
    56313132
*/

    int64_t t = 349771 * 17;
    int64_t n = 1;
    while(true) {
        bool found = true;
        for (auto& x: prs) {
            if (((t*n-17) + x.second) % x.first != 0) {
                found = false;
                break;
            }
        }
        if (found) return t * n - 17;
        n++;
    }

    return 0;
}



int main(int argc, char** argv) {
    auto indata = parse("input");
    std::cout << "Part 1: " << check_bus(indata) << std::endl;
    auto indata2 = parse2("input");
    std::cout << "Part 2: " << check_bus2(indata2) << std::endl;

    return 0;
}
