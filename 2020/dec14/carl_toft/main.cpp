#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>

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

std::string convertNumberToBinaryString(unsigned long long int value, unsigned int desired_length=-1) {
    std::string binary_representation = "";

    unsigned long long int power_of_two = 1;
    while (value > power_of_two) {
        power_of_two *= 2;
    }

    while (power_of_two >= 1) {
        if (value >= power_of_two) {
            value -= power_of_two;
            binary_representation = binary_representation + "1";
        } else {
            binary_representation = binary_representation + "0";
        }
        power_of_two = power_of_two / 2;
    }

    // Zero-pad the beginning of the string so it has the desired length
    if (desired_length != -1) {
        while (binary_representation.length() < desired_length)
            binary_representation = "0" + binary_representation;
    }

    return binary_representation;
}

unsigned long long int convertBinaryStringToNumber(std::string binary_representation) {
    unsigned long long int power_of_two = 1, value = 0;
    for (int i = 0; i < binary_representation.length(); i++) {
        if (binary_representation.at(binary_representation.length()-1-i) == '1')
            value += power_of_two;
        power_of_two = power_of_two*2;
    }

    return value;
}

unsigned long long int transformValueUsingMask(unsigned long long int value, std::string mask) {
    std::string binary_representation = convertNumberToBinaryString(value, mask.length());
    std::string new_binary_representation = binary_representation;

    // Loop over all the characters in the binary representation and check in the mask if
    // they should be changed.
    for (int i = 0; i < binary_representation.length() && i < mask.length(); i++) {
        if (mask.at(mask.length()-1-i) == '0')
            new_binary_representation.at(new_binary_representation.length()-1-i) = '0';
        else if (mask.at(mask.length()-1-i) == '1')
            new_binary_representation.at(new_binary_representation.length()-1-i) = '1';
    }

    // Done! Just convert back to a decimal number
    unsigned long long int new_value = convertBinaryStringToNumber(new_binary_representation);
    return new_value;
}

void carryOutInstruction(std::string instruction, std::map<unsigned long long int, unsigned long long int>& memory, std::string& mask) {
    std::vector<std::string> parts = splitString(instruction, ' ');
    // Check if the instruction changes the mask or the memory
    if (parts[0] == "mask") {
        mask = parts[2];
        return;
    }

    // If we get here, the instruction changes the memory. Extract the value and memory address
    unsigned long long int value = std::stoi(parts[2]);

    parts = splitString(parts[0], '[');
    unsigned long long int address = std::stoi(parts[1].substr(0, parts[1].length()-1));

    // Write the transformed value
    value = transformValueUsingMask(value, mask);
    memory[address] = value;
}

std::vector<std::string> getAllMemoryAddresses(std::string binary_address, std::string mask) {
    std::vector<std::string> addresses, sub_addresses;

    // First, address the base case of the recursion
    if (binary_address.length() == 0) {
        addresses.push_back("");
        return addresses;
    }

    std::string first_part;
    for (int i = 0; i < binary_address.length(); i++) {
        if (mask.at(i) == '1')
            binary_address.at(i) = '1';
        if (mask.at(i) == 'X') {
            std::string sub_address = binary_address.substr(i+1, binary_address.length()-(i+1));
            std::string sub_mask = mask.substr(i+1, mask.length()-(i+1));
            sub_addresses = getAllMemoryAddresses(sub_address, sub_mask);
            first_part = binary_address.substr(0, i);
            break;
        }
    }

    if (sub_addresses.size() == 0) {
        addresses.push_back(binary_address);
        return addresses;
    }

    for (std::string sub_address : sub_addresses) {
        addresses.push_back(first_part + "0" + sub_address);
        addresses.push_back(first_part + "1" + sub_address);
    }

    return addresses;
}

void carryOutInstructionPart2(std::string instruction, std::map<unsigned long long int, unsigned long long int>& memory, std::string& mask) {
    std::vector<std::string> parts = splitString(instruction, ' ');
    // Check if the instruction changes the mask or the memory
    if (parts[0] == "mask") {
        mask = parts[2];
        return;
    }

    // If we get here, the instruction changes the memory. Extract the value and memory address
    unsigned long long int value = std::stoi(parts[2]);

    parts = splitString(parts[0], '[');
    unsigned long long int address = std::stoi(parts[1].substr(0, parts[1].length()-1));
    std::string binary_address = convertNumberToBinaryString(address, mask.length());

    // Get all possible addresses (several are possible due to the X'ses)
    std::vector<std::string> addresses = getAllMemoryAddresses(binary_address, mask);

    // Now we are pretty much done, write the right hand side to all addresses
    for (std::string curr_address : addresses) {
        memory[convertBinaryStringToNumber(curr_address)] = value;
        //std::cout << convertBinaryStringToNumber(curr_address) << "\n";
    }
}

int main() {
    // Read the puzzle input
    std::vector<std::string> input = readLines("/home/carl/CLionProjects/AdventOfCode/Day14/input.txt");
    std::map<unsigned long long int, unsigned long long int> memory;
    std::string mask;

    // Loop over all instructions and carry them out
    for (std::string instruction : input) {
        carryOutInstruction(instruction, memory, mask);
    }

    // We are done with part 1! Just sum up the numbers
    unsigned long long int sum = 0;
    for (auto it = memory.begin(); it != memory.end(); it++) {
        sum = sum + it->second;
    }
    std::cout << "Part 1: " << sum << "\n";

    // Now for part 2
    memory.clear();
    // Loop over all instructions and carry them out
    for (std::string instruction : input) {
        carryOutInstructionPart2(instruction, memory, mask);
    }

    // Now we are done with part 2 as well! Just sum up the numbers again
    sum = 0;
    for (auto it = memory.begin(); it != memory.end(); it++) {
        sum = sum + it->second;
    }
    std::cout << "Part 2: " << sum << "\n";

    return 0;
}










