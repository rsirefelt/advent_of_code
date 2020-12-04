#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <regex>
#include <set>
#include <vector>

using passpt = std::map<std::string, std::string>;
using passpvec = std::vector<passpt>;

void process_line(const std::string& line, passpt& passp) {
    static std::regex re("(\\w+):([\\w#]+)");
    auto pos = line.cbegin();
    std::smatch match;
    while(std::regex_search(pos, line.cend(), match, re)) {
        passp[match[1].str()] = match[2].str();
        pos += match.position() + match.length();
    }
}

passpvec parse(const std::string& filename) {
    passpvec retval;
    std::ifstream ifs(filename);
    if (ifs.fail()) {
        throw std::runtime_error("Could not open file");
    }

    passpt passp;
    std::string line;
    while(std::getline(ifs, line)) {
        if (line.empty()) {
            retval.push_back(std::move(passp));
        } else {
            process_line(line, passp);
        }
    }
    retval.push_back(std::move(passp));
    return retval;
}

bool validate(const passpt& p) {
    auto required = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" };
    for (auto& field : required) {
        if (p.find(field) == p.end()) {
            return false;
        }
    }
    return true;
}

bool validate_height(const std::string& hgt) {
    static std::regex re_cm("(\\d+)cm");
    static std::regex re_in("(\\d+)in");
    std::smatch match;
    if (std::regex_match(hgt, match, re_cm)) {
        int h = std::stoi(match[1].str());
        if (h >= 150 && h <= 193) {
            return true;
        }
    }
    if (std::regex_match(hgt, match, re_in)) {
        int h = std::stoi(match[1].str());
        if (h >= 59 && h <= 76) {
            return true;
        }
    }
    return false;

}

bool validate2(passpt& p) {
    try {
        int byr = std::stoi(p["byr"]);
        if (byr < 1920 || byr > 2002) return false;
        int iyr = std::stoi(p["iyr"]);
        if (iyr < 2010 || iyr > 2020) return false;
        int eyr = std::stoi(p["eyr"]);
        if (eyr < 2020 || eyr > 2030) return false;
        if (!validate_height(p["hgt"])) return false;
        static std::regex re_hcl("#[0-9a-f]{6}");
        std::smatch m;
        if (!std::regex_match(p["hcl"], m, re_hcl)) return false;
        static std::set<std::string> valid_ecl = { "amb", "blu", "brn", "gry", "grn", "hzl", "oth"};
        if (valid_ecl.find(p["ecl"]) == valid_ecl.end()) return false;
        static std::regex re_pid("[0-9]{9}");
        if (!std::regex_match(p["pid"], m, re_pid)) return false;
        return true;
    } catch(...) {
        return false;
    }
}

int main(int argc, char** argv) {
    auto indata = parse("input");

    int valids = 0;
    int valids2 = 0;
    for (auto& p: indata) {
        if (validate(p)) {
            valids++;
            if (validate2(p)) {
                valids2++;
            }
        }
    }
    std::cout << "part 1: " << valids << std::endl;
    std::cout << "part 2: " << valids2 << std::endl;
    return 0;
}
