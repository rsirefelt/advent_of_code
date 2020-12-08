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

int main() {
    // Load the puzzle input (the map)
    std::vector<std::string> map = readLines("/home/carl/CLionProjects/AdventOfCode/Day3/input.txt");
    unsigned int W = map[0].length();
    unsigned int H = map.size();

    // Define starting position
    unsigned int curr_col = 0;
    unsigned int curr_row = 0;

    // Define horizontal and vertical speeds
    int speed_right = 3;
    int speed_down = 1;

    // Traverse each row until we hit bottom
    unsigned int num_trees_hit = 0;
    for (int i = 0; curr_row < map.size(); i++) {
        // Move the sled
        curr_row = curr_row + speed_down;
        curr_col = curr_col + speed_right;
        curr_col = curr_col % W;

        // Stop if we reached the bottom
        if (curr_row >= H)
            break;

        // Check if we hit a tree
        if (map[curr_row][curr_col] == '#')
            num_trees_hit++;
    }

    std::cout << num_trees_hit << "\n";
    return 0;
}
