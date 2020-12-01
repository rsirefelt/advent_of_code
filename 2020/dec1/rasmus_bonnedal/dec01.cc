#include <fstream>
#include <iostream>
#include <set>
#include <vector>

std::vector<int> parse_vec(const std::string& filename) {
	std::vector<int> retval;
	std::ifstream ifs(filename);
	if (ifs.fail()) {
		throw std::runtime_error("Could not open file");
	}
	int a;
	while(ifs >> a) {
		retval.push_back(a);
	}
	return retval;
}


int main(int argc, char** argv) {
	auto indata = parse_vec("input");
	std::set<int> indata_set(indata.begin(), indata.end());
	for (auto& i : indata) {
		if (indata_set.find(2020 - i) != indata_set.end()) {
			std::cout << i * (2020 - i) << std::endl;
		}
	}
	for (auto& i : indata) {
		for (auto& j : indata) {
			if (indata_set.find(2020 - i - j) != indata_set.end()) {
				std::cout << i * j * (2020 - i - j) << std::endl;
			}
		}
	}
	return 0;
}
