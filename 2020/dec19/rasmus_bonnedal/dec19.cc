#include "ctl.hh"

#include <iostream>
#include <sstream>
#include <assert.h>

struct rule_t {
    int from;
    std::vector<std::vector<int>> oth;
    char c;
};

struct indata_t {
    std::vector<rule_t> rules;
    std::vector<std::string> msg;
};

int stoi(const std::string& s) { return std::stoi(s); }

rule_t parse_rule(const std::string& s2) {
    rule_t retval;
    auto x = split(s2, ":");
    retval.from = std::stoi(x[0]);
    std::string s = x[1];
    if (s.find("\"") != s.npos) {
        retval.c = s[2];
    } else {
        for (auto& x: split(s, "|")) {
            retval.oth.push_back(map(stoi, split(x, " ")));
        }
        retval.c = 0;
    }

    return retval;
}

indata_t parse(const std::string& filename) {
    indata_t retval;
    auto s = split(read_file(filename), "\n\n");
    retval.rules = map(parse_rule, split(s[0], "\n"));
    retval.msg = split(s[1], "\n");
    return retval;
}

const rule_t& find_rule(const indata_t& ind, int rule) {
    for (auto& r: ind.rules) {
        if (r.from == rule) return r;
    }
    assert(0);
    return ind.rules[0];
}

std::string print_rule(const rule_t& rule) {
    std::stringstream ss;
    ss << rule.from << ": ";
    if (rule.c) {
        ss << "\"" << rule.c << "\"";
    } else {
        for (int i = 0; i < rule.oth.size(); ++i) {
            for (int n: rule.oth[i]) {
                ss << n << " ";
            }
            if (i < rule.oth.size() - 1) {
                ss << "| ";
            }
        }
    }
    return ss.str();
}

bool match2(const indata_t& ind, const rule_t& rule, const std::string& msg, int& offs) {
    if (offs >= msg.size()) return false;
    // std::cout << "checking " << msg.substr(offs) << " against " << print_rule(rule) << std::endl;
    if (rule.c == msg[offs]) {
        offs++;
        return true;
    }

    for (const auto& r: rule.oth) {
        int offs2 = offs;
        bool is_match = true;
        for (int n: r) {
            const rule_t& new_rule = find_rule(ind, n);
            if (!match2(ind, new_rule, msg, offs2)) {
                is_match = false;
                break;
            }
        }
        if (is_match) {
            offs = offs2;
            return true;
        }
    }
    return false;
}

int validate1(const indata_t& ind) {
    int count = 0;
    for (auto& msg: ind.msg) {
        int offs = 0;
        if (match2(ind, find_rule(ind, 0), msg, offs) && offs == msg.size()) {
            count++;
        }
    }
    return count;
}

int validate2(const indata_t& ind) {
    int count = 0;
    for (auto& msg: ind.msg) {
        int offs = 0;

        int fts = 0;
        int els = 0;
        while(offs < msg.size() && match2(ind, find_rule(ind, 42), msg, offs)) { fts++; }
        while(offs < msg.size() && match2(ind, find_rule(ind, 31), msg, offs)) { els++; }
        if (offs == msg.size() && fts > els && els > 0) {
            count++;
        }
    }
    return count;
}

/*
0: 8 11
8: 42 | 42 8
(8 = 42+)
11: 42 31 | 42 11 31
(11 = 42{n} 31{n})
*/

void check(const indata_t& ind, const std::string& s) {
    int offs = 0;
    bool f = match2(ind, find_rule(ind, 0), s, offs);
    if (f) {
        std::cout << s << " matches " << offs << std::endl;
    }
}

int main(int argc, char** argv) {
    auto indata = parse("input");

    int part1 = validate1(indata);
    int part2 = validate2(indata);
    std::cout << part1 << std::endl;
    std::cout << part2 << std::endl;

    return 0;
}
