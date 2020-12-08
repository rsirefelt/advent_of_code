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

unsigned int readBoardingPass(std::string boarding_pass, unsigned int& row, unsigned int& col) {
    row = 0;
    col = 0;

    // Find the row
    unsigned int to_add = 64;
    for (int i = 0; i < 7; i++) {
        if (boarding_pass.at(i) == 'B')
            row += to_add;
        to_add = to_add / 2;
    }

    // Find the column
    to_add = 4;
    for (int i = 7; i < 10; i++) {
        if (boarding_pass.at(i) == 'R')
            col += to_add;
        to_add = to_add / 2;
    }

    // Lastly, compute the seat ID
    unsigned int ID = row*8 + col;
    return ID;
}

int main() {
    // Read the puzzle input
    std::vector<std::string> boarding_passes = readLines("/home/carl/CLionProjects/AdventOfCode/Day5/input.txt");

    // Create a map over all taken seats
    bool seat_map[128][8];
    for (int i = 0; i < 128; i++) {
        for (int j = 0; j < 8; j++)
            seat_map[i][j] = false;
    }

    // Go over all boarding passes, find their seat IDs, and populate the
    // map over filled seats
    unsigned int row = 0, col = 0, ID = 0;
    unsigned int max_id = 0;
    for (std::string boarding_pass : boarding_passes) {
        ID = readBoardingPass(boarding_pass, row, col);
        seat_map[row][col] = true;
        if (ID > max_id)
            max_id = ID;
    }

    // Print the seat map
    for (int i = 0; i < 128; i++) {
        std::cout << "|";
        for (int j = 0; j < 8; j++) {
            if (seat_map[i][j] == true)
                std::cout << "o";
            else
                std::cout << " ";
        }
        std::cout << "| " << i << "\n";
    }

    std::cout << max_id << "\n";
    return 0;
}