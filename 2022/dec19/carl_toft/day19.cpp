#include <iostream>
#include <vector>
#include <fstream>
#include <cstdlib>
#include <map>

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

unsigned long long int max(unsigned long long int a, unsigned long long int b) {
    if (a > b)
        return a;
    else
        return b;
}

struct State {
    int ore;
    int clay;
    int obsidian;
    int geode;
    int ore_robots;
    int clay_robots;
    int obsidian_robots;
    int geode_robots;

    State(int o, int c, int ob, int geo, int o_r, int c_r, int ob_r, int g_r) {
        ore = o;
        clay = c;
        obsidian = ob;
        geode = geo;
        ore_robots = o_r;
        clay_robots = c_r;
        obsidian_robots = ob_r;
        geode_robots = g_r;
    };

    State() {ore=0; clay=0; obsidian=0; geode = 0; ore_robots=0; clay_robots=0; obsidian_robots=0; geode_robots=0;};

    bool operator<(State const& rhs) const;

    State obtain_ore() const {
        State new_state(ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots);
        new_state.ore += new_state.ore_robots;
        new_state.clay += new_state.clay_robots;
        new_state.obsidian += new_state.obsidian_robots;
        new_state.geode += new_state.geode_robots;

        return new_state;
    }

};


unsigned long long int solve_heuristic(const State &state, int ore_robot_ore_cost, int clay_robot_ore_cost, int obsidian_robot_ore_cost, int obsidian_robot_clay_cost, int geode_robot_ore_cost, int geode_robot_obsidian_cost, int threshold1=3, int threshold2=10, int threshold3=17) {
    State curr_state = state;

    for (int minute = 1; minute <= 24; minute++) {
        if (minute < threshold1 && ore_robot_ore_cost <= curr_state.ore) {
            curr_state.ore -= ore_robot_ore_cost;
            curr_state = curr_state.obtain_ore();
            curr_state.ore_robots += 1;
            continue;
        }
        else if (minute <= threshold2 && clay_robot_ore_cost <= curr_state.ore) {
            curr_state.ore -= clay_robot_ore_cost;
            curr_state = curr_state.obtain_ore();
            curr_state.clay_robots += 1;
            continue;
        }
        else if (minute <= threshold3 && obsidian_robot_ore_cost <= curr_state.ore && obsidian_robot_clay_cost <= curr_state.clay) {
            curr_state.ore -= obsidian_robot_ore_cost;
            curr_state.clay -= obsidian_robot_clay_cost;
            curr_state = curr_state.obtain_ore();
            curr_state.obsidian_robots += 1;
        }
        else if (minute > threshold3 && geode_robot_ore_cost <= curr_state.ore && geode_robot_obsidian_cost <= curr_state.obsidian) {
            curr_state.ore -= geode_robot_ore_cost;
            curr_state.obsidian -= curr_state.obsidian;
            curr_state = curr_state.obtain_ore();
            curr_state.geode_robots += 1;
        } else {
            curr_state = curr_state.obtain_ore();
        }
    }

    return curr_state.geode;
}


unsigned long long int solve_heuristic_multiple(const State &state, int ore_robot_ore_cost, int clay_robot_ore_cost, int obsidian_robot_ore_cost, int obsidian_robot_clay_cost, int geode_robot_ore_cost, int geode_robot_obsidian_cost) {
    int num_tries = 1000;
    int threshold1, threshold2, threshold3;
    unsigned long long int curr_solution, best_solution = 0;
    for (int i = 0; i < num_tries; i++) {
        threshold1 = rand() % 14 + 1;
        threshold2 = threshold1 + rand() % 9 + 1;
        threshold3 = threshold2 + rand() % 9 + 1;
        //std::cout << threshold1 << " " << threshold2 << " " << threshold3 << "\n";

        curr_solution = solve_heuristic(state, ore_robot_ore_cost, clay_robot_ore_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_robot_ore_cost, geode_robot_obsidian_cost, threshold1, threshold2, threshold3);
        if (curr_solution > best_solution) {
            best_solution = curr_solution;
        }
    }

    return best_solution;
}


// Get the maximum ore possible at the start of the stop minute
unsigned long long int upper_bound_ore(int curr_ore, int num_ore_robots, int ore_robot_cost, int start_minute, int stop_minute) {
    if (start_minute == stop_minute) {
        return curr_ore;
    }

    // We can do to things: buy an ore robot if we can afford it, or just collect ore
    unsigned long long int choice1 = 0, choice2 = 0;
    if (curr_ore >= ore_robot_cost) {
        choice1 = upper_bound_ore(curr_ore - ore_robot_cost + num_ore_robots, num_ore_robots+1, ore_robot_cost, start_minute+1, stop_minute);
    }
    choice2 = upper_bound_ore(curr_ore + num_ore_robots, num_ore_robots, ore_robot_cost, start_minute+1, stop_minute);

    if (choice1 > choice2) {
        return choice1;
    } else {
        return choice2;
    }
}

