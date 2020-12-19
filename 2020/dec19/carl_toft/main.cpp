#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>

long long int toInt(std::string num) {
    unsigned long int multiplier = 1;
    long long int number = 0;
    for (int idx = num.length()-1; idx >= 0; idx--) {
        number = number + multiplier*(int(num.at(idx))-48);
        multiplier *= 10;
    }
    return number;
}

std::vector<std::string> splitString(std::string line, char delimiter) {
    std::vector<std::string> substrings;

    // First, find all occurences of the delimiter
    std::vector<long int> delimiter_indices;
    delimiter_indices.push_back(-1);
    for (long int i = 0; i < line.length(); i++) {
        if (line.at(i) == delimiter) {
            delimiter_indices.push_back(i);
        }
    }
    delimiter_indices.push_back(line.length());

    // Now that we have found all the delimiters, split the string into
    // appropriate substrings
    unsigned int substring_length = 0;
    for (unsigned int i = 0; i < delimiter_indices.size() - 1; i++) {
        substring_length = delimiter_indices[i+1] - delimiter_indices[i] - 1;
        substrings.push_back(line.substr(delimiter_indices[i]+1, substring_length));
    }

    return substrings;
}

// This function reads the .txt file given as input, and returns its lines
// as a vector of strings. The last line is not included if it is empty.
// If the file can not be opened for reading it terminates the program.
std::vector<std::string> readLines(std::string filename) {
    std::vector<std::string> lines; // to be returned
    std::string line;               // will hold each individual line

    // Open file
    std::ifstream file(filename);
    if (file.is_open()) {
        // Read the lines one by one and add to vector "lines"
        while (getline(file, line)) {
            lines.push_back(line);
        }
    }
    else {
        // File failed to open for some reason. Report the error and exit the program.
        std::cout << "FAILED TO OPEN FILE: " << filename << "\nAborting...";
        exit(0);
    }

    // Remove the last line if it is empty (equal to "")
    if (lines.back() == "") {
        lines.pop_back();
    }

    // Done!
    return lines;
}

std::vector<std::string> findAllCombinations(std::vector<std::vector<std::string>> strings) {
    if (strings.size() == 1)
        return strings[0];

    std::vector<std::string> all_combinations;
    if (strings.size() == 2) {
        for (int i = 0; i < strings[0].size(); i++) {
            for (int j = 0; j < strings[1].size(); j++) {
                all_combinations.push_back(strings[0][i] + strings[1][j]);
            }
        }
        return all_combinations;
    } else {
        std::vector<std::vector<std::string>> new_list;

        std::vector<std::vector<std::string>> first_two;
        first_two.push_back(strings[0]);
        first_two.push_back(strings[1]);
        std::vector<std::string> first_two_merged = findAllCombinations(first_two);
        new_list.push_back(first_two_merged);

        for (int i = 2; i < strings.size(); i++) {
            new_list.push_back(strings[i]);
        }

        return findAllCombinations(new_list);
    }
}

struct Rule {
    long long int rule_number;
    std::vector<std::string> strings_that_match;
    bool computed_rule = false;
    bool isSingleCharRule;
    char character;
    std::vector<std::vector<Rule*>> sub_rules; // a list with potentially two lists of sub rules
    std::vector<std::string> getMatchingStrings(); // apply the rule to a message

    Rule() {rule_number = -1; isSingleCharRule = false; character = 'X'; }
};

std::vector<std::string> Rule::getMatchingStrings() {
    if (computed_rule == true)
        return strings_that_match;

    // First, consider the base case
    if (isSingleCharRule == true) {
        strings_that_match.push_back(std::string(1, character));
        computed_rule = true;
        return strings_that_match;
    }

    // Now, consider the case where we have several rules
    std::vector<std::vector<std::string>> matching_strings_for_sub_rules;
    for (int i = 0; i < sub_rules[0].size(); i++) {
        matching_strings_for_sub_rules.push_back(sub_rules[0][i]->getMatchingStrings()); // HERE WE MUST CHANGE THE ZERO!!! WE ONLY ADDRES THE FIRST SUB RULE OPTION NOW!!!
    }
    std::vector<std::string> matching_strings = findAllCombinations(matching_strings_for_sub_rules);

    if (sub_rules.size() > 1) {
        matching_strings_for_sub_rules.clear();
        for (int i = 0; i < sub_rules[1].size(); i++) {
            matching_strings_for_sub_rules.push_back(sub_rules[1][i]->getMatchingStrings()); // HERE WE MUST CHANGE THE ZERO!!! WE ONLY ADDRES THE FIRST SUB RULE OPTION NOW!!!
        }
        std::vector<std::string> matching_strings_subrule1 = findAllCombinations(matching_strings_for_sub_rules);
        for (int k = 0; k < matching_strings_subrule1.size(); k++)
            matching_strings.push_back(matching_strings_subrule1[k]);

    }

    strings_that_match = matching_strings;
    computed_rule = true;
    return strings_that_match;

}

