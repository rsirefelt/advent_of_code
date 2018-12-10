//#include <algorithm>
#include <fstream>
#include <iostream>
#include <regex>
#include <vector>

using int2 = std::pair<int, int>;
int2 make_int2(const std::string& s1, const std::string& s2) {
    return std::make_pair(std::stoi(s1), std::stoi(s2));
}

std::ostream& operator<<(std::ostream& stream, const int2& v) {
    return stream << "(" << v.first << ", " << v.second << ")";
}

class Point {
public:
    Point(const int2& pos, const int2& velocity) : 
        _position(pos)
        , _velocity(velocity) {
    }

    const int2& position() const {
        return _position;
    }

    const int2& velocity() const {
        return _velocity;
    }

    void move(int scale) {
        _position.first += _velocity.first * scale;
        _position.second += _velocity.second * scale;
    }

    void print(std::ostream& stream) const {
        stream << _position << " - " << _velocity;
    }
private:
    int2 _position;
    int2 _velocity;
};

std::ostream& operator<<(std::ostream& stream, const Point& v) {
    v.print(stream);
    return stream;
}

std::pair<int2, int2> getMinMaxSize(const std::vector<Point>& points) {
    int2 minv, maxv;
    minv = maxv = points[0].position();

    for (auto& ps : points) {
        minv.first = std::min(minv.first, ps.position().first);
        minv.second = std::min(minv.second, ps.position().second);
        maxv.first = std::max(maxv.first, ps.position().first);
        maxv.second = std::max(maxv.second, ps.position().second);
    }
    return std::make_pair(minv, maxv);
}

int2 getSize(const std::pair<int2, int2>& minMaxSize) {
    return std::make_pair(minMaxSize.second.first - minMaxSize.first.first + 1,
                          minMaxSize.second.second - minMaxSize.first.second + 1);
}

Point parse(const std::string& s) {
    std::regex re("position=<([\\ \\d-]+),([\\ \\d-]+)> velocity=<([\\ \\d-]+),([\\ \\d-]+)>");
    std::smatch m;
    if (!std::regex_search(s, m, re)) {
        throw std::runtime_error("Could not parse\"" + s + "\"");
    }
    return Point(make_int2(m[1], m[2]), make_int2(m[3], m[4]));
}

void printPoints(const std::vector<Point>& points) {
    std::pair<int2, int2> minmax = getMinMaxSize(points);
    int2 size = getSize(minmax);

    std::vector<char> field(size.first * size.second);

    std::fill(field.begin(), field.end(), '.');
    for (const auto& ps : points) {
        int x = ps.position().first - minmax.first.first;
        int y = ps.position().second - minmax.first.second;
        if (x >= 0 && y >= 0 && x < size.first && y < size.second) {
            field[x + size.first * y] = '#';
        }
    }
    for (size_t y = 0; y < size.second; ++y) {
        for (size_t x = 0; x < size.first; ++x) {
            std::cout << field[x + size.first * y];
        }
        std::cout << std::endl;
    }
}

int main(int, char**) {
    std::ifstream input("../input.txt");
    if (!input.is_open()) {
        std::cout << "Could not open file" << std::endl;
        return 1;
    }
    std::string s;
    std::vector<Point> points;
    while (std::getline(input, s)) {
        points.push_back(parse(s));
    }

    auto pointsStartState = points;
    int2 size = getSize(getMinMaxSize(points));
    int iteration = 0;
    while (true) {
        for (auto& p : points) p.move(1);
        int2 newSize = getSize(getMinMaxSize(points));
        if (newSize.first > size.first || newSize.second > size.second) {
            break;
        }
        size = newSize;
        iteration++;
    }
    std::cout << "Iteration " << iteration << std::endl;
    points = pointsStartState;
    for (auto& ps : points) ps.move(iteration);
    printPoints(points);

    return 0;
}
