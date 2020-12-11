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

bool shouldSeatChange(std::vector<std::string>& seats, unsigned int row, unsigned int col) {
    // Floor doesnt change
    if (seats[row].at(col) == '.')
        return false;

    // Count number of adjacent occupied seats
    unsigned int num_adjacent_occupied_seats = 0;
    for (int i = -1; i <= 1; i++) {
        for (int j = -1; j <= 1; j++) {
            if (i == 0 and j == 0)
                continue;
            if (seats[row+i].at(col+j) == '#')
                num_adjacent_occupied_seats++;
        }
    }

    if (seats[row].at(col) == '#' && num_adjacent_occupied_seats >= 4)
        return true;
    if (seats[row].at(col) == 'L' && num_adjacent_occupied_seats == 0)
        return true;

    return false;
}

bool shouldSeatChangePart2(std::vector<std::string>& seats, unsigned int row, unsigned int col) {
    // Floor doesnt change
    if (seats[row].at(col) == '.')
        return false;

    // For each direction, see if we hit an occupied seat
    unsigned int num_visible_occupied_seats = 0;
    for (int i = -1; i <= 1; i++) {
        for (int j = -1; j <= 1; j++) {
            if (i == 0 and j == 0)
                continue;
            // Traverse the line and see if we hit an occupied seat
            unsigned int stepLength = 1;
            while (true) {
                // See if we have left the map
                if (row+i*stepLength >= seats.size() || row+i*stepLength < 0 || col+j*stepLength >= seats[0].length() || col+j*stepLength < 0)
                    break;

                // See if we hit an occupied seat
                if (seats[row+i*stepLength].at(col+j*stepLength) == '#') {
                    num_visible_occupied_seats++;
                    break;
                } // or an unoccupied seat
                else if (seats[row+i*stepLength].at(col+j*stepLength) == 'L') {
                    break;
                }
                stepLength++;
            }
        }
    }

    if (seats[row].at(col) == '#' && num_visible_occupied_seats >= 5)
        return true;
    if (seats[row].at(col) == 'L' && num_visible_occupied_seats == 0)
        return true;

    return false;
}

bool updateAllSeats(std::vector<std::string>& seats) {
    // Keep track och which seats to change
    std::vector<std::vector<bool>> seatsToChange(seats.size());
    for (int i = 0; i < seats.size(); i++) {
        std::vector<bool> seatRow(seats[0].length());
        for (int j = 0; j < seats[0].length(); j++) {
            seatRow[j] = false;
        }
        seatsToChange[i] = seatRow;
    }

    // Check if each seat should be changed
    for (int row = 1; row < seats.size()-1; row++) {
        for (int col = 1; col < seats[row].length()-1; col++) {
            seatsToChange[row][col] = shouldSeatChangePart2(seats, row, col);
        }
    }

    // Update seats
    bool updated = false;
    for (int i = 1; i < seats.size()-1; i++) {
        for (int j = 1; j < seats[0].length()-1; j++) {
            if (seatsToChange[i][j] == true && seats[i].at(j) == '#') {
                seats[i].at(j) = 'L';
                updated = true;
            }
            else if (seatsToChange[i][j] == true && seats[i].at(j) == 'L') {
                seats[i].at(j) = '#';
                updated = true;
            }
        }
    }

    return updated;
}

unsigned long long int countUnoccupiedSeats(std::vector<std::string>& seats) {
    unsigned long long int num_occupied_seats = 0;
    for (int i = 1; i < seats.size()-1; i++) {
        for (int j = 1; j < seats[0].length()-1; j++) {
            if (seats[i].at(j) == '#')
                num_occupied_seats++;
        }
    }

    return num_occupied_seats;
}

int main() {
    // Read the puzzle input
    std::vector<std::string> input = readLines("/home/carl/CLionProjects/AdventOfCode/Day11/input.txt");

    // Pad the input with empty seats
    for (int i = 0; i < input.size(); i++) {
        input[i].insert(0, ".");
        input[i].insert(input[i].length(), ".");
    }
    std::string empty_seats = ".";
    for (int i = 1; i < input[0].length(); i++)
        empty_seats += ".";
    input.insert(input.begin(), empty_seats);
    input.push_back(empty_seats);

    bool updated = true;
    while (updated == true) {
        updated = updateAllSeats(input);
    }

    std::cout << "Part 2: " << countUnoccupiedSeats(input) << "\n";

    return 0;
}