bool isStringInVector(std::string message, std::vector<std::string> messages) {
    for (int i = 0; i < messages.size(); i++) {
        if (message == messages[i])
            return true;
    }

    return false;
}

bool isStringValidAccordingToNewRules(std::string message, std::vector<std::string> valid_messages_42, std::vector<std::string> valid_messages_31) {
    unsigned int len = valid_messages_42[0].length();
        unsigned long int num_42 = 0;
        while (message.length() >= len) {
            if (isStringInVector(message.substr(0, len), valid_messages_42)) {
                message = message.substr(len, message.length() - len);
                num_42++;
            } else
                break;
        }

        len = valid_messages_31[0].length();
        unsigned long int num_31 = 0;
        while (message.length() >= len) {
            if (isStringInVector(message.substr(0, len), valid_messages_31)) {
                message = message.substr(len, message.length() - len);
                num_31++;
            } else
                break;
        }

    if (message.length() == 0 && num_42 > 0 && num_31 > 0 && num_42 > num_31)
        return true;
    else
        return false;

}

int main() {
    // Parse the puzzle input
    std::vector<std::string> input = readLines("/home/carl/CLionProjects/AdventOfCode/Day19/input.txt");
    std::vector<Rule> rules;

    // First, create all the rules
    for (unsigned long long int i = 0; i < input.size(); i++) {
        if (input[i] == "")
            break;
        auto parts = splitString(input[i], ':');
        unsigned long long int rule_number = toInt(parts[0]);
        Rule rule;
        rule.rule_number = rule_number;
        if (parts[1].at(2) == 'a' || parts[1].at(2) == 'b') {
            rule.isSingleCharRule = true;
            rule.character = parts[1].at(2);
        }
        rules.push_back(rule);
    }

    // Now, assign all the subrules
    for (unsigned long int i = 0; i < rules.size(); i++) {
        if (rules[i].isSingleCharRule == true)
            continue;
        auto parts = splitString(input[i], ':');
        auto sub_rules = splitString(parts[1], '|');
        if (sub_rules.size() == 1)
            sub_rules[0] = sub_rules[0].substr(1, sub_rules[0].length()-1);
        else
            sub_rules[0] = sub_rules[0].substr(1, sub_rules[0].length()-2);
        for (int i = 1; i < sub_rules.size(); i++) {
            if (i == sub_rules.size()-1)
                sub_rules[i] = sub_rules[i].substr(1, sub_rules[i].length() - 1);
            else
                sub_rules[i] = sub_rules[i].substr(1, sub_rules[i].length()-2); // this is probably never used, but whatever
        }

        for (int ii = 0; ii < sub_rules.size(); ii++) {
            std::vector<Rule*> sub_rule_list;
            auto rules_to_use = splitString(sub_rules[ii], ' ');
            for (int j = 0; j < rules_to_use.size(); j++) {
                for (int k = 0; k < rules.size(); k++) {
                    if (rules[k].rule_number == toInt(rules_to_use[j]))
                        sub_rule_list.push_back(&rules[k]);
                }
            }
            rules[i].sub_rules.push_back(sub_rule_list);
        }
    }

    // With the puzzle input successfully parsed. Read all the messages
    std::vector<std::string> messages;
    unsigned long int i;
    for (i = 0; i < input.size(); i++) {
        if (input[i] == "")
            break;
    }
    i++;
    for (; i < input.size(); i++) {
        messages.push_back(input[i]);
    }

    // Now, go through the messages and count how many are valid according to rule 0. First, find the index of rule 0
    unsigned long long int rule_0_index;
    for (int i = 0; i < rules.size(); i++) {
        if (rules[i].rule_number == 0)
            rule_0_index = i;
    }
    /*for (int i = 0; i < valid_messages_42.size(); i++) {
        if (isStringInVector(valid_messages_42[i], valid_messages_31))
            std::cout << valid_messages_42[i] << "\n";
    }*/

    unsigned long long int num_valid_messages = 0;
    std::vector<std::string> valid_messages = rules[rule_0_index].getMatchingStrings();
    for (int i = 0; i < messages.size(); i++) {
        if (isStringInVector(messages[i], valid_messages))
            num_valid_messages++;
    }

    std::cout << "Part 1: " << num_valid_messages << "\n";

    // Solve part 2
    std::vector<std::string> valid_messages_42 = rules[20].getMatchingStrings();
    std::vector<std::string> valid_messages_31 = rules[38].getMatchingStrings();
    num_valid_messages = 0;
    for (int i = 0; i < messages.size(); i++) {
        if (isStringValidAccordingToNewRules(messages[i], valid_messages_42, valid_messages_31)) {
            num_valid_messages++;
        }
    }
    std::cout << "Part 2: " << num_valid_messages << "\n";

    return 0;
}







