#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

using mapt = std::vector<std::vector<bool>>;

mapt parse_vec(const std::string& filename) {
    mapt retval;
    std::ifstream ifs(filename);
    if (ifs.fail()) {
        throw std::runtime_error("Could not open file");
    }
    std::string line;
    std::vector<bool> linedata;
    while(std::getline(ifs, line)) {
        linedata.resize(line.size());
        std::transform(line.begin(), line.end(), linedata.begin(), 
            [](auto c) { return c == '#';});
        retval.push_back(std::move(linedata));
    }
    return retval;
}

int walk(const mapt& m, int sx, int sy) {
    int x = 0;
    int y = 0;
    int trees = 0;

    int nrows = m.size();
    int ncols = m[0].size();
    while (y < nrows) {
        if (m[y][x % ncols]) {
            trees += 1;
        }
        x += sx;
        y += sy;
    }
    return trees;
}

int64_t try_walks(const mapt& m) {
    int64_t retval;
    retval = walk(m, 1, 1);
    retval *= walk(m, 3, 1);
    retval *= walk(m, 5, 1);
    retval *= walk(m, 7, 1);
    retval *= walk(m, 1, 2);
    return retval;
}

int main(int argc, char** argv) {
    auto indata = parse_vec("input");
    std::cout << "part 1: " << walk(indata, 3, 1) << std::endl;
    std::cout << "part 2: " << try_walks(indata) << std::endl;
    return 0;
}
