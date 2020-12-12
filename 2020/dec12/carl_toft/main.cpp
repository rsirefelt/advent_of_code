#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <cmath>

const double PI = 3.14159265;

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

void moveShip(std::string instruction, long int& x, long int& y, long int& current_heading) {
    char letter = instruction.at(0);
    long int move_distance = std::stoi(instruction.substr(1, instruction.length()-1));

    if (letter == 'N') {
        y += move_distance;
    } else if (letter == 'E') {
        x += move_distance;
    } else if (letter == 'S') {
        y -= move_distance;
    } else if (letter == 'W') {
        x -= move_distance;
    } else if (letter == 'F') {
        x += round(move_distance*cos(current_heading*PI/180.0));
        y += round(move_distance*sin(current_heading*PI/180.0));
    } else if (letter == 'L') {
        current_heading += move_distance;
    } else if (letter == 'R') {
        current_heading -= move_distance;
    }
}

void carryOutWaypointInstruction(std::string instruction, long int& x, long int& y, long int& waypoint_x, long int& waypoint_y) {
    char letter = instruction.at(0);
    long int move_distance = std::stoi(instruction.substr(1, instruction.length()-1));

    if (letter == 'N') {
        waypoint_y += move_distance;
    } else if (letter == 'E') {
        waypoint_x += move_distance;
    } else if (letter == 'S') {
        waypoint_y -= move_distance;
    } else if (letter == 'W') {
        waypoint_x -= move_distance;
    } else if (letter == 'F') {
        x += move_distance*waypoint_x;
        y += move_distance*waypoint_y;
    } else if (letter == 'L') {
        double angle = atan2(waypoint_y, waypoint_x);
        double dist = sqrt(waypoint_x*waypoint_x + waypoint_y*waypoint_y);
        waypoint_x = round(dist*cos(angle+move_distance*PI/180.0));
        waypoint_y = round(dist*sin(angle+move_distance*PI/180.0));
    } else if (letter == 'R') {
        double angle = atan2(waypoint_y, waypoint_x);
        double dist = sqrt(waypoint_x*waypoint_x + waypoint_y*waypoint_y);
        waypoint_x = round(dist*cos(angle-move_distance*PI/180.0));
        waypoint_y = round(dist*sin(angle-move_distance*PI/180.0));
    }
}

int main() {
    // Read the puzzle input
    std::vector<std::string> input = readLines("/home/carl/CLionProjects/AdventOfCode/Day12/input.txt");

    // Define starting position and heading
    long int x = 0, y = 0, current_heading = 0;

    // Loop over all instructions and move the ship accordingly
    for (std::string instruction : input) {
        moveShip(instruction, x, y, current_heading);
    }

    std::cout << "Part 1: " << abs(x) + abs(y) << "\n";

    // Now for part 2
    x = 0;
    y = 0;
    long int waypoint_x = 10, waypoint_y = 1;
    for (std::string instruction : input) {
        carryOutWaypointInstruction(instruction, x, y, waypoint_x, waypoint_y);
    }

    std::cout << "Part 2: " << abs(x) + abs(y) << "\n";

    return 0;
}



