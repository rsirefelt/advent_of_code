#include <iostream>
#include <fstream>
#include <string>
#include <vector>

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
    // Read the input data into a vector of ints
    auto lines = readLines("/home/carl/CLionProjects/AdventOfCode/Day1/input.txt");
    std::vector<unsigned long int> numbers;
    for (auto line : lines) {
        numbers.push_back(std::stoi(line));
    }

    // Find the triplet of entries that sum to 2020
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i+1; j < numbers.size(); j++) {
            for (int k = j + 1; k < numbers.size(); k++) {
                if (numbers[i] + numbers[j] + numbers[k] == 2020) {
                    std::cout << numbers[i] * numbers[j] * numbers[k] << "\n";
                }
            }
        }
    }

    return 0;
}
