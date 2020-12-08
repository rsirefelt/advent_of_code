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

typedef std::map<std::string, std::string> passport;

bool validatePassport(passport pass) {
    // Check that all entries exist
    if (pass.count("byr") != 1)
        return false;
    if (pass.count("iyr") != 1)
        return false;
    if (pass.count("eyr") != 1)
        return false;
    if (pass.count("hgt") != 1)
        return false;
    if (pass.count("hcl") != 1)
        return false;
    if (pass.count("ecl") != 1)
        return false;
    if (pass.count("pid") != 1)
        return false;

    // All entries exist. Validate each of them
    int byr = std::stoi(pass["byr"]);
    if (byr < 1920 || byr > 2020)
        return false;

    int iyr = std::stoi(pass["iyr"]);
    if (iyr < 2010 || iyr > 2020)
        return false;

    int eyr = std::stoi(pass["eyr"]);
    if (eyr < 2020 || eyr > 2030)
        return false;

    std::string ecl = pass["ecl"];
    if (! (ecl == "amb" || ecl == "blu" || ecl == "brn" || ecl == "gry" || ecl == "grn" || ecl == "hzl" || ecl == "oth")  )
        return false;

    std::string pid = pass["pid"];
    if (pid.length() != 9)
        return false;
    for (int i = 0; i < 9; i++) {
        if (!(pid.at(i) == '0' || pid.at(i) == '1' || pid.at(i) == '2' || pid.at(i) == '3' || pid.at(i) == '4' ||
              pid.at(i) == '5' || pid.at(i) == '6' || pid.at(i) == '7' || pid.at(i) == '8' || pid.at(i) == '9'))
            return false;
    }

    std::string hcl = pass["hcl"];
    if (hcl.length() != 7)
        return false;
    if (hcl.at(0) != '#')
        return false;
    for (int i = 1; i < 6; i++) {
        if (!(hcl.at(i) == '0' || hcl.at(i) == '1' || hcl.at(i) == '2' || hcl.at(i) == '3' || hcl.at(i) == '4' ||
              hcl.at(i) == '5' || hcl.at(i) == '6' || hcl.at(i) == '7' || hcl.at(i) == '8' || hcl.at(i) == '9' ||
              hcl.at(i) == 'a' || hcl.at(i) == 'b' || hcl.at(i) == 'c' || hcl.at(i) == 'd' || hcl.at(i) == 'e' ||
              hcl.at(i) == 'f'))
            return false;
    }

    std::string hgt = pass["hgt"];
    std::string unit;
    unsigned int length;
    unit = hgt.substr(hgt.length()-2,2);
    length = std::stoi(hgt.substr(0, hgt.length()-2));
    if (!(unit == "cm" || unit == "in"))
        return false;
    if (unit == "cm") {
        if (length < 150 || length > 193)
            return false;
    }
    if (unit == "in") {
        if (length < 59 || length > 76)
            return false;
    }

    return true;
}

int main() {
    std::vector<passport> passports; // to hold all passport information

    // Read the input data
    std::vector<std::string> input = readLines("/home/carl/CLionProjects/AdventOfCode/Day4/input.txt");

    passport curr_passport;
    for (std::string line : input) {
        if (line == "") {
            // Start new passport and continue
            passports.push_back(curr_passport);
            curr_passport.clear();
            continue;
        }

        // The line contained entries, so read them and add to the current passport
        // being processed.
        std::vector<std::string> entries = splitString(line, ' ');
        for (std::string entry : entries) {
            std::vector<std::string> key_value = splitString(entry, ':');
            curr_passport[key_value[0]] = key_value[1];
        }
    }

    // Now we have processed all passports. Count how many are valid
    unsigned int num_valid = 0;
    for (passport pass : passports) {
        if (validatePassport(pass) == true)
            num_valid++;
    }

    std::cout << num_valid << "\n";

    return 0;
}




















