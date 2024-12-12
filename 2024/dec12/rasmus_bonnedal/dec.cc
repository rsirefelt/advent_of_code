#include "ctl.hh"

#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>
#include <regex>

using namespace std;
using namespace ctl;

using indata = map_t;

indata parse(const std::string& filename) {
    indata d;
    for (const auto& s : split(read_file(filename), "\n")) {
        d.map.push_back(s);
    }
    return d;
}

map_t empty_map(const map_t& src) {
    map_t m;
    for (int y = 0; y < src.height(); ++y) {
        m.map.push_back(string(src.width(), '.'));
    }
    return m;
}

void flood_fill(const indata& data, char c, map_t& plot, map_t& taken, vec2 pos) {
    if (!plot.is_inside(pos)) return;
    if (plot.get(pos) != '.') return;
    if (data.get(pos) != c) return;
    plot.set(pos, c);
    taken.set(pos, '#');
    for (auto dir : DIRS) {
        flood_fill(data, c, plot, taken, step(pos, dir));
    }
}

int64_t count_fence(const map_t& plot, int64_t& area) {
    int64_t fence = 0;
    area = 0;

    for (auto it = plot.cbegin(); it != plot.cend(); ++it) {
        if (*it != '.') {
            area++;
            for (auto dir : DIRS) {
                if (plot.get(step(it.pos(), dir)) == '.') fence++;
            }
        }
    }
    return fence;
}

int64_t count(const indata& data, map_t& taken, vec2 pos) {
    if (taken.get(pos) != '.') {
        return 0;
    }
    map_t plot = empty_map(data);
    flood_fill(data, data.get(pos), plot, taken, pos);
    int64_t area;
    int64_t fence = count_fence(plot, area);
    return area * fence;
}

using fence_piece = pair<vec2, vec2>;

dir_t get_dir(const fence_piece& fp) {
    if (fp.first == fp.second) throw runtime_error("Impossible direction");
    if (fp.first.y == fp.second.y) return RIGHT;
    if (fp.first.x == fp.second.x) return UP;
    throw runtime_error("Impossible direction");
}

int64_t count_fence_segments(const vector<fence_piece>& fence) {
    dir_t last_dir = get_dir(fence.back());

    int corners = 0;
    for (const auto& fp: fence) {
        dir_t dir = get_dir(fp);
        if (last_dir != dir) {
            corners++;
            last_dir = dir;
        }
    }
    return corners;
}

int64_t count_fence2(const map_t& plot) {
    int64_t area = 0;
    vector<fence_piece> fence_pieces;
    vector<vector<fence_piece>> fences;

    for (auto it = plot.cbegin(); it != plot.cend(); ++it) {
        if (*it != '.') {
            const vec2 p = it.pos();
            area++;
            if (plot.get(step(p, UP)) == '.') fence_pieces.push_back(make_pair(p, step(p, RIGHT)));
            if (plot.get(step(p, DOWN)) == '.') fence_pieces.push_back(make_pair(step(step(p, RIGHT), DOWN), step(p, DOWN)));
            if (plot.get(step(p, RIGHT)) == '.') fence_pieces.push_back(make_pair(step(p, RIGHT), step(step(p, RIGHT), DOWN)));
            if (plot.get(step(p, LEFT)) == '.') fence_pieces.push_back(make_pair(step(p, DOWN), p));
        }
    }
    while (fence_pieces.size() > 0) {
        vector<fence_piece> fence;
        fence.push_back(fence_pieces[0]);
        fence_pieces.erase(fence_pieces.begin());

        while (fence.begin()->first != fence.back().second) {
            for (int i = 0; i < fence_pieces.size(); ++i) {
                const fence_piece p = fence_pieces[i];
                if (fence.back().second == p.first) {
                    fence_pieces.erase(fence_pieces.begin() + i--);
                    fence.push_back(p);
                }
            }
        }
        fences.push_back(fence);
    }
    int64_t segments = 0;
    for (const auto& fence : fences) {
        segments += count_fence_segments(fence);
    }
    return area * segments;
}

int64_t count2(const indata& data, map_t& taken, vec2 pos) {
    if (taken.get(pos) != '.') {
        return 0;
    }
    map_t plot = empty_map(data);
    flood_fill(data, data.get(pos), plot, taken, pos);
    return count_fence2(plot);
}


int64_t part1(const indata& data) {
    int64_t result = 0;
    map_t taken = empty_map(data);
    for (auto it = data.cbegin(); it != data.cend(); ++it) {
        result += count(data, taken, it.pos());
    }
    return result;
}

int64_t part2(const indata& data) {
    int64_t result = 0;
    map_t taken = empty_map(data);
    for (auto it = data.cbegin(); it != data.cend(); ++it) {
        result += count2(data, taken, it.pos());
    }
    return result;
}

void test() {
}

int main(int argc, char** argv) {
    try {
        test();
        auto data = parse("..\\input.txt");
        print("part1: {}\n", part1(data));
        print("part2: {}\n", part2(data));
    }
    catch (const std::exception& e) {
        std::print("Error: {}\n", e.what());
    }
    return 0;
}
