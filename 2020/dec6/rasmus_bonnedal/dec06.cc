#include "ctl.hh"

#include <iostream>
#include <iterator>

using indata = std::vector<std::vector<std::string>>;

indata parse(const std::string& filename) {
    return map([](const auto& s) {
        return split(s, "\n");
    }, split(read_file(filename), "\n\n"));
}

int calc_group_union(const std::vector<std::string>& group) {
    return set_union(group).size();
}

int calc_group_intersect(const std::vector<std::string>& group) {
    return intersection(map(make_set<std::string>, group)).size();
}

int main(int argc, char** argv) {
    indata data = parse("input");
    std::cout << "Part 1: " << sum(map(calc_group_union, data)) << std::endl;
    std::cout << "Part 2: " << sum(map(calc_group_intersect, data)) << std::endl;
    return 0;
}
