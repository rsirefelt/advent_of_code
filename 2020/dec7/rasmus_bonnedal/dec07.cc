#include "ctl.hh"

#include <iostream>
#include <iterator>

using stringint = std::pair<std::string, int>;
using bagrule = std::pair<std::string, std::vector<stringint>>;
using stringvec = std::vector<std::string>;
using bagrulemap = std::map<std::string, std::vector<stringint>>;

std::string get_color(const std::string& line) {
    stringvec words = split(line, " ");
    return words[0] + " " + words[1];
}

// "5 foo bar" -> (5, "foo bar")
stringint parse_rule(const std::string& line) {
    stringvec words = split(line, " ");
    return std::make_pair(words[1] + " " + words[2], std::stoi(words[0]));
}

// "dim olive bags contain 2 dull silver bags, 4 posh blue bags." ->
// ("dim olive", [(2, "dull silver"), (4, "posh blue")])
bagrule parse_line(const std::string& line) {
    bagrule retval;
    stringvec sv = split(line, ",");
    stringvec first = split(sv[0], "contain ");
    retval.first = get_color(first[0]);
    if (first[1] != "no other bags.") {
        retval.second.push_back(parse_rule(first[1]));
    }
    for (size_t i = 1; i < sv.size(); ++i) {
        retval.second.push_back(parse_rule(sv[i]));
    }
    return retval;
}

bagrulemap parse(const std::string& filename) {
    return make_map(map(parse_line, split(read_file(filename), "\n")));
}

bool check_valid(const bagrulemap& brm, const std::string& bag_to_check, const std::string& bag_to_store) {
    const auto& br = brm.at(bag_to_check);
    return std::any_of(br.begin(), br.end(), [&](const auto& bag) {
        return bag.first == bag_to_store ||
            check_valid(brm, bag.first, bag_to_store); 
    });
}

int count_required(const bagrulemap& brm, const std::string& bag, int count = 0) {
    return count + sum(map([&brm](const auto& bagrule) {
        return bagrule.second * count_required(brm, bagrule.first, 1);
    }, brm.at(bag)));
}

int main(int argc, char** argv) {
    bagrulemap brm = parse("input");

    int part1 = count(map([&brm](const auto& bagrule) {
        return check_valid(brm, bagrule.first, "shiny gold"); 
    }, brm), true);

    std::cout << "Part 1: " << part1 << std::endl;
    std::cout << "Part 2: " << count_required(brm, "shiny gold") << std::endl;
    return 0;
}