// Is this too strict?
unsigned long long int upper_bound(const State &state, int ore_robot_ore_cost, int clay_robot_ore_cost, int obsidian_robot_ore_cost, int obsidian_robot_clay_cost, int geode_robot_ore_cost, int geode_robot_obsidian_cost, int curr_minute) {
    // Calculate maximum possible ore at the start of each minute in the future
    std::map<int, int> max_ore, max_clay, max_obsidian, max_geodes, max_ore_robots, max_clay_robots, max_obsidian_robots, max_geode_robots;
    int curr_max_ore, curr_max_clay, curr_max_obsidian, curr_max_geodes;

    max_ore[curr_minute] = state.ore;
    max_clay[curr_minute] = state.clay;
    max_obsidian[curr_minute] = state.obsidian;
    max_geodes[curr_minute] = state.geode;

    //max_ore_robots[curr_minute] = state.ore_robots;
    //max_clay_robots[curr_minute] = state.clay_robots;
    //max_obsidian_robots[curr_minute] = state.obsidian_robots;
    //max_geode_robots[curr_minute] = state.geode_robots;
    
    // Upper bound ore
    for (int min = curr_minute + 1; min <= 25; min++) {
        // TODO: CHECK FOR OFF-BY-ONE ERRORS HERE
        max_ore[min] = upper_bound_ore(state.ore, state.ore_robots, ore_robot_ore_cost, curr_minute, min);
    }

    // Upper bound clay
    int num_clay_robots_bought = 0;
    for (int min = curr_minute; min <= 24; min++) {
        max_clay[min+1] = max_clay[min] + (state.clay_robots + num_clay_robots_bought);
        if (max_ore[min] >= (num_clay_robots_bought+1)*clay_robot_ore_cost) {
            num_clay_robots_bought++;
        }
    }

    // Upper bound obsidian
    int num_obsidian_robots_bought = 0;
    for (int min = curr_minute; min <= 24; min++) {
        max_obsidian[min+1] = max_obsidian[min] + (state.obsidian_robots + num_obsidian_robots_bought);
        if (max_ore[min] >= (num_obsidian_robots_bought+1)*obsidian_robot_ore_cost && max_clay[min] >= (num_obsidian_robots_bought+1)*obsidian_robot_clay_cost) {
            num_obsidian_robots_bought++;
        }
    }

    // Upper bound geode
    int num_geode_robots_bought = 0;
    for (int min = curr_minute; min <= 24; min++) {
        max_geodes[min+1] = max_geodes[min] + (state.geode_robots + num_geode_robots_bought);
        if (max_ore[min] >= (num_geode_robots_bought+1)*geode_robot_ore_cost && max_obsidian[min] >= (num_geode_robots_bought+1)*geode_robot_obsidian_cost) {
            num_geode_robots_bought++;
        }
    }

    return max_geodes[25];
}


unsigned long long int LOWER_BOUND;
unsigned long long int NUM_BRANCHES = 0;

