#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>
#include <regex>

using namespace std;
using namespace ctl;

struct row {
    string s;
    vector<int> damaged;
    int damaged_size;
};

string to_string(const vector<int>& v) {
    string result;
    for (int i = 0; i < v.size(); ++i) {
        result += to_string(v[i]);
        if (i < (v.size() - 1)) {
            result += ", ";
        }
    }
    return result;
}

using indata = vector<row>;

indata parse(const std::string& filename) {
    indata d;
    for (const auto& s : split(read_file(filename), "\n")) {
        auto v = split(s, " ");
        d.push_back({ v[0], mapf(stoint, split(v[1], ",")) });
        d.back().damaged_size = (int)d.back().damaged.size();
    }
    return d;
}

struct iter_state {
    unsigned char current_damage = 0;
    unsigned char damage_pos = 0;
    unsigned char str_pos = 0;
};

// Returns true if mismatch
bool handle_eod(const row& r, iter_state& s) {
    if (s.current_damage > 0) {
        if (s.damage_pos >= r.damaged.size()) {
            return true;
        }
        if (r.damaged[s.damage_pos] == s.current_damage) {
            s.current_damage = 0;
            s.damage_pos++;
        }
        else {
            return true;
        }
    }
    return false;

}

struct cache_t {
    map<pair<string, vector<int>>, int64_t> c;

    void add(const string& s, const vector<int>& v, int64_t count) {
        c[make_pair(s, v)] = count;
    }

    bool find(const string& s, const vector<int>& v, int64_t& count) {
        auto p = make_pair(s, v);
        if (c.count(p)) {
            count = c[p];
            return true;
        }
        return false;
    }

};

int64_t _match_damage2(const row& r, iter_state& s, cache_t& cache) {
    if (s.current_damage > 0) {
        throw runtime_error("AAARGH");
    }
    string ss = r.s.substr(s.str_pos);
    vector vv(r.damaged.begin() + s.damage_pos, r.damaged.end());
    int64_t count = 0;

    if (cache.find(ss, vv, count)) {
        return count;
    }

    int n_s = (int)r.s.size();
    while (s.str_pos < n_s) {
        char c = r.s[s.str_pos++];
        if (c == '.') {
            if (handle_eod(r, s)) {
                cache.add(ss, vv, count);
                return count;
            }
        }
        else if (c == '#') {
            bool damage_ok = s.damage_pos < r.damaged_size && s.current_damage < r.damaged[s.damage_pos];
            s.current_damage++;
            if (!damage_ok) {
                cache.add(ss, vv, count);
                return count;
            }
        }
        else if (c == '?') {
            // '.' case
            iter_state state_dot = s;
            if (!handle_eod(r, state_dot)) {
                count += _match_damage2(r, state_dot, cache);
            }

            bool damage_ok = s.damage_pos < r.damaged_size && s.current_damage < r.damaged[s.damage_pos];
            s.current_damage++;
            if (!damage_ok) {
                cache.add(ss, vv, count);
                return count;
            }
        }
    }
    if (handle_eod(r, s)) {
        cache.add(ss, vv, count);
        return count;
    }
    if (s.damage_pos == r.damaged_size) {
        count++;
    }
    cache.add(ss, vv, count);
    return count;
}

int64_t match_damage2(const row& r) {
    iter_state is;
    cache_t cache;
    return _match_damage2(r, is, cache);
}

int64_t match_n(const row& r, int n) {
    string sn;
    sn.reserve(r.s.size() * n + (n - 1));
    for (int i = 0; i < n; ++i) {
        sn += r.s;
        if (i < (n - 1)) sn += '?';
    }
    int q = (int)count(sn, '?');
    return match_damage2(row{ sn, dup(r.damaged, n), (int)r.damaged.size() * n });
}

int64_t part1(const indata& data) {
    int64_t result = 0;
    timer t;
    for (const row& r: data) {
        int64_t dot_end = 0;
        result += match_damage2(r);
    }
    print("{:.2f} s\n", t());
    return result;
}

// 298505635139 too low
int64_t part2(const indata& data, int max_row) {
    int64_t result = 0;
    timer t;
    int i = 0;
    for (int row_num = 0; row_num < max_row; ++row_num) {
        const row& r = data[row_num];
        timer t;
        int64_t e = match_n(r, 5);
        result += e;
    }
    print("{:.3f} s\n", t());
    return result;
}

int main(int argc, char** argv) {
    try {
        bool test = false;
        auto data = parse(test ? "..\\test1.txt" : "..\\input.txt");
        print("part1: {}\n", part1(data));
        int64_t p2 = part2(data, (int)data.size());
        print("part2: {}\n", p2);
    }
    catch (const exception& e) {
        print("Error: {}\n", e.what());
    }
    return 0;
}
