#include <array>
#include <fstream>
#include <iostream>
#include <numeric>
#include <regex>
#include <string>
#include <unordered_map>
#include <vector>

enum Event {
    SHIFT_START,
    FALLS_ASLEEP,
    WAKES_UP
};

Event parse(const std::string& s, int& minute, int& id) {
    std::regex re("\\[\\d\\d\\d\\d-\\d\\d-\\d\\d \\d\\d:(\\d\\d)\\] (.*)");
    std::smatch m;
    if (std::regex_search(s, m, re)) {
        minute = std::stoi(m[1]);
        const std::string& rest = m[2];

        if (rest.find("falls asleep") != std::string::npos) {
            return FALLS_ASLEEP;
        }
        else if (rest.find("wakes up") != std::string::npos) {
            return WAKES_UP;
        }
        std::regex re2("#(\\d+)");
        std::smatch m2;
        if (std::regex_search(rest, m2, re2)) {
            id = std::stoi(m2[1]);
            return SHIFT_START;
        }
    }
    throw std::runtime_error("Could not parse " + s);
}

using MapType = std::unordered_map<int, std::array<int, 60>>;

MapType buildMap(const std::vector<std::string>& times) {
    int currentId = -1, startMinute = -1;
    MapType sleepTimes;
    for (auto& t : times) {
        int minute, id;
        switch (parse(t, minute, id)) {
        case SHIFT_START:
            currentId = id;
            break;
        case FALLS_ASLEEP:
            startMinute = minute;
            break;
        case WAKES_UP:
            if (currentId == -1 || startMinute == -1) {
                throw std::runtime_error("Malformed input");
            }
            for (int i = startMinute; i < minute; ++i) {
                sleepTimes[id][i]++;
            }
            startMinute = -1;
            break;
        }
    }
    return sleepTimes;
}

int problemA(MapType& sleepTimes) {
    int bestTime = 0, bestId;
    for (auto it = sleepTimes.begin(); it != sleepTimes.end(); ++it) {
        int time = std::accumulate(it->second.begin(), it->second.end(), 0);
        if (time > bestTime) {
            bestTime = time;
            bestId = it->first;
        }
    }
    const auto& t = sleepTimes[bestId];
    int minute = static_cast<int>(std::minmax_element(t.begin(), t.end()).second - t.begin());
    return bestId * minute;
}

int problemB(MapType& sleepTimes) {
    int bestTime = 0, bestIdMin;
    for (auto it = sleepTimes.begin(); it != sleepTimes.end(); ++it) {
        auto& t = it->second;
        auto& elem = std::minmax_element(t.begin(), t.end()).second;
        int minute = static_cast<int>(elem - t.begin());
        int time = *elem;

        if (time > bestTime) {
            bestTime = time;
            bestIdMin = it->first * minute;
        }
    }
    return bestIdMin;
}

int main(char argc, char** argv) {
    std::ifstream input("..\\input_04.txt");
    if (!input.is_open()) {
        std::cout << "Could not open file" << std::endl;
        return 1;
    }

    std::string s;
    std::vector<std::string> times;
    while (std::getline(input, s)) {
        times.push_back(s);
    }
    std::sort(times.begin(), times.end());
    MapType sleepTimes = buildMap(times);

    std::cout << problemA(sleepTimes) << std::endl;
    std::cout << problemB(sleepTimes) << std::endl;
    return 0;
}