unsigned long long int solve_branch_and_bound(const State &state, int ore_robot_ore_cost, int clay_robot_ore_cost, int obsidian_robot_ore_cost, int obsidian_robot_clay_cost, int geode_robot_ore_cost, int geode_robot_obsidian_cost, int minute, int curr_score) {

    if (minute == 24) {
        unsigned long long int total_num_geodes = state.geode_robots + curr_score;
        if (total_num_geodes > LOWER_BOUND) {
            //std::cout << "New best solution found: " << total_num_geodes << "\n";
            LOWER_BOUND = total_num_geodes;
        }
        return total_num_geodes;
    }

    // Compute upper bound for the number of geodes. If the known lower bound is higher than this, terminate search of this subtree
    if (minute == 20) {
        NUM_BRANCHES++;
        //std::cout << "Obsidian: " << state.obsidian << "\n";
    }

    // TODO: PRUNING STRATEGY
    if (minute >= 10) {
        auto upper_limit = upper_bound(state, ore_robot_ore_cost, clay_robot_ore_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_robot_ore_cost, geode_robot_obsidian_cost, minute);
        if (upper_limit <= LOWER_BOUND) {
            //std::cout << "Terminating search at minute " << minute << " with upper limit " << upper_limit << "\n";
            return upper_limit;
        }
    }
    //if (minute >= 20 && state.obsidian == 0 && state.geode == 0) {
    //        std::cout << "Terminating...\n";
    //        return 0;
    //}

    State tmp_state = state;
    unsigned long long int curr_val, best_val;
    best_val = solve_branch_and_bound(tmp_state.obtain_ore(), ore_robot_ore_cost, clay_robot_ore_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_robot_ore_cost, geode_robot_obsidian_cost, minute+1, curr_score + state.geode_robots);

    // Buy ore robot
    if (state.ore >= ore_robot_ore_cost) {
        tmp_state = state;
        tmp_state.ore -= ore_robot_ore_cost;
        tmp_state = tmp_state.obtain_ore();
        tmp_state.ore_robots += 1;
        //curr_val = state.geode_robots + solve_branch_and_bound(tmp_state, ore_robot_ore_cost, clay_robot_ore_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_robot_ore_cost, geode_robot_obsidian_cost, minute+1, curr_score + state.geode_robots);
        curr_val = solve_branch_and_bound(tmp_state, ore_robot_ore_cost, clay_robot_ore_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_robot_ore_cost, geode_robot_obsidian_cost, minute+1, curr_score + state.geode_robots);
        best_val = max(best_val, curr_val);
    }
    // Buy clay robot
    if (state.ore >= clay_robot_ore_cost) {
        tmp_state = state;
        tmp_state.ore -= clay_robot_ore_cost;
        tmp_state = tmp_state.obtain_ore();
        tmp_state.clay_robots += 1;
        curr_val = solve_branch_and_bound(tmp_state, ore_robot_ore_cost, clay_robot_ore_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_robot_ore_cost, geode_robot_obsidian_cost, minute+1, curr_score + state.geode_robots);
        best_val = max(best_val, curr_val);
    }
    // Buy obsidian robot
    if (state.ore >= obsidian_robot_ore_cost && state.clay >= obsidian_robot_clay_cost) {
        tmp_state = state;
        tmp_state.ore -= obsidian_robot_ore_cost;
        tmp_state.clay -= obsidian_robot_clay_cost;
        tmp_state = tmp_state.obtain_ore();
        tmp_state.obsidian_robots += 1;
        curr_val = solve_branch_and_bound(tmp_state, ore_robot_ore_cost, clay_robot_ore_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_robot_ore_cost, geode_robot_obsidian_cost, minute+1, curr_score + state.geode_robots);
        best_val = max(best_val, curr_val);
    }
    // Buy geode robot
    if (state.ore >= geode_robot_ore_cost && state.obsidian >= geode_robot_obsidian_cost) {
        tmp_state = state;
        tmp_state.ore -= geode_robot_ore_cost;
        tmp_state.obsidian -= geode_robot_obsidian_cost;
        tmp_state = tmp_state.obtain_ore();
        tmp_state.geode_robots += 1;
        curr_val = solve_branch_and_bound(tmp_state, ore_robot_ore_cost, clay_robot_ore_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_robot_ore_cost, geode_robot_obsidian_cost, minute+1, curr_score + state.geode_robots);
        best_val = max(best_val, curr_val);
    }

    return best_val;
}

int main() {
    srand(time(NULL));
    std::vector<std::string> lines = readLines("test_input.txt");

    // Solve for each blueprint
    int ID = 1;
    int total_quality_levels = 0;
    for (std::string line : lines) {
        auto words = splitString(line, ' ');
        int ore_robot_ore_cost = std::atoi(words[6].c_str());
        int clay_robot_ore_cost = std::atoi(words[12].c_str());
        int obsidian_robot_ore_cost = std::atoi(words[18].c_str());
        int obsidian_robot_clay_cost = std::atoi(words[21].c_str());
        int geode_robot_ore_cost = std::atoi(words[27].c_str());
        int geode_robot_obsidian_cost = std::atoi(words[30].c_str());

        State initial_state;
        initial_state.ore_robots = 1;
        LOWER_BOUND = solve_heuristic_multiple(initial_state, ore_robot_ore_cost, clay_robot_ore_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_robot_ore_cost, geode_robot_obsidian_cost);
        unsigned long long int max_geodes = solve_branch_and_bound(initial_state, ore_robot_ore_cost, clay_robot_ore_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_robot_ore_cost, geode_robot_obsidian_cost, 1, 0);
        std::cout << "ID " << ID << ": " <<  max_geodes << ". Lower bound: " << LOWER_BOUND << "\n";
        total_quality_levels = total_quality_levels + ID*max_geodes;

        ID++;
    }

    std::cout << "Answer: " << total_quality_levels << "\n";

    return 0;
}
