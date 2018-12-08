#include <fstream>
#include <iostream>
#include <memory>
#include <numeric>
#include <vector>

class Node {
public:
    void parse(const std::vector<int>& data, int& index) {
        int nChildren = data[index++];
        int nMetadata = data[index++];
        _children.reserve(nChildren);
        for (int i = 0; i < nChildren; ++i) {
            std::unique_ptr<Node> child = std::make_unique<Node>();
            child->parse(data, index);
            _children.push_back(std::move(child));
        }
        _metadata.reserve(nMetadata);
        for (int i = 0; i < nMetadata; ++i) {
            _metadata.push_back(data[index++]);
        }
    }

    int sum() const {
        int s = std::accumulate(_children.begin(), 
                                _children.end(), 
                                0, 
                                [](int lhs, const std::unique_ptr<Node>& n) { 
                                    return lhs + n->sum(); 
                                });
        return std::accumulate(_metadata.begin(), _metadata.end(), s);
    }

    int value() const {
        if (_children.size() == 0) {
            return sum();
        }
        int s = 0;
        for (int m : _metadata) {
            m--;
            if (size_t(m) < _children.size()) {
                s += _children[m]->value();
            }
        }
        return s;
    }

private:
    std::vector<std::unique_ptr<Node>> _children;
    std::vector<int> _metadata;
};

Node buildTree(std::istream& input) {
    std::vector<int> indata;
    int i;
    while (input >> i) {
        indata.push_back(i);
    }
    Node n;
    int index = 0;
    n.parse(indata, index);
    return n;
}

int main(int, char**) {
    std::ifstream input("../input_08.txt");
    if (!input.is_open()) {
        std::cout << "Could not open file" << std::endl;
        return 1;
    }

    Node n = buildTree(input);

    std::cout << n.sum() << std::endl;
    std::cout << n.value() << std::endl;
    return 0;
}
