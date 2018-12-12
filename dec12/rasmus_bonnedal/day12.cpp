#include <fstream>
#include <iostream>
#include <string>
#include <vector>

std::vector<bool> parseInitial(const std::string& s) {
    std::vector<bool> result;
    for (auto c : s) {
        if (c == '#') result.push_back(true);
        if (c == '.') result.push_back(false);
    }
    return result;
}

int parseTransform(const std::string& s, bool& result) {
    int retval = 0;
    for (size_t i = 0; i < 5; ++i) {
        retval <<= 1;
        if (s[i] == '#') retval |= 1;
    }
    result = s[9] == '#';
    return retval;
}

template<typename Iterator>
bool isTrue(Iterator begin, Iterator end) {
    while(begin != end) {
        if (*begin++) return true;
    }
    return false;
}

int getNum(std::vector<bool>::const_iterator it) {
    int result = 0;
    for (int i = 0; i < 5; ++i) {
        result <<= 1;
        if (*it++) result |= 1;
    }
    return result;
}

void expand(std::vector<bool>& state, int64_t& leftIndex) {
    while (isTrue(state.begin(), state.begin() + 4)) {
        state.insert(state.begin(), false);
        leftIndex--;
    }
    while (!isTrue(state.begin(), state.begin() + 5)) {
        state.erase(state.begin());
        leftIndex++;
    }
    while (isTrue(state.end() - 4, state.end())) {
        state.push_back(false);
    }
    while (!isTrue(state.end() - 5, state.end())) {
        state.pop_back();
    }
}

std::vector<bool> transform(const std::vector<bool>& table, const std::vector<bool>& state) {
    std::vector<bool> result;
    result.resize(state.size(), false);
    for (size_t i = 0; i < state.size() - 4; ++i) {
        result[i + 2] = table[getNum(state.begin() + i)];
    }
    return result;
}

int64_t count(const std::vector<bool>& state, int64_t leftIndex) {
    int64_t result = 0;

    for (auto s : state) {
        if (s) result += leftIndex;
        leftIndex++;
    }
    return result;
}

int main(int, char**) {
    std::ifstream input("../input.txt");
    if (!input.is_open()) {
        std::cout << "Could not open file" << std::endl;
        return 1;
    }

    std::string s;
    std::getline(input, s);
    std::vector<bool> state = parseInitial(s);
    int64_t leftIndex = 0;
    std::getline(input, s);
    std::vector<bool> table(32, false);
    bool b;
    while (std::getline(input, s)) {
        int i = parseTransform(s, b);
        table[i] = b;
    }

    time_t startT = time(0);

    int64_t maxIt = 50000000000;
    for (int64_t i = 1; i <= maxIt; ++i) {
        expand(state, leftIndex);
        std::vector<bool> newState = transform(table, state);
        int oldLeftindex = leftIndex;
        expand(newState, leftIndex);
        if (newState == state) {
            std::cout << "Steady state detected" << std::endl;
            leftIndex += (leftIndex - oldLeftindex) * (maxIt - i);
            break;
        }
        state = newState;
        if (i == 20) {
            std::cout << "#20: " << count(state, leftIndex) << std::endl;
        }
    }
    std::cout << "#" << maxIt << ": " <<count(state, leftIndex) << std::endl;
    return 0;
}
