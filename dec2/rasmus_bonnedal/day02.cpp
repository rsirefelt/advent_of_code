#include <fstream>
#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>

void countString(const std::string& s, bool& hasTwo, bool& hasThree) {
    std::unordered_map<char, int> counts;
    for (auto c : s) {
        counts[c]++;
    }
    hasTwo = false;
    hasThree = false;
    for (auto kv : counts) {
        if (kv.second == 2) {
            hasTwo = true;
        }
        if (kv.second == 3) {
            hasThree = true;
        }
        if (hasTwo && hasThree) {
            return;
        }
    }
}

int distance(const std::string& s1, const std::string& s2) {
    int d = 0;
    for (int i = 0; i < s1.size(); ++i) {
        if (s1[i] != s2[i]) d++;
    }
    return d;
}

std::string common(const std::string& s1, const std::string& s2) {
    std::string s;
    for (int i = 0; i < s1.size(); ++i) {
        if (s1[i] == s2[i]) s += s1[i];
    }
    return s;
}

int problemA(const std::vector<std::string>& boxes) {
    int twos = 0, threes = 0;

    for (auto& s : boxes) {
        bool hasTwo, hasThree;
        countString(s, hasTwo, hasThree);
        if (hasTwo) twos++;
        if (hasThree) threes++;
    }
    return twos * threes;
}

std::string problemB(const std::vector<std::string>& boxes) {
    size_t len = boxes.size();
    for (int i = 0; i < len; i++) {
        for (int j = i + 1; j < len; j++) {
            if (distance(boxes[i], boxes[j]) == 1) {
                return common(boxes[i], boxes[j]);
            }
        }
    }
}

int main(char argc, char** argv) {
    std::ifstream input("..\\input_02.txt");
    if (!input.is_open()) {
        std::cout << "Could not open file" << std::endl;
        return 1;
    }

    std::string s;
    std::vector<std::string> boxes;
    while (input >> s) {
        boxes.push_back(s);
    }
    std::cout << "Checksum: " << problemA(boxes) << std::endl;
    std::cout << "Common letters: " << problemB(boxes) << std::endl;

    return 0;
}
