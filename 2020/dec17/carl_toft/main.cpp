#include <iostream>
#include <fstream>
#include <vector>
#include <string>

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

const unsigned long long int MAP_SIZE = 30;
const unsigned long long int OFFSET = (MAP_SIZE-1)/2;

void printMapSlice(bool map[MAP_SIZE][MAP_SIZE][MAP_SIZE], long int z) {
    for (int y = 0; y < MAP_SIZE; y++) {
        for (int x = 0; x < MAP_SIZE; x++) {
            if (map[x][y][z+OFFSET] == true)
                std::cout << "A";
            else
                std::cout << "B";
        }
        std::cout << "\n";
    }
}

void timeStep(bool map[MAP_SIZE][MAP_SIZE][MAP_SIZE]) {
    // Create a copy of the old map (since all values change simultaneously)
    bool old_map[MAP_SIZE][MAP_SIZE][MAP_SIZE];
    for (int x = 0; x < MAP_SIZE; x++) {
        for (int y = 0; y < MAP_SIZE; y++) {
            for (int z = 0; z < MAP_SIZE; z++) {
                old_map[x][y][z] = map[x][y][z];
            }
        }
    }

    // Now, update all values
    unsigned int num_neighbours_active = 0;
    for (int x = 1; x < MAP_SIZE-1; x++) {
        for (int y = 1; y < MAP_SIZE-1; y++) {
            for (int z = 1; z < MAP_SIZE-1; z++) {
                // For each cube, check all neighbouring cubes, and count how many
                // are active.
                num_neighbours_active = 0;
                for (int delta_x = -1; delta_x <= 1; delta_x++) {
                    for (int delta_y = -1; delta_y <= 1; delta_y++) {
                        for (int delta_z = -1; delta_z <= 1; delta_z++) {
                            if (delta_x == 0 && delta_y == 0 && delta_z == 0)
                                continue; // skip the current cube
                            if (old_map[x + delta_x][y + delta_y][z + delta_z] == true)
                                num_neighbours_active++;

                        }
                    }
                }

                // We have now counted the neighbours. Update the cube if necessary
                if (old_map[x][y][z] == true) {
                    if (num_neighbours_active == 2 || num_neighbours_active == 3)
                        map[x][y][z] = true;
                    else
                        map[x][y][z] = false;
                } else {
                    if (num_neighbours_active == 3)
                        map[x][y][z] = true;
                }
            }
        }
    }
}

void timeStep4D(bool map[MAP_SIZE][MAP_SIZE][MAP_SIZE][MAP_SIZE]) {
    // Create a copy of the old map (since all values change simultaneously)
    bool old_map[MAP_SIZE][MAP_SIZE][MAP_SIZE][MAP_SIZE];
    for (int x = 0; x < MAP_SIZE; x++) {
        for (int y = 0; y < MAP_SIZE; y++) {
            for (int z = 0; z < MAP_SIZE; z++) {
                for (int w = 0; w < MAP_SIZE; w++) {
                    old_map[x][y][z][w] = map[x][y][z][w];
                }
            }
        }
    }

    // Now, update all values
    unsigned int num_neighbours_active = 0;
    for (int x = 1; x < MAP_SIZE-1; x++) {
        for (int y = 1; y < MAP_SIZE-1; y++) {
            for (int z = 1; z < MAP_SIZE-1; z++) {
                for (int w = 1; w < MAP_SIZE-1; w++) {
                    // For each cube, check all neighbouring cubes, and count how many
                    // are active.
                    num_neighbours_active = 0;
                    for (int delta_x = -1; delta_x <= 1; delta_x++) {
                        for (int delta_y = -1; delta_y <= 1; delta_y++) {
                            for (int delta_z = -1; delta_z <= 1; delta_z++) {
                                for (int delta_w = -1; delta_w <= 1; delta_w++) {
                                    if (delta_x == 0 && delta_y == 0 && delta_z == 0 && delta_w == 0)
                                        continue; // skip the current cube
                                    if (old_map[x + delta_x][y + delta_y][z + delta_z][w + delta_w] == true)
                                        num_neighbours_active++;
                                }

                            }
                        }
                    }

                    // We have now counted the neighbours. Update the cube if necessary
                    if (old_map[x][y][z][w] == true) {
                        if (num_neighbours_active == 2 || num_neighbours_active == 3)
                            map[x][y][z][w] = true;
                        else
                            map[x][y][z][w] = false;
                    } else {
                        if (num_neighbours_active == 3)
                            map[x][y][z][w] = true;
                    }
                }
            }
        }
    }
}

