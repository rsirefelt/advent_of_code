#define _CRT_SECURE_NO_WARNINGS
#include "ctl.hh"

#include <chrono>
#include <ctime>
#include <iostream>
#include <assert.h>
#include <math.h>
#include <print>
#include <regex>
#include <unordered_set>

using namespace std;
using namespace ctl;


struct indata {
    int64_t A, B, C;
    int64_t IP;
    vector<int> prog;
};

template <>
struct std::formatter<indata> : std::formatter<std::string> {
    auto format(const indata& p, format_context& ctx) const {
        string v;
        for (auto i : p.prog) {
            v += to_string(i) + ", ";
        }
        return formatter<string>::format(
            std::format("A: {}\nB: {}\nC: {}\nIP: {}\nProgram: {}", p.A, p.B, p.C, p.IP, v), ctx);
    }
};

indata parse(const std::string& filename) {
    indata d;
    for (const auto& s : split(read_file(filename), "\n")) {
        if (in("A", s)) {
            d.A = stoint(split(s, " ")[2]);
        }
        if (in("B", s)) {
            d.B = stoint(split(s, " ")[2]);
        }
        if (in("C", s)) {
            d.C = stoint(split(s, " ")[2]);
        }
        if (in(",", s)) {
            d.prog = mapf(stoint, split(split(s, ":")[1], ","));
        }
    }
    d.IP = 0;
    return d;
}

int64_t get_op(const indata& data, int operand) {
    switch (operand) {
    case 0: return 0;
    case 1: return 1;
    case 2: return 2;
    case 3: return 3;
    case 4: return data.A;
    case 5: return data.B;
    case 6: return data.C;
    case 7: throw runtime_error("Reserved");
    default: throw runtime_error("Illegal operand");
    }
}

/*
2, 4:   bst B = A & 7
1, 3:   bxl B = B ^ 3
7, 5:   cdv C = A / (1 << B)
4, 1:   bxc B = B ^ C
1, 3:   bxl B = B ^ 3
0, 3:   adv A = A / 8
5, 5:   out B & 7
3, 0:   jnz 

while (A > 0) {
    B = (A & 7) ^ 3
    C = A / (1 << B)
    B = B ^ C ^ 3
    A = A >> 3
    out B & 7
}

A: aaa
B: aa'a'
C = A / (1 << B)
B = aaa ^ ccc
out = aaa ^ ccc = 0


000
*/
int64_t find_digit2(const int64_t Ao, const vector<int>& prog, int digit) {
    if (digit < 0) {
        return Ao;
    }
    for (int n = 0; n < 8; n++) {
        int64_t A = (Ao << 3) | n;
        if (A == 0) continue;

        int64_t B = (A & 7) ^ 3;
        int64_t C = A / (1LL << B);
        B = B ^ C ^ 3;
        if ((B & 7) == prog[digit]) {
            int64_t A_prim = find_digit2(A, prog, digit - 1);
            if (A_prim != 0) {
                return A_prim;
            }
        }
    }
    return 0;
}

void step(indata& data, vector<int>& output) {
    int opcode = data.prog.at(data.IP++);
    int operand = data.prog.at(data.IP++);
    switch (opcode) {
    case 0:
        data.A = data.A / (1LL << get_op(data, operand));
        break;
    case 1:
        data.B = data.B ^ operand;
        break;
    case 2:
        data.B = get_op(data, operand) & 7;
        break;
    case 3:
        if (data.A != 0) data.IP = operand;
        break;
    case 4:
        data.B = data.B ^ data.C;
        break;
    case 5:
        output.push_back(get_op(data, operand) & 7);
        break;
    case 6:
        data.B = data.A / (1LL << get_op(data, operand));
        break;
    case 7:
        data.C = data.A / (1LL << get_op(data, operand));
        break;
    default:
        throw runtime_error("Illegal opcode");
    }
}

bool test_number(indata data, int64_t number, bool show) {
    data.A = number;
    vector<int> output;
    while (data.IP < (int64_t)data.prog.size()) {
        step(data, output);
    }
    if (show) {
        print("data.A: {}\nProg: {}\nOutput: {}\n", number, join(",", data.prog), join(",", output));
    }
    return output == data.prog;
}

string part1(const indata& data) {
    vector<int> output;
    indata d = data;
    while (d.IP < (int64_t)d.prog.size()) {
        step(d, output);
    }
    return join(",", output);
}

int64_t part2(const indata& data) {
    int64_t result = 0;
    result = find_digit2(0, data.prog, (int)data.prog.size() - 1);
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
