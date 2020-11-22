#include <algorithm>
#include <cctype>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>

using int2 = std::pair<int, int>;
int2 parse(const std::string& s) {
    size_t n = s.find(",");
    return std::make_pair(std::stoi(s.substr(0, n)), std::stoi(s.substr(n + 2)));
}

std::ostream& operator<<(std::ostream& os, const int2 m) {
    return os << m.first << ", " << m.second;
}

int2 getMax(const std::vector<int2>& coords) {
    return int2(
        std::max_element(coords.begin(), coords.end(), [](int2 x, int2 y) { return x.first < y.first; })->first,
        std::max_element(coords.begin(), coords.end(), [](int2 x, int2 y) { return x.second < y.second; })->second);
}

int dist(int2 a, int2 b) {
    return abs(a.first - b.first) + abs(a.second - b.second);
}

int2 operator+(int2 lhs, int2 rhs) {
    return int2(lhs.first + rhs.first, lhs.second + rhs.second);
}

template<class ForwardIt, class Compare>
std::pair<ForwardIt, ForwardIt> min2_element(ForwardIt first, ForwardIt last, Compare comp) {
    ForwardIt min1, min2;
    min1 = min2 = last;

    for (auto it = first; it != last; ++it) {
        if (min1 == last || comp(*it, *min1)) {
            min2 = min1;
            min1 = it;
        } else if (min2 == last || comp(*it, *min2)) {
            min2 = it;
        }
    }
    return std::make_pair(min1, min2);
}

class Grid {
public:
    Grid(int2 size) :
        _size(size)
        , _grid(size.first * size.second, -1) {
    }

    int& elem(int x, int y) {
        return _grid[x + y * _size.first];
    }

    std::unordered_map<int, int> getCountA() {
        std::unordered_map<int, int> result;
        for (int elem : _grid) {
            if (elem >= 0) {
                result[elem]++;
            }
        }
        for (int x  = 0; x < _size.first; ++x) {
            result[elem(x, 0)] = 0;
            result[elem(x, _size.second - 1)] = 0;
        }
        for (int y  = 0; y < _size.second; ++y) {
            result[elem(0, y)] = 0;
            result[elem(_size.first - 1, y)] = 0;
        }
        return result;
    }

    int getCount(int threshold) {
        return std::count_if(_grid.begin(), 
                             _grid.end(), 
                             [threshold](int x) {
                                return x < threshold;
                             });
    }

private:
    int2 _size;
    std::vector<int> _grid;
};

int problemA(const std::vector<int2>& coords) {
    int2 gridSize = getMax(coords) + int2(2, 2);
    Grid grid(gridSize);

    for (int y = 0; y < gridSize.second; ++y) {
        for (int x = 0; x < gridSize.first; ++x) {
            int2 gridCoord(x, y);
            auto min2 = min2_element(coords.begin(), 
                                     coords.end(), 
                                     [gridCoord](int2 lhs, int2 rhs) { 
                                         return dist(lhs, gridCoord) < dist(rhs, gridCoord); 
                                     });
            int2 c0 = *(min2.first);
            int2 c1 = *(min2.second);
            if (dist(c0, gridCoord) != dist(c1, gridCoord)) {
                grid.elem(x, y) = min2.first - coords.begin();
            }
        }
    }
    auto count = grid.getCountA();
    using pt = decltype(count)::value_type;
    return std::max_element(count.begin(), 
                            count.end(), 
                            [] (const pt& lhs, const pt& rhs) {
                                return lhs.second < rhs.second;  
                            })->second;

}

int problemB(const std::vector<int2>& coords) {
    int2 gridSize = getMax(coords) + int2(2, 2);
    Grid grid(gridSize);

    for (int y = 0; y < gridSize.second; ++y) {
        for (int x = 0; x < gridSize.first; ++x) {
            grid.elem(x, y) = std::accumulate(coords.begin(), 
                                              coords.end(), 
                                              0, 
                                              [x, y](int lhs, int2 rhs) {
                                                  return lhs + dist(rhs, int2(x, y));
                                              });
        }
    }
    return grid.getCount(10000);
}



int main(int, char**) {
    std::ifstream input("../input_06.txt");
    if (!input.is_open()) {
        std::cout << "Could not open file" << std::endl;
        return 1;
    }

    std::vector<int2> coords;
    std::string s;
    while (std::getline(input, s)) {
        coords.push_back(parse(s));
    }
    std::cout << problemA(coords) << std::endl;
    std::cout << problemB(coords) << std::endl;

    return 0;
}



