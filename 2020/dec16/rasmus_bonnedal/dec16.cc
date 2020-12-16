#include "ctl.hh"

#include <iostream>

struct rule_t {
    std::string field;
    std::pair<long, long> r1, r2;
};

using intvec = std::vector<long>;

struct indata_t {
    std::vector<rule_t> rules;
    intvec my_tic;
    std::vector<intvec> nearby_tics;
};

indata_t parse(const std::string& filename) {
    indata_t retval;
    auto x = split(read_file(filename), "\n\n");
    for (auto& r: split(x[0],"\n")) {
        auto s1 = split(r, ": ");
        rule_t rule;
        rule.field = s1[0];
        auto s2 = split(s1[1], " or ");
        auto s3 = split(s2[0], "-");
        auto s4 = split(s2[1], "-");
        rule.r1 = std::make_pair(std::stol(s3[0]), std::stol(s3[1]));
        rule.r2 = std::make_pair(std::stol(s4[0]), std::stol(s4[1]));
        retval.rules.push_back(rule);
    }
    retval.my_tic = map(stol, split(split(x[1], "\n")[1], ","));
    auto nearbys = split(x[2], "\n");
    for (size_t i = 1; i < nearbys.size(); ++i) {
        retval.nearby_tics.push_back(map(stol, split(nearbys[i], ",")));
    }
    return retval;
}

bool in_range(const std::pair<long, long>& range, long val) {
    return val >= range.first && val <= range.second;
}

int part1(const indata_t& indata, std::vector<intvec>& valids) {
    int invalid_sum = 0;
    for (auto& tic: indata.nearby_tics) {
        bool tic_valid = true;
        for (auto& val: tic) {
            bool valid = false;
            for (auto& range: indata.rules) {
                if (in_range(range.r1, val) || in_range(range.r2, val)) {
                    valid = true;
                    break;
                }
            }
            if (!valid) {
                invalid_sum += val;
                tic_valid = false;
            }
        }
        if (tic_valid) {
            valids.push_back(tic);
        }
    }
    return invalid_sum;
}

int64_t part2(const indata_t& indata, const std::vector<intvec>& valids) {
    int n_rules = indata.rules.size();

    std::vector<bool> rule_found(n_rules, false);
    std::map<int, std::string> field_names;

    int iters = 0;
    while(true) {
        if (std::count(rule_found.begin(), rule_found.end(), false) == 0) break;
        iters++;
        for (int field = 0; field < valids[0].size(); ++field) {
            std::vector<bool> rule_ok(n_rules, true);
            for (auto& valid: valids) {
                int val = valid[field];
                for (int i = 0; i < n_rules; ++i) {
                    if (!in_range(indata.rules[i].r1, val) && !in_range(indata.rules[i].r2, val)) {
                        rule_ok[i] = false;
                    }
                }
            }
            for (int i = 0; i < n_rules; ++i) {
                if (rule_found[i]) rule_ok[i] = false;
            }
            if (std::count(rule_ok.begin(), rule_ok.end(), true) == 1) {
                for (int i = 0; i < n_rules; ++i) {
                    if (rule_ok[i] && !rule_found[i]) {
                        std::cout << "Field " << field << " is " << indata.rules[i].field << std::endl;
                        rule_found[i] = true;
                        field_names[field] = indata.rules[i].field;
                    }
                }
            }
        }
    }
    int64_t product = 1;
    for (int i = 0; i < indata.my_tic.size(); ++i) {
        if (field_names[i].find("departure") != std::string::npos) {
            std::cout << field_names[i] << ", " << indata.my_tic[i] << std::endl;
            product *= indata.my_tic[i];
        }
    }
    std::cout << "Solved in " << iters << " iterations" << std::endl;
    return product;
}

int main(int argc, char** argv) {
//    auto indata = parse("input");
    auto indata = parse("niklas_input");
    std::vector<intvec> valids;
    std::cout << "Part 1: " << part1(indata, valids) << std::endl;
    std::cout << "Part 2: " << part2(indata, valids) << std::endl;
    return 0;
}
