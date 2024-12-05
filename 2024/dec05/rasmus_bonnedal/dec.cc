#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>
#include <regex>

using namespace std;
using namespace ctl;

using pr = pair<int, int>;

struct book {
    vector<int> pages;
    std::map<int, int> page_to_index;
};

struct indata {
    vector<pr> rules;
    vector<book> books;
};

indata parse(const std::string& filename) {
    indata d;
    for (const auto& s : split(read_file(filename), "\n")) {
        if (s.find('|') != string::npos) {
            auto v = ctl::map(stoint, split(s, "|"));
            d.rules.push_back({ v[0], v[1] });
        } else {
            d.books.push_back({ ctl::map(stoint, split(s, ",")) });
        }
    }
    for (auto& book : d.books) {
        for (int i = 0; i < (int)book.pages.size(); ++i) {
            book.page_to_index[book.pages[i]] = i;
        }
    }
    return d;
}

int64_t part1(const indata& data) {
    int64_t result = 0;
    for (const auto& book : data.books) {
        bool success = true;
        for (const auto& rule : data.rules) {
            if (book.page_to_index.count(rule.first) > 0 && book.page_to_index.count(rule.second)) {
                int i1 = book.page_to_index.at(rule.first);
                int i2 = book.page_to_index.at(rule.second);
                if (i1 >= i2) {
                    success = false;
                }
            }
        }
        if (success) {
            result += book.pages[book.pages.size() / 2];
        }
    }
    return result;
}

int64_t part2(const indata& data) {
    int64_t result = 0;

    indata d = data;
    int book_id = 0;
    for (auto& book : d.books) {
        bool success = true;
        int changes;
        do {
            changes = 0;
            for (int i = 0; i < book.pages.size() - 1; ++i) {
                int p0 = book.pages[i];
                int p1 = book.pages[i + 1];
                for (const auto& rule : data.rules) {
                    if (rule.first == p0 && rule.second == p1) {
                        // correct order
                    }
                    else if (rule.first == p1 && rule.second == p0) {
                        success = false;
                        changes++;
                        std::swap(book.pages[i], book.pages[i + 1]);
                    }
                }
            }
        } while (changes > 0);
        if (!success) {
            result += book.pages[book.pages.size() / 2];
        }
        book_id++;
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
