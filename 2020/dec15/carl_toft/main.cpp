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

int main() {
    const unsigned long long int MAX_ITERS = 30000000;

    // Read the puzzle input
    std::vector<std::string> input = readLines("/home/carl/CLionProjects/AdventOfCode/Day15/input.txt");
    std::vector<unsigned long long int> numbers(MAX_ITERS);
    std::vector<std::string> numbers_as_strings = splitString(input[0], ',');
    for (int i = 0; i < numbers_as_strings.size(); i++)
        numbers[i] = std::stoi(numbers_as_strings[i]);

    // Store the indices for each spoken word in an array
    std::vector<long long int> last_observation(MAX_ITERS);
    for (unsigned long long int i = 0; i < MAX_ITERS; i++)
        last_observation[i] = -1;
    for (int i = 0; i < numbers_as_strings.size(); i++) {
        last_observation[numbers[i]] = i;
    }

    unsigned long long int next_number;
    for (unsigned long long int i = numbers_as_strings.size(); i < MAX_ITERS; i++) {
        // Check if the previous number has been said before
        if (last_observation[numbers[i-1]] == -1) {
            // The last number had not been said previously
            numbers[i] = 0;
            last_observation[numbers[i-1]] = i-1;
            continue;
        } else {
            // It has been said previously. The next number is the difference between
            // the last two times it was said.
            next_number = (i-1) - last_observation[numbers[i-1]];
            numbers[i] = next_number;
            last_observation[numbers[i-1]] = i-1;
        }
    }

    std::cout << "Part 2: " << numbers[numbers.size()-1] << "\n";

    return 0;
}
