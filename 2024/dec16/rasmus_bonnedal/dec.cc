#define _CRT_SECURE_NO_WARNINGS
#include "ctl.hh"

#include <chrono>
#include <ctime>
#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>
#include <regex>
#include <unordered_set>

using namespace std;
using namespace ctl;

struct indata {
    map_t map;
    vec2 start;
    vec2 end;
};

std::string get_time() {
    auto end = std::chrono::system_clock::now();
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);
    return std::ctime(&end_time);
}

vec2 find_pos(const map_t& map, char c) {
    for (auto it = map.cbegin(); it != map.cend(); ++it) {
        if (*it == c) {
            return it.pos();
        }
    }
    throw runtime_error("Couldn't find " + c);
}


indata parse(const std::string& filename) {
    indata d;
    for (const auto& s : split(read_file(filename), "\n")) {
        d.map.map.push_back(s);
    }
    d.start = find_pos(d.map, 'S');
    d.map.set(d.start, '.');
    d.end = find_pos(d.map, 'E');
    d.map.set(d.end, '.');
    return d;
}

void print_map(const map_t& mp, const map<vec2, int>& scores, vec2 cur_pos = vec2(-1, -1)) {
    HANDLE hCons = GetStdHandle(STD_OUTPUT_HANDLE);
    for (auto it = mp.cbegin(); it != mp.cend(); ++it) {
        SetConsoleTextAttribute(hCons, it.pos() == cur_pos ? 10 : 7);
        if (*it == '#') print("######");
        if (*it == '.') {
            if (scores.count(it.pos())) {
                print("{:5} ", scores.at(it.pos()));
            }
            else {
                print("......");
            }
        }
        if (it.pos().x == (mp.width() - 1)) print("\n");
    }
}

template<class T>
void print_map(const map_t& mp, const T& scenic_route) {
    for (auto it = mp.cbegin(); it != mp.cend(); ++it) {
        if (*it == '#') print("#");
        if (*it == '.') {
            if (scenic_route.count(it.pos())) {
                print("O");
            }
            else {
                print(".");
            }
        }
        if (it.pos().x == (mp.width() - 1)) print("\n");
    }
}


int rot_diff(dir_t d1, dir_t d2) {
    int d = abs(int(d1) - int(d2));
    return d == 3 ? 1 : d;
}

dir_t rot_cw(dir_t d) {
    return dir_t((int(d) + 1) % 4);
}

dir_t rot_180(dir_t d) {
    return dir_t((int(d) + 2) % 4);
}

dir_t rot_ccw(dir_t d) {
    return dir_t((int(d) + 3) % 4);
}

struct score_t {
    int score = 0;
    int depth = 0;
};

void _find_best(const map_t& mp, vec2 pos, int score, dir_t dir, map<vec2, score_t>& scores, int depth) {
    if (scores.count(pos) > 0 && scores[pos].score <= score) return;
    scores[pos] = { score, depth };

    for (const auto new_dir : DIRS) {
        vec2 p = step(pos, new_dir);
        if (mp.get(p) == '.') {
            int new_score = score + 1 + 1000 * rot_diff(dir, new_dir);
            _find_best(mp, p, new_score, new_dir, scores, depth + 1);
        }
    }
    return;
}

int64_t find_best(const indata& data, map<vec2, score_t>& scores) {
    _find_best(data.map, data.start, 0, RIGHT, scores, 0);
    print("score: {}, depth: {}\n", scores[data.end].score, scores[data.end].depth);
    return scores[data.end].score;
}

using from_end_t = map<vec2, int>;

void _find_from_end(const map_t& mp, vec2 pos, int score, dir_t dir, from_end_t& scores) {
    if (scores.count(pos) > 0 && scores[pos] <= score) return;
    scores[pos] = score;
    for (const auto new_dir : DIRS) {
        vec2 new_pos = step(pos, new_dir);
        if (mp.get(new_pos) == '.') {
            int new_score = score + 1 + 1000 * rot_diff(dir, new_dir);
            _find_from_end(mp, new_pos, new_score, new_dir, scores);
        }
    }
}

from_end_t find_from_end(const indata& data) {
    from_end_t scores;
    _find_from_end(data.map, data.end, 0, DOWN, scores);
    return scores;
}

void find_best_2(const indata& data, const from_end_t& from_end, unordered_set<vec2> visited, map<int, set<vec2>>& scenic_route, int score, vec2 pos, dir_t dir) {
    static int64_t visits = 0;
    static int64_t rejects = 0;
    static timer total_timer;
    // if (visited.count(pos) > 0) return;

    visits++;
    visited.insert(pos);
    static size_t max_depth = 0;
    static timer last_print;
    max_depth = max(visited.size(), max_depth);

    int from_end_score = from_end.count(pos) > 0 ? from_end.at(pos) : -1;
    if (last_print() > 10) {
        last_print = timer();
        print_map(data.map, visited);
        int best_score = scenic_route.size() > 0 ? scenic_route.begin()->first : 0;
        size_t srl = scenic_route.size() > 0 ? scenic_route.begin()->second.size() : 0;
        print("{}: depth: {} score: {}\n", get_time(), visited.size(), score);
        print("From end: {}\n", from_end_score);

        print("max depth: {} max score: {} ({})\n", max_depth, best_score, srl);
        print("rejects: {}\n", rejects);
        //        print("visits: {} visits / s: {}\n", visits, visits / total_timer());
    }

    if (scenic_route.size() > 0 && scenic_route.begin()->first < score) {
        // This route is worse then current best, abort
        return;
    }

    if (pos == data.end) {
        print("Found route score: {}\n", score);
        scenic_route[score].insert(visited.begin(), visited.end());
        scenic_route[score].insert(pos);
        return;
    }


    int max_dist;
    if (data.map.width() > 15) {
        max_dist = 85420;
    }
    else {
        max_dist = 7036;
    }

    if (from_end_score > 0 && from_end_score + score > max_dist) {
        //print("Early out @ ({}, {}) ({} + {})\n", pos.x, pos.y, from_end_score, score);
        rejects++;
        return;
    }

    for (auto new_dir : { dir, rot_cw(dir), rot_ccw(dir) }) {
        vec2 new_pos = step(pos, new_dir);
        if (data.map.get(new_pos) == '.' && visited.count(new_pos) == 0) {
            int new_score = score + 1 + 1000 * rot_diff(dir, new_dir);
            find_best_2(data, from_end, visited, scenic_route, new_score, new_pos, new_dir);
        }
    }
}

int64_t part1(const indata& data) {
    int64_t result = 0;
    map<vec2, score_t> scores;
    result = find_best(data, scores);
    return result;
}

int64_t part2(const indata& data) {
    int64_t result = 0;
    std::unordered_set<vec2> visited;
    map<int, set<vec2>> scenic_route;
    from_end_t from_end = find_from_end(data);
    find_best_2(data, from_end, visited, scenic_route, 0, data.start, RIGHT);
    result = scenic_route.size() > 0 ? scenic_route.begin()->second.size() : -1;
    print_map(data.map, scenic_route.begin()->second);
    return result;
}

void test() {
}

int main(int argc, char** argv) {
    try {
        test();
        auto data = parse("..\\input.txt");
        print("width: {}\n", data.map.width());
        print("part1: {}\n", part1(data));
        print("part2: {}\n", part2(data));
    }
    catch (const std::exception& e) {
        std::print("Error: {}\n", e.what());
    }
    return 0;
}
