#include "ctl.hh"

#include <iostream>
#include <iterator>

using stringint = std::pair<std::string, int>;
struct bagrule {
    std::string _bag;
    std::vector<stringint> _rules;
};

using stringvec = std::vector<std::string>;
using bagrulemap = std::map<std::string, std::vector<stringint>>;

std::string get_color(const std::string& line) {
    stringvec words = split(line, " ");
    return words[0] + " " + words[1];
}

stringint parse_rule(const std::string& line) {
    stringint retval;
    stringvec words = split(line, " ");
    retval.second = std::stoi(words[0]);
    retval.first = words[1] + " " + words[2];
    return retval;
}

bagrule parse_line(const std::string& line) {
    bagrule retval;
    stringvec sv = split(line, ",");
    stringvec first = split(sv[0], "contain ");
    retval._bag = get_color(first[0]);
    if (first[1] != "no other bags.") {
        retval._rules.push_back(parse_rule(first[1]));
    }
    for (size_t i = 1; i < sv.size(); ++i) {
        retval._rules.push_back(parse_rule(sv[i]));
    }
    return retval;
}

bagrulemap parse(const std::string& filename) {
    bagrulemap brm;
    for (const auto& line: split(read_file(filename), "\n")) {
        bagrule br = parse_line(line);
        brm[std::move(br._bag)] = std::move(br._rules);
    }
    return brm;
}

bool check_valid(const bagrulemap& brm, const std::string& bag_to_check, const std::string& bag_to_store) {
    const std::vector<stringint>& br = brm.at(bag_to_check);
    for (auto& bag: br) {
        if (bag.first == bag_to_store) return true;
    }
    for (auto& bag: br) {
        if (check_valid(brm, bag.first, bag_to_store)) return true;
    }
    return false;
}

int count_required(const bagrulemap& brm, const std::string& bag, int count = 0) {
    const std::vector<stringint>& bagrules = brm.at(bag);
    for (auto& bagrule: bagrules) {
        count += bagrule.second * count_required(brm, bagrule.first, 1);
    }
    return count;
}

int main(int argc, char** argv) {
    bagrulemap brm = parse("input");

    int valids = 0;
    for (auto& rule: brm) {
        if (check_valid(brm, rule.first, "shiny gold")) valids++;
    }
    std::cout << "Part 1: " << valids << std::endl;
    std::cout << "Part 2: " << count_required(brm, "shiny gold") << std::endl;
    return 0;
}
