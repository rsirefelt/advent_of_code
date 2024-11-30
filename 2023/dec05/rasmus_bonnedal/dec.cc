#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>

using namespace std;
using namespace ctl;

struct range {
    uint64_t source_range_start;
    uint64_t dest_range_start;
    uint64_t length;
};

struct smap {
    vector<range> ranges;
    string from;
    string to;
};


struct indata {
    vector<uint64_t> seeds;
    std::map<string, smap> maps;
};

indata parse(const std::string& filename) {
    indata data;
    smap sm;
    for (const auto& s : split(read_file(filename), "\n")) {
        if (s.find("seeds:") != string::npos) {
            data.seeds = ctl::map(ctl::stoull, split(split(s, ":")[1], " "));
        }
        else if (s.find(" map:") != string::npos) {
            if (!sm.from.empty()) {
                data.maps[sm.from] = std::move(sm);
            }
            sm = smap();
            auto v = split(split(s, " ")[0], "-");
            sm.from = v[0];
            sm.to = v[2];
        }
        else if (!s.empty()) {
            auto x = ctl::map(ctl::stoull, split(s, " "));
            sm.ranges.push_back({ x[1], x[0], x[2] });
        }
    }
    if (!sm.from.empty()) {
        data.maps[sm.from] = std::move(sm);
    }
    sm = smap();
    return data;
}

uint64_t part1(const indata& data) {
#if 0
    print("seeds: ");
    for (auto s : data.seeds) {
        print("{} ", s);
    }
    print("\n");

    for (const auto& [k, v] : data.maps) {
        print("{}-to-{} map:\n", v.from, v.to);
        for (const auto& range : v.ranges) {
            print("src: [{}, {}], dest: [{}, {}]\n", range.source_range_start, range.source_range_start + range.length, range.dest_range_start, range.dest_range_start + range.length);
        }
    }
#endif
    uint64_t result = 0xffffffffffffffff;
    for (auto seed : data.seeds) {
        string type = "seed";
        auto value = seed;
        while (type != "location") {
            print("{}: {}\n", type, value);
            const smap& sm = data.maps.at(type);
            for (const auto& range : sm.ranges) {
                if (value >= range.source_range_start && value < (range.source_range_start + range.length)) {
                    value = value - range.source_range_start + range.dest_range_start;
                    break;
                }
            }
            type = sm.to;
        }
        print("seed: {}, location: {}\n", seed, value);
        result = min(result, value);
    }
    return result;
}

uint64_t part2(const indata& data) {
    uint64_t result = 0xffffffffffffffff;
    for (int i = 0; i < data.seeds.size(); i += 2) {
        print("Seed range {}: {} {}\n", i, data.seeds[i], data.seeds[i + 1]);
        for (uint64_t seed = data.seeds[i]; seed < (data.seeds[i] + data.seeds[i + 1]); seed++) {
            string type = "seed";
            auto value = seed;
            while (type != "location") {
                // print("{}: {}\n", type, value);
                const smap& sm = data.maps.at(type);
                for (const auto& range : sm.ranges) {
                    if (value >= range.source_range_start && value < (range.source_range_start + range.length)) {
                        value = value - range.source_range_start + range.dest_range_start;
                        break;
                    }
                }
                type = sm.to;
            }
            //print("seed: {}, location: {}\n", seed, value);
            result = min(result, value);
        }
    }
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
