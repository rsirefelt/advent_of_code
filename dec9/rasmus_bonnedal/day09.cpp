#include <algorithm>
#include <fstream>
#include <iostream>
#include <list>
#include <numeric>
#include <regex>
#include <vector>

template<class Base>
class circular_iterator : public Base {
public:
    circular_iterator(Base begin, Base end) :
        Base(begin)
        ,_begin(begin)
        , _end(end) {
    }

    void set(Base begin, Base end, Base current) {
        _begin = begin;
        _end = end;
        Base::operator=(current);
    }

    circular_iterator& operator++(void) {
        if (_begin == _end) {
            return *this;
        }
        if (_end == *this) {
            Base::operator=(_begin);
        }
        Base::operator++();
        if (_end == *this) {
            Base::operator=(_begin);
        }
        return *this;
    }

    circular_iterator& operator--(void) {
        if (_begin == *this) {
            Base::operator=(_end);
        }
        Base::operator--();
        return *this;
    }
private:
    Base _begin, _end;
};

class MarbleCircle {
public:
    MarbleCircle() :
        _marbles()
        , _current(_marbles.begin(), _marbles.end()) {
    }

    int place(int marble) {
        int score = 0;
        if (marble > 0 && marble % 23 == 0) {
            for (int i = 0; i < 7; ++i) {
                --_current;
            }
            score = marble + *_current;
            auto newCurrent = _current;
            ++newCurrent;
            _marbles.erase(_current);
            _current = newCurrent;
        }
        else {
            ++_current;
            decltype(_marbles)::iterator it = _current;
            if (it != _marbles.end()) ++it;
            it = _marbles.insert(it, marble);
            _current.set(_marbles.begin(), _marbles.end(), it);
        }
        return score;
    }

    void print(std::ostream& stream) const {
        for (auto it = _marbles.begin(); it != _marbles.end(); ++it) {
            if (it == _current) {
                stream << " (" << *it << ") ";
            }
            else {
                stream << "  " << *it << "  ";
            }
        }
    }
private:
    std::list<int> _marbles;
    circular_iterator<std::list<int>::iterator> _current;
};

std::ostream& operator<<(std::ostream& stream, const MarbleCircle& mc) {
    mc.print(stream);
    return stream;
}

int64_t problemAB(int nPlayers, int nMaxMarble) {
    MarbleCircle mc;
    mc.place(0);
    std::vector<int64_t> players(nPlayers);

    size_t curPlayer = 0;
    for (int i = 1; i <= nMaxMarble; ++i) {
        players[curPlayer] += mc.place(i);
        //std::cout << "[" << curPlayer << "] " << mc << std::endl;
        curPlayer = (curPlayer + 1) % nPlayers;
    }
    return *std::max_element(players.begin(), players.end());
}

int main(int, char**) {
    std::ifstream input("../input.txt");
    if (!input.is_open()) {
        std::cout << "Could not open file" << std::endl;
        return 1;
    }
    std::string s;
    std::getline(input, s);
    std::regex re("(\\d+) players; last marble is worth (\\d+) points");
    std::smatch m;
    if (!std::regex_search(s, m, re) || m.size() != 3) {
        std::cout << "Error parsing input" << std::endl;
        return 1;
    }
    int nPlayers = std::stoi(m[1]);
    int nMaxMarble = std::stoi(m[2]);
    
    std::cout << problemAB(nPlayers, nMaxMarble) << std::endl;
    std::cout << problemAB(nPlayers, nMaxMarble * 100) << std::endl;
    return 0;
}