unsigned long long int countActiveCells(bool map[MAP_SIZE][MAP_SIZE][MAP_SIZE]) {
    unsigned long long int num_cells_active = 0;
    for (int x = 0; x < MAP_SIZE; x++) {
        for (int y = 0; y < MAP_SIZE; y++) {
            for (int z = 0; z < MAP_SIZE; z++) {
                if (map[x][y][z] == true)
                    num_cells_active++;
            }
        }
    }

    return num_cells_active;
}

unsigned long long int countActiveCells4D(bool map[MAP_SIZE][MAP_SIZE][MAP_SIZE][MAP_SIZE]) {
    unsigned long long int num_cells_active = 0;
    for (int x = 0; x < MAP_SIZE; x++) {
        for (int y = 0; y < MAP_SIZE; y++) {
            for (int z = 0; z < MAP_SIZE; z++) {
                for (int w = 0; w < MAP_SIZE; w++) {
                    if (map[x][y][z][w] == true)
                        num_cells_active++;
                }
            }
        }
    }

    return num_cells_active;
}

/*
// Part 1
int main() {
    // Read the puzzle input, and convert it to an appropriate format
    std::vector<std::string> input = readLines("/home/carl/CLionProjects/AdventOfCode/Day17/input.txt");

    // Initialize 3D map
    bool map[MAP_SIZE][MAP_SIZE][MAP_SIZE];
    for (int x = 0; x < MAP_SIZE; x++) {
        for (int y = 0; y < MAP_SIZE; y++) {
            for (int z = 0; z < MAP_SIZE; z++) {
                map[x][y][z] = false;
            }
        }
    }
    for (int x = 0; x < input[0].length(); x++) {
        for (int y = 0; y < input.size(); y++) {
            if (input[y].at(x) == '#')
                map[x+OFFSET][y+OFFSET][OFFSET] = true;
        }
    }

    // Timestep 3D map
    for (int t = 1; t <= 6; t++) {
        timeStep(map);
    }

    // Done! Count the number of active cells
    std::cout << "Part 1: " << countActiveCells(map) << "\n";
    return 0;
}
*/

// Part 2
int main() {
    // Read the puzzle input, and convert it to an appropriate format
    std::vector<std::string> input = readLines("/home/carl/CLionProjects/AdventOfCode/Day17/input.txt");

    // Initialize 3D map
    bool map[MAP_SIZE][MAP_SIZE][MAP_SIZE][MAP_SIZE];
    for (int x = 0; x < MAP_SIZE; x++) {
        for (int y = 0; y < MAP_SIZE; y++) {
            for (int z = 0; z < MAP_SIZE; z++) {
                for (int w = 0; w < MAP_SIZE; w++) {
                    map[x][y][z][w] = false;
                }
            }
        }
    }
    for (int x = 0; x < input[0].length(); x++) {
        for (int y = 0; y < input.size(); y++) {
            if (input[y].at(x) == '#')
                map[x+OFFSET][y+OFFSET][OFFSET][OFFSET] = true;
        }
    }

    // Timestep 3D map
    for (int t = 1; t <= 6; t++) {
        timeStep4D(map);
    }

    // Done! Count the number of active cells
    std::cout << "Part 2: " << countActiveCells4D(map) << "\n";
    return 0;
}