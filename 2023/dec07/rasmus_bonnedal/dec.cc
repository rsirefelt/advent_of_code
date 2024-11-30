#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>

using namespace std;
using namespace ctl;

enum Kind {
    FIVE = 0,
    FOUR = 1,
    FULL_HOUSE = 2,
    THREE = 3,
    TWO_PAIR = 4,
    ONE_PAIR = 5,
    HIGH = 6
};

struct hand {
    string cards;
    int bid;
    Kind kind;
};

bool operator<(const hand& lhs, const hand& rhs) {
    if (lhs.kind != rhs.kind) {
        return lhs.kind < rhs.kind;
    }
    const std::string FROM = "AKQJT98765432";
    const std::string TO =   "abcdefghijklm";
    return translate(lhs.cards, FROM, TO) < translate(rhs.cards, FROM, TO);
}

bool compare_j(const hand& lhs, const hand& rhs) {
    if (lhs.kind != rhs.kind) {
        return lhs.kind < rhs.kind;
    }
    const std::string FROM = "AKQT98765432J";
    const std::string TO = "abcdefghijklm";
    return translate(lhs.cards, FROM, TO) < translate(rhs.cards, FROM, TO);
}

struct indata {
    vector<hand> hands;
};

Kind categorize(const std::string& cards) {
    struct Count {
        int i = 0;
    };
    std::map<char, Count> counts;
    for (char c : cards) {
        counts[c].i++;
    }
    vector<int> histogram;
    for (const auto& [k, v] : counts) {
        histogram.push_back(v.i);
    }
    sort(histogram);
    std::reverse(histogram.begin(), histogram.end());
    if (histogram[0] == 5) {
        return FIVE;
    }
    else if (histogram[0] == 4) {
        return FOUR;
    }
    else if (histogram[0] == 3 && histogram[1] == 2) {
        return FULL_HOUSE;
    }
    else if (histogram[0] == 3) {
        return THREE;
    }
    else if (histogram[0] == 2 && histogram[1] == 2) {
        return TWO_PAIR;
    }
    else if (histogram[0] == 2) {
        return ONE_PAIR;
    }
    else {
        return HIGH;
    }
    throw std::runtime_error("Unknown hand " + cards);
}

Kind categorize_j(const std::string& cards) {
    int best = 99;
    for (char c : string("AKQT98765432")) {
        best = std::min(best, (int)categorize(replace(cards, 'J', c)));
    }
    return (Kind)best;
}

indata parse(const std::string& filename) {
    indata data;
    for (const auto& s : split(read_file(filename), "\n")) {
        hand h;
        auto v = split(s, " ");
        data.hands.push_back({ v[0], stoint(v[1]), categorize(v[0])});
    }
    return data;
}

int64_t part1(const indata& data) {
    int64_t result = 0;
    auto hands = sorted(data.hands);
    int rank = (int)hands.size();
    for (const auto& hand : hands) {
        result += rank * hand.bid;
        rank--;
    }
    CHECK(result == 248453531);
    return result;
}

int part2(const indata& data) {
    int result = 0;
    indata d = data;
    for (auto& h : d.hands) {
        h.kind = categorize_j(h.cards);
    }
    std::sort(d.hands.begin(), d.hands.end(), compare_j);
    int rank = (int)d.hands.size();
    for (const auto& hand : d.hands) {
        result += rank * hand.bid;
        rank--;
    }
    return result;
}

void test() {
    CHECK(categorize("22JJA") == TWO_PAIR);
    CHECK(categorize("KK677") == TWO_PAIR);
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
