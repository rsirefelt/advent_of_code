#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>

using stringvec = std::vector<std::string>;

struct cont_t {
    std::vector<std::string> ingredients;
    std::vector<std::string> allergens;
};

using indata_t = std::vector<cont_t>;

cont_t parse_cont(const std::string& line) {
    auto s = split(line, " (contains ");
    cont_t retval;
    retval.ingredients = split(s[0], " ");
    if (s.size() == 2) {
        retval.allergens = split(split(s[1], ")")[0], ", ");
    }
    return retval;
}

indata_t parse(const std::string& filename) {
    return map(parse_cont, split(read_file(filename), "\n"));
}

struct allergen_t {
    std::vector<stringvec> ingredients;
};

struct DefInt {
    int i = 0;
};

int part1(indata_t& indata) {
    std::map<std::string, allergen_t> allergenmap;
    std::set<std::string> allergenset;
    for (auto& cont: indata) {
        for (auto& all: cont.allergens) {
            allergenset.insert(all);
            allergen_t& allergen = allergenmap[all];
            allergen.ingredients.push_back(cont.ingredients);
        }
    }

    std::set<std::string> found_ingredients;

    std::vector<std::pair<std::string, std::string>> allingvec;

    while(!allergenset.empty()) {
        for (auto& allergen: allergenmap) {
            if (!in(allergen.first, allergenset)) continue;
            std::vector<std::set<std::string>> sets;
            for (auto& ing: allergen.second.ingredients) {
                sets.push_back(make_set(ing));
                for (auto& found: found_ingredients) {
                    sets.back().erase(found);
                }
            }
            auto inters = intersection(sets);
            if (inters.size() == 0) {
                assert(false);
            } else if (inters.size() == 1) {
                allergenset.erase(allergen.first);
                found_ingredients.insert(*inters.begin());
                allingvec.push_back(std::make_pair(allergen.first, *inters.begin()));
                std::cout << allergen.first << " is " << *inters.begin() << std::endl;
            }
        }
    }

    std::map<std::string, DefInt> ingredient_count;
    for (auto& i: indata) {
        for (auto& ingredient: i.ingredients) {
            if (!in(ingredient, found_ingredients)) {
                ingredient_count[ingredient].i++;
            }
        }
    }
    int total = 0;
    for (auto& i: ingredient_count) {
        total += i.second.i;
    }

    sort(allingvec);
    for (auto& alling: allingvec) {
        std::cout << alling.second << ",";
    }

    return total;
}

int main(int argc, char** argv) {
    auto indata = parse("input");

    std::cout << part1(indata) << std::endl;
    return 0;
}
