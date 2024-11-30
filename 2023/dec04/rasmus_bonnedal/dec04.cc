#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>

using namespace std;
using namespace ctl;

struct card {
    vector<int> winners;
    vector<int> numbers;
};

using indata = vector<card>;

indata parse(const std::string& filename) {
    indata data;
    for (const auto& s : split(read_file(filename), "\n")) {
        auto v2 = split(split(s, ":")[1], "|");
        data.push_back({ ctl::map(stoint, split(v2[0], " ")) , ctl::map(stoint, split(v2[1], " ")) });
    }
    return data;
}

int winners(const card& c) {
    return (int)intersection(vector<set<int>>({ make_set(c.winners), make_set(c.numbers) })).size();
}

int part1(const indata& data) {
    return sum(ctl::map([](const card& c) { return 1 << (winners(c) - 1); }, data));
}

int part2(const indata& data) {
    int n_data = (int)data.size();
    vector<int> cards(n_data, 1);
    for (int i = 0; i < n_data; ++i) {
        int w = winners(data[i]);
        for (int j = i + 1; j < min(i + 1 + w, n_data); ++j) {
            cards[j] += cards[i];
        }
    }
    return sum(cards);
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
