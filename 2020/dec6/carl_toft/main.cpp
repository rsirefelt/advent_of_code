#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>

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

std::set<char> intersectSets(std::vector<std::set<char>> sets) {
    std::set<char> intersection;
    for (char entry : sets[0]) {
        bool add = true;
        for (int j = 1; j < sets.size(); j++) {
            if (sets[j].count(entry) == 0)
                add = false;
        }
        if (add == true)
            intersection.insert(entry);
    }

    return intersection;
}

int main() {
    // Read the puzzle input
    std::vector<std::string> input = readLines("/home/carl/CLionProjects/AdventOfCode/Day6/input.txt");

    std::vector<std::set<char>> group_answers, persons_in_group_answers;
    std::set<char> current_group_answer, current_person_answer;
    for (std::string line : input) {
        // If the current line is a newline, save the current answer for the group and continue to next line
        if (line == "") {
            current_group_answer = intersectSets(persons_in_group_answers);
            group_answers.push_back(current_group_answer);
            current_group_answer.clear();
            persons_in_group_answers.clear();
            continue;
        }

        // Get answer of current person as a set
        current_person_answer.clear();
        for (int i = 0; i < line.length(); i++) {
            current_person_answer.insert(line.at(i));
        }
        persons_in_group_answers.push_back(current_person_answer);
    }

    unsigned long int sum = 0;
    for (int i = 0; i < group_answers.size(); i++) {
        sum += group_answers[i].size();
    }

    std::cout << sum << "\n";

    return 0;
}





















