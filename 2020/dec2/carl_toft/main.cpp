#include <iostream>
#include <fstream>
#include <vector>
#include <string>

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

void parseInput(unsigned int &min, unsigned int &max, char &character, std::string &password, std::string input_line) {
    auto substrings = splitString(input_line, ' ');
    auto min_max_strings = splitString(substrings[0], '-');
    min = std::stoi(min_max_strings[0]);
    max = std::stoi(min_max_strings[1]);
    character = substrings[1].at(0);
    password = substrings[2];
}

bool validatePassword(unsigned int min, unsigned int max, char character, std::string password) {
    unsigned int count = 0;
    for (unsigned int i = 0; i < password.length(); i++) {
        if (password.at(i) == character)
            count++;
    }

    if (min <= count && count <= max)
        return true;
    return false;
}

bool validatePassword2(unsigned int min, unsigned int max, char character, std::string password) {
    if (password.at(min-1) == character && password.at(max-1) != character)
        return true;
    if (password.at(max-1) == character && password.at(min-1) != character)
        return true;
    return false;
}

int main() {
    // Read the puzzle input
    std::vector<std::string> lines = readLines("/home/carl/CLionProjects/AdventOfCode/Day2/input.txt");

    unsigned int min, max;
    char character;
    std::string password;

    // Parse each line, and check its validity
    unsigned int num_ok = 0;
    for (std::string line : lines) {
        parseInput(min, max, character, password, line);
        bool is_password_ok = validatePassword2(min, max, character, password);
        if (is_password_ok)
            num_ok++;
    }

    std::cout << num_ok << "\n";
    return 0;
}





