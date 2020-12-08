#include <fstream>
#include <iostream>
#include <vector>
#include <regex>

using namespace std;

enum Instruction
{
  nop,
  acc,
  jmp

};

struct Operation
{
  Instruction intstruction;
  int value;
};

Operation createOperation(string line)
{
  Operation out;
  std::smatch sm;
  regex re("(acc|nop|jmp) ([+-]\\d+)");
  regex_match(line, sm, re);
  if (sm[1] == "acc")
  {
    out.intstruction = Instruction::acc;
    out.value = stoi(sm[2]);
  }
  else if (sm[1] == "nop")
  {
    out.intstruction = Instruction::nop;
    out.value = stoi(sm[2]);
  }
  if (sm[1] == "jmp")
  {
    out.intstruction = Instruction::jmp;
    out.value = stoi(sm[2]);
  }
  return out;
}

bool runCode(const vector<Operation> &operations, int &result)
{
  vector<bool> visited(operations.size(), false);
  result = 0;
  int index = 0;
  bool return_val = true;
  while (true)
  {
    if (index >= operations.size())
    {
      break;
    }
    if (visited[index])
    {
      return_val = false;
      break;
    }
    visited[index] = true;
    const Operation &currentOp = operations[index];
    switch (currentOp.intstruction)
    {
    case acc:
      result += currentOp.value;
      index++;
      break;
    case nop:
      index++;
      break;
    case jmp:
      index += currentOp.value;
      break;
    }
  }
  return return_val;
}

int main()
{
  ifstream infile("input.txt");
  string line;
  vector<Operation> operations;
  while (getline(infile, line))
  {
    Operation operation = createOperation(line);
    operations.push_back(operation);
  }
  int result = 0;
  bool end = runCode(operations, result);
  cout << "Acc: " << result << "\n";

  for (int i = 0; i < operations.size(); i++)
  {
    result = 0;

    vector<Operation> operations_copy = operations;
    switch (operations_copy[i].intstruction)
    {
    case nop:
      operations_copy[i].intstruction = jmp;
      break;
    case jmp:
      operations_copy[i].intstruction = nop;
      break;
    }
    bool end = runCode(operations_copy, result);
    if (end)
    {
      break;
    }
  }
  cout << "Acc2: " << result << "\n";
}