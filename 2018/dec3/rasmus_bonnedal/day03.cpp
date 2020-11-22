#include <fstream>
#include <iostream>
#include <regex>
#include <string>
#include <utility>
#include <vector>

using int2 = std::pair<int, int>;
int2 make_int2(const std::string& s1, const std::string& s2) {
    return std::make_pair(std::stoi(s1), std::stoi(s2));
}

using PosSize = std::pair<int2, int2>;

PosSize parse(const std::string& s) {
    std::regex re("#\\d+ @ (\\d+)\\,(\\d+): (\\d+)x(\\d+)");
    std::smatch m;
    if (std::regex_search(s, m, re)) {
        return std::make_pair(make_int2(m[1], m[2]), make_int2(m[3], m[4]));
    }
    throw std::runtime_error("Could not parse " + s);
}

int2 getMaxSize(const std::vector<PosSize>& posSizeVec) {
    int maxX = 0, maxY = 0;
    for (auto& ps : posSizeVec) {
        maxX = std::max(maxX, ps.first.first + ps.second.first);
        maxY = std::max(maxY, ps.first.second + ps.second.second);
    }
    return std::make_pair(maxX, maxY);
}

int problemA(const std::vector<PosSize>& posSizeVec, std::vector<int>& board) {
    int2 extents = getMaxSize(posSizeVec);
    board = std::vector<int>(extents.first * extents.second, 0);
    int claims = 0;
    for (auto& ps : posSizeVec) {
        int2 pos = ps.first;
        int2 size = ps.second;
        for (int y = 0; y < size.second; ++y) {
            for (int x = 0; x < size.first; ++x) {
                if (board[(y + pos.second) * extents.first + (x + pos.first)]++ == 1) {
                    claims++;
                }
            }
        }
    }
    return claims;
}

int problemB(const std::vector<PosSize>& posSizeVec, const std::vector<int>& board) {
    int2 extents = getMaxSize(posSizeVec);

    size_t len = posSizeVec.size();
    for (int i = 0; i < len; ++i) {
        const PosSize& ps = posSizeVec[i];
        int2 pos = ps.first;
        int2 size = ps.second;
        int claims = 0;
        for (int y = 0; y < size.second; ++y) {
            for (int x = 0; x < size.first; ++x) {
                claims += board[(y + pos.second) * extents.first + (x + pos.first)];
            }
        }
        if (claims == size.first * size.second) {
            return i;
        }
    }
    throw std::runtime_error("Could not find a clean claim");
}

int main(char argc, char** argv) {
    std::ifstream input("..\\input_03.txt");
    if (!input.is_open()) {
        std::cout << "Could not open file" << std::endl;
        return 1;
    }

    std::string s;
    std::vector<PosSize> posSizeVec;
    while (std::getline(input, s)) {
        int2 pos, size;
        posSizeVec.push_back(parse(s));
    }

    std::vector<int> board;
    std::cout << "Double claims: " << problemA(posSizeVec, board) << std::endl;
    std::cout << "Free claim id: " << problemB(posSizeVec, board) + 1 << std::endl;
    return 0;
}
