#include <fstream>
#include <iostream>
#include <unordered_set>
#include <string>

int problemA(std::ifstream& input) {
    int n, frequency = 0;

    while (input >> n) {
        frequency += n;
    }
    return frequency;
}

int problemB(std::ifstream& input) {
    int n, frequency = 0;
    std::unordered_set<int> frequencies;

    while (true) {
        if (input >> n) {
            if (!frequencies.insert(frequency += n).second) return frequency;
        } else {
            input.clear();
            input.seekg(0);
        }
    }
}

int main(char argc, char** argv) {
    std::ifstream input("..\\input_01.txt");
    if (!input.is_open()) {
        std::cout << "Could not open file" << std::endl;
        return 1;
    }
    
    std::cout << "Frequency sum: " << problemA(input) << std::endl;
    input.clear();
    input.seekg(0);
    std::cout << "First recurring frequency: " << problemB(input) << std::endl;
    return 0;
}
