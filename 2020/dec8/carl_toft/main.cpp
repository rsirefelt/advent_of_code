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

bool doesItLoop(std::vector<std::string> instructions, long int& accumulator, long int jmp_index_to_change = -1, long int nop_index_to_change = -1) {
    std::vector<bool> visited(instructions.size());
    for (int i = 0; i < visited.size(); i++)
        visited[i] = false;

    // Loop over the instructions until we hit the same instruction twice
    unsigned int current_instruction = 0;
    accumulator = 0;
    int jump_size = 0;
    long int curr_jmp_index = 1, curr_nop_index = 1;

    while (true) {
        if (visited[current_instruction] == true) {
            return true; // Program is looping
        }
        if (current_instruction == instructions.size()) {
            return false; // Program terminated correctly
        }

        // Parse instruction
        jump_size = 1;
        visited[current_instruction] = true;
        std::vector<std::string> split = splitString(instructions[current_instruction], ' ');
        // Check if the current instruction should be changed
        if (split[0] == "jmp" && curr_jmp_index == jmp_index_to_change) {
            split[0] = "nop";
            curr_jmp_index++;
        }
        if (split[0] == "nop" && curr_nop_index == nop_index_to_change) {
            split[0] = "jmp";
            curr_nop_index++;
        }

        // Now process the instruction (which may have changed)
        if (split[0] == "nop") {
            current_instruction++;
            curr_nop_index++;
            continue;
        }
        if (split[0] == "acc")
            accumulator += std::stoi(split[1]);
        if (split[0] == "jmp") {
            curr_jmp_index++;
            jump_size = std::stoi(split[1]);
        }

        current_instruction += jump_size;
    }
}

int main() {
    // Read the puzzle input
    std::vector<std::string> instructions = readLines("/home/carl/CLionProjects/AdventOfCode/Day8/input.txt");

    // Loop over the instructions until we hit the same instruction twice
    long int accumulator = 0;
    bool loop = doesItLoop(instructions, accumulator);
    if (loop == true) {
        std::cout << "It loops! Accumulator before loop: " << accumulator << "\n";
    }

    for (long int jmp_index_to_change = 1; jmp_index_to_change < instructions.size(); jmp_index_to_change++) {
        bool loop = doesItLoop(instructions, accumulator, jmp_index_to_change, -1);
        if (loop == false) {
            std::cout << "The program terminated! Accumulator after termination: " << accumulator << "\n";
        }
    }

    for (long int nop_index_to_change = 1; nop_index_to_change < instructions.size(); nop_index_to_change++) {
        bool loop = doesItLoop(instructions, accumulator, -1, nop_index_to_change);
        if (loop == false) {
            std::cout << "The program terminated! Accumulator after termination: " << accumulator << "\n";
        }
    }

    return 0;
}