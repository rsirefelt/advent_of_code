#include <fstream>
#include <iostream>
#include <memory>
#include <numeric>
#include <vector>

class MarbleCircle {
public:
    int place(int marble) {
        int score = 0;
        if (marble == 0) {
            _marbles.push_back(marble);
            _current = 0;
        } else if (marble == 1) {
            _marbles.push_back(marble);
            _current = 1;
        } else if (marble % 23 == 0) {
            int i = index(-7);
            score = marble + _marbles.at(i);
            _marbles.erase(_marbles.begin() + i);
            _current = i % _marbles.size();
        } else {
            _current = _marbles.insert(_marbles.begin() + index(1) + 1, marble) - _marbles.begin();
        }
        return score;
    }

    void print(std::ostream& stream) const {
        for (size_t i = 0; i < _marbles.size(); ++i) {
            if (i == _current) {
                stream << " (" << _marbles[i] << ") ";
            } else {
                stream << "  " << _marbles[i] << "  ";
            }
        }
    }
private:
    size_t index(size_t offset) {
        return (_current + offset + _marbles.size()) % _marbles.size();
    }

    std::vector<int> _marbles;
    size_t _current;
};

std::ostream& operator<<(std::ostream& stream, const MarbleCircle& mc) {
    mc.print(stream);
    return stream;
}

int problemA(int nPlayers, int nMaxMarble) {
    MarbleCircle mc;
    mc.place(0);
    std::vector<int> players(nPlayers);

    size_t curPlayer = 0;
    for (int i = 1; i <= nMaxMarble; ++i) {
        players[curPlayer] += mc.place(i);
//        std::cout << "[" << (curPlayer + 1) << "] " << mc << std::endl;
        curPlayer = (curPlayer + 1) % nPlayers;
        if (i % 10000 == 0) {
            std::cout << "marble: " << i << std::endl;
        }
    }
    return *std::max_element(players.begin(), players.end());
}

int main(int, char**) {
    std::cout << problemA(438, 71626) << std::endl;
    std::cout << problemA(438, 7162600) << std::endl;
    return 0;
}
