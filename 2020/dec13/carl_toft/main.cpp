#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <limits>

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
    // Read the puzzle input
    std::vector<std::string> input = readLines("/home/carl/CLionProjects/AdventOfCode/Day13/input.txt");
    long long int earliest_time = std::stoi(input[0]);
    std::vector<std::string> bus_ID_strings = splitString(input[1], ',');
    std::vector<long long int> bus_IDs;
    for (auto ID : bus_ID_strings) {
        if (ID != "x")
            bus_IDs.push_back(std::stoi(ID));
    }

    // Find the earliest departure time
    long int earliest_bus_ID;
    long int best_departure_time_found = -1, curr_departure_time;
    for (int i = 0; i < bus_IDs.size(); i++) {
        curr_departure_time = ceil(double(earliest_time)/bus_IDs[i])*bus_IDs[i];
        if (curr_departure_time < best_departure_time_found || best_departure_time_found == -1) {
            best_departure_time_found = curr_departure_time;
            earliest_bus_ID = bus_IDs[i];
        }
    }

    std::cout << "Part 1: " << earliest_bus_ID*(best_departure_time_found-earliest_time) << "\n";

    // Construct the system of moduli equations (C++ % is annoying...)
    unsigned long long int N = 1;
    std::vector<long int> a, b;
    long int a_i;
    for (auto ID : bus_IDs)
        N *= ID;
    for (int i = 0; i < bus_ID_strings.size(); i++) {
        if (bus_ID_strings[i] == "x")
            continue;
        a_i = (-i) % std::stoi(bus_ID_strings[i]);
        while (a_i < 0)
            a_i += std::stoi(bus_ID_strings[i]);
        a.push_back(a_i);
        b.push_back(std::stoi(bus_ID_strings[i]));
    }

    // Solve the system of moduli equations
    // t = a_i   (mod b_i)
    // using a sieving method
    unsigned long long int x = a[0], difference = b[0];
    unsigned long long int next_index = 1;
    while (true) {
        if (x % b[next_index] == a[next_index]) {
            difference = difference*b[next_index];
            next_index++;
            if (next_index == b.size())
                break;
            continue;
        }
        x += difference;
    }

    std::cout << "Part 2: " << x << "\n";
}
