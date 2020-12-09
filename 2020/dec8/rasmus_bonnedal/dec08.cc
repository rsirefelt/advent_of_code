#include "ctl.hh"

#include <iostream>

enum {
    JMP,
    NOP,
    ACC
};

using indata = std::vector<std::pair<int, int>>;

int tokenize(const std::string& s) {
    static const std::map<std::string, int> tokens = {
        { "jmp", JMP },
        { "nop", NOP },
        { "acc", ACC }
    };
    return tokens.at(s);
}

indata parse(const std::string& filename) {
    return map([](const std::string& line) {
        auto sv = split(line, " ");
        return std::make_pair(tokenize(sv[0]), std::stoi(sv[1]));
    }, split(read_file(filename), "\n"));
}

template<typename F>
bool execute(indata& program, int& acc, F patch) {
    int ip = 0;
    acc = 0;
    int program_length = program.size();
    std::set<int> visited;

    while(visited.find(ip) == visited.end()) {
        visited.insert(ip);
        int insn = patch(ip, program[ip].first);
        int arg = program[ip].second;

        if (insn == ACC) {
            acc += arg;
        } else if (insn == JMP) {
            ip += arg - 1;
        }
        ip++;
        if (ip == program_length) {
            return true;
        }
    }
    return false;
}

int main(int argc, char** argv) {
    auto nopatch = [](int ip, int insn) { return insn; };
    auto indata = parse("input");

    int acc;
    execute(indata, acc, nopatch);
    std::cout << "Part 1: " << acc << std::endl;

    for (int i = 0; i < indata.size(); ++i) {
        auto patch_i = [i](int ip, int insn) {
            if (ip == i) {
                if (insn == NOP) return (int)JMP;
                if (insn == JMP) return (int)NOP;
            }
            return insn;
        };
        if (execute(indata, acc, patch_i)) {
            break;
        }
    }
    std::cout << "Part 2: " << acc << std::endl;
    return 0;
}
