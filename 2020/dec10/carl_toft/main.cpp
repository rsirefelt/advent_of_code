#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

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

struct Adapter {
    long int joltage;
    std::vector<Adapter*> ingoing, outgoing;
    bool done;
    unsigned long long int num_paths;
};

unsigned long long int countPaths(Adapter* A) {
    if (A->done == true)
        return A->num_paths;

    for (int i = 0; i < A->ingoing.size(); i++) {
        A->num_paths = A->num_paths + countPaths(A->ingoing[i]);
    }

    A->done = true;
    return A->num_paths;
}

// Part 2
int main() {
    // Read the puzzle input
    std::vector<std::string> input = readLines("/home/carl/CLionProjects/AdventOfCode/Day10/input.txt");
    std::vector<long int> numbers;
    numbers.push_back(0); // add the outlet
    for (std::string line : input)
        numbers.push_back(std::stoi(line));

    // Add the device at max+3
    long int max_num = *std::max_element(numbers.begin(), numbers.end());
    numbers.push_back(max_num+3);
    std::sort(numbers.begin(), numbers.end());

    // Create the adapters
    std::vector<Adapter> adapters;
    for (long int num : numbers) {
        Adapter A;
        A.joltage = num;
        A.done = false;
        A.num_paths = 0;
        adapters.push_back(A);
    }
    adapters[0].num_paths = 1;

    // For each adapter, find the ingoing and outgoing ones
    for (int i = 0; i < adapters.size(); i++) {
        for (int j = 0; j < adapters.size(); j++) {
            if (i == j)
                continue;
            if (adapters[j].joltage < adapters[i].joltage && adapters[j].joltage >= adapters[i].joltage-3)
                adapters[i].ingoing.push_back(&adapters[j]);
            if (adapters[i].joltage < adapters[j].joltage && adapters[i].joltage >= adapters[j].joltage-3)
                adapters[i].outgoing.push_back(&adapters[j]);
        }
    }

    unsigned long long int num_paths = countPaths(&adapters[adapters.size()-1]);
    std::cout << adapters[adapters.size()-1].num_paths << "\n";

    return 0;
}

// Part 1
/*int main() {
    // Read the puzzle input
    std::vector<std::string> input = readLines("/home/carl/CLionProjects/AdventOfCode/Day10/input.txt");
    std::vector<long int> numbers;
    for (std::string line : input)
        numbers.push_back(std::stoi(line));

    // Add the outlet at 0, and the device at max+3
    long int max_num = *std::max_element(numbers.begin(), numbers.end());
    numbers.push_back(0);
    numbers.push_back(max_num+3);

    // Sort!
    std::sort(numbers.begin(), numbers.end());

    // Now, count number of one- and three-jolt differences
    unsigned long int num_one_jolt = 0, num_three_jolt = 0;
    for (int i = 1; i < numbers.size(); i++) {
        if (numbers[i] - numbers[i-1] == 1)
            num_one_jolt++;
        else if (numbers[i] - numbers[i-1] == 3)
            num_three_jolt++;
    }

    std::cout << num_one_jolt*num_three_jolt << "\n";

    return 0;
}*/
