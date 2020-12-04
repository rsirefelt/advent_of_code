#include "ctl.hh"

#include <iostream>

using passpt = std::map<std::string, std::string>;

bool validate1(const passpt& p) {
    static std::set<std::string> required_keys =
        { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" };    
    return is_subset(map_keys(p), required_keys);
}

bool validate2(const passpt& p) {
    if (!in_range(1920, std::stoi(p.at("byr")), 2002)) return false;
    if (!in_range(2010, std::stoi(p.at("iyr")), 2020)) return false;
    if (!in_range(2020, std::stoi(p.at("eyr")), 2030)) return false;
    if (ends_with(p.at("hgt"), "in")) {
        if (!in_range(59, std::stoi(slice(p.at("hgt"), 0, -2)), 76))  return false;
    } else if (ends_with(p.at("hgt"), "cm")) {
        if (!in_range(150, std::stoi(slice(p.at("hgt"), 0, -2)), 193))  return false;
    } else {
        return false;
    }
    const std::string& hcl = p.at("hcl");
    if (hcl[0] != '#' || !std::all_of(hcl.cbegin() + 1, hcl.cend(), is_hex)) return false;
    static std::set<std::string> valid_ecl = { "amb", "blu", "brn", "gry", "grn", "hzl", "oth"};
    if (valid_ecl.find(p.at("ecl")) == valid_ecl.end()) return false;
    const std::string& pid = p.at("pid");
    if (pid.length() != 9 || !std::all_of(pid.begin(), pid.end(), isdigit)) return false;
    return true;
}

std::vector<passpt> parse(const std::string& filename) {
    using stringvec = std::vector<std::string>;
    auto passports = map([](const auto& s) {
        return split(strip(replace(s, '\n', ' ')), " ");
    }, split(read_file(filename), "\n\n"));
    return map([](const stringvec& sv) {
        return make_map(map([](const auto& kvstr) {
            return make_pair(split(kvstr, ":"));
        }, sv));
    }, passports);
}

int main(int argc, char** argv) {
    std::vector<passpt> valid1 = filter(parse("input"), validate1);
    std::cout << valid1.size() << std::endl;
    std::cout << filter(valid1, validate2).size() << std::endl;
    return 0;
}
