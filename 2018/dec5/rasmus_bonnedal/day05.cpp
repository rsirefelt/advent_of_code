#include <algorithm>
#include <cctype>
#include <fstream>
#include <iostream>
#include <string>

bool scanReplace(std::string& input) {
    const size_t len = input.length();
    size_t edi = 0;
    for (size_t i = 0; i < len; i++) {
        char c0 = input[i];
        if (i == len - 1) {
            input[edi++] = c0;
            break;
        }
        char c1 = input[i + 1];
        if (std::toupper(c0) != std::toupper(c1) || c0 == c1) {
            input[edi++] = c0;
        }
        else {
            i++;
        }
    }
    input.resize(edi);
    return len != edi;
}

void cut(std::string& input, char c) {
    char cref = std::toupper(c);
    const size_t len = input.length();
    size_t edi = 0;
    for (size_t i = 0; i < len; i++) {
        char c0 = input[i];
        if (std::toupper(c0) != cref) {
            input[edi++] = c0;
        }
    }
    input.resize(edi);
}

int problemA(const std::string& s) {
    std::string ws = s;
    while (scanReplace(ws));
    return static_cast<int>(ws.length());
}

int problemB(const std::string& s) {
    int shortest = 1000000;
    for (char c = 'a'; c <= 'z'; ++c) {
        std::string ws = s;
        cut(ws, c);
        while (scanReplace(ws));
        shortest = std::min(shortest, static_cast<int>(ws.length()));
    }
    return shortest;
}


int main(char argc, char** argv) {
    std::ifstream input("..\\input_05.txt");
    if (!input.is_open()) {
        std::cout << "Could not open file" << std::endl;
        return 1;
    }

    std::string s;
    input >> s;

    std::cout << problemA(s) << std::endl;
    std::cout << problemB(s) << std::endl;
    return 0;
}
