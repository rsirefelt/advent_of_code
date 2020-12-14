#include "ctl.hh"

#include <assert.h>
#include <iostream>
#include <sys/time.h>

using indata_t = std::vector<std::pair<std::string, std::string>>;

indata_t parse(const std::string& filename) {
    auto x = split(read_file(filename), "\n");
    indata_t retval;
    for (const auto& y: x) {
        auto z = split(y, " = ");
        retval.push_back(make_pair(z[0], z[1]));
    }
    return retval;
}

int64_t parse_addr(const std::string& addr) {
    return std::stoll(split(split(addr, "[")[1], "]")[0]);
}

using mem_t = std::map<int64_t, int64_t>;

mem_t process1(const indata_t& indata) {
    mem_t mem;
    std::string mask;
    for (auto& x: indata) {
        if (x.first == "mask") {
            mask = x.second;
        } else {
            int64_t addr = parse_addr(x.first);
            int64_t value = std::stoll(x.second);
            for (int bit = 0; bit < 36; ++bit) {
                if (mask[bit] == '1') {
                    setbit(value, bit);
                } else if (mask[bit] == '0') {
                    clearbit(value, bit);
                }
            }
            mem[addr] = value;
        }
    }
    return mem;
}

void addresses(std::vector<int64_t>& addrs, const std::string& mask, int64_t addr, int bit = 0) {
    while(bit < 36) {
        if (mask[bit] == '1') {
            setbit(addr, bit);
        } else if (mask[bit] == 'X') {
            setbit(addr, bit);
            addresses(addrs, mask, addr, bit + 1);
            clearbit(addr, bit);
        }
        bit++;
    }
    addrs.push_back(addr);
}

mem_t process2(const indata_t& indata) {
    mem_t mem;
    std::string mask;
    for (auto& x: indata) {
        if (x.first == "mask") {
            mask = x.second;
        } else {
            int64_t addr = parse_addr(x.first);
            int64_t value = std::stoll(x.second);
            std::vector<int64_t> addrs;
            addresses(addrs, mask, addr);
            for (auto& naddr: addrs) {
                mem[naddr] = value;
            }
        }
    }
    return mem;
}

int64_t sum(const mem_t& mem) {
    int64_t sum = 0;
    for (auto& x: mem) {
        sum += x.second;
    }
    return sum;
}

int main(int argc, char** argv) {
    auto indata = parse("input");
    auto mem1 = process1(indata);
    std::cout << "Part 1: " << sum(mem1) << std::endl;
    auto mem2 = process2(indata);
    std::cout << "Part 2: " << sum(mem2) << std::endl;
    return 0;
}
