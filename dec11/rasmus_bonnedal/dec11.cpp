#include <cassert>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>

class Grid {
public:
    Grid(int serial) :
        _grid(300 * 300)
        , _serial(serial) {
        calc();
    }

    std::pair<int, int> findMax(int minSize, int maxSize, int& bestSize) const {
        int best = 0;
        std::pair<int, int> bestCoord;
        for (int size = minSize; size <= maxSize; ++size) {
            for (int y = 1; y < 302 - size; ++y) {
                for (int x = 1; x < 302 - size; ++x) {
                    int s = sum(x, y, size);
                    if (s > best) {
                        bestCoord = std::make_pair(x, y);
                        best = s;
                        bestSize = size;
                    }
                }
            }
        }
        return bestCoord;
    }


    static int calc(int x, int y, int serial) {
        return ((x + 10) * y + serial) * (x + 10) / 100 % 10 - 5;
    }

private:
    int sum(int x, int y, int size) const {
        int s = 0;
        auto it = _grid.begin() + index(x, y);

        for (int yp = 0; yp < size; ++yp) {
            s += std::accumulate(it, it + size, 0);
            it += 300;
        }
        return s;
    }

    int& get(int x, int y) {
        return _grid[index(x, y)];
    }

    int index(int x, int y) const {
        assert(x >= 1 && x <= 300 && y >= 1 && y <= 300);
        return (x - 1) + (y - 1) * 300;
    }

    void calc() {
        for (int y = 1; y <= 300; ++y) {
            for (int x = 1; x <= 300; ++x) {
                get(x, y) = calc(x, y, _serial);
            }
        }
    }
    std::vector<int> _grid;
    int _serial;
};

int main(int argc, char** argv) {
    assert(Grid::calc(3, 5, 8) == 4);
    assert(Grid::calc(122, 79, 57) == -5);
    assert(Grid::calc(217, 196, 39) == 0);
    assert(Grid::calc(101, 153, 71) == 4);
    Grid g(2866);
    int bestSize;
    std::pair<int, int> v = g.findMax(3, 3, bestSize);
    std::cout << v.first << "," << v.second << std::endl;
    v = g.findMax(1, 300, bestSize);
    std::cout << v.first << "," << v.second << "," << bestSize << std::endl;
}
