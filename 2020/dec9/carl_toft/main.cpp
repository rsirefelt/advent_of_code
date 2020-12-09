#include <iostream>
#include <fstream>
#include <vector>
#include <string>

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

bool isValid(std::vector<long int> numbers, unsigned int index_to_check, long int num_previous_nums) {
    for (int i = index_to_check-num_previous_nums; i < index_to_check; i++) {
        for (int j = index_to_check-num_previous_nums; j < index_to_check; j++) {
            if (i == j)
                continue;
            if (numbers[i] + numbers[j] == numbers[index_to_check])
                return true;
        }
    }

    return false;
}

long long int toInt(std::string num) {
    unsigned long int multiplier = 1;
    long long int number = 0;
    for (int idx = num.length()-1; idx >= 0; idx--) {
        number = number + multiplier*(int(num.at(idx))-48);
        multiplier *= 10;
    }
    return number;
}

int main() {
    // Read the puzzle input
    std::vector<std::string> input = readLines("/home/carl/CLionProjects/AdventOfCode/Day9/input.txt");
    std::vector<long int> numbers;
    for (std::string number : input)
        numbers.push_back(toInt(number));

    long int num_previous_nums = 25; // number of preceding numbers which should be used to compute current number

    // Check all numbers in the list to see if they are valid
    unsigned long long int invalid_number = 0;
    for (unsigned int i = num_previous_nums; i < numbers.size(); i++)  {
        if (isValid(numbers, i, num_previous_nums) == false) {
            invalid_number = numbers[i];
            std::cout << "Part 1: " << invalid_number << "\n";
            break;
        }
    }

    // Now we have found the invalid number. Find the numbers that sum to this
    for (unsigned long int i = 0; i < numbers.size(); i++) {
        unsigned long long int current_sum = 0, smallest = numbers[i], largest = numbers[i];
        for (int j = i; j < numbers.size(); j++) {
            current_sum += numbers[j];
            if (current_sum == invalid_number) {
                std::cout << "Part 2: " << smallest + largest << "\n";
                return 0;
            }

            if (numbers[j] > largest)
                largest = numbers[j];
            if (numbers[j] < smallest)
                smallest = numbers[j];
        }
    }

    return 0;
}

