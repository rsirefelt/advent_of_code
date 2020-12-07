#include <fstream>
#include <iostream>
#include <map>
#include <regex>

using namespace std;

struct Rule
{
  string name;
  map<string, Rule> contains;
};

Rule createRule(string line)
{
  Rule outRule;
  std::smatch sm;
  regex re("(\\w+\\s\\w+)\\sbags\\scontain\\s(.*).");
  regex_match(line, sm, re);
  string name = sm[1];
  cout << line << "\n" << sm[2]<< "\n";
  return Rule {"test",map<string, Rule>()};
}

int main()
{
  ifstream infile("input.txt");
  string ruleString;
  map<string, Rule> ruleMap;
  while (getline(infile,ruleString))
  {
    cout << ruleString << "\n";

    Rule newRule = createRule(ruleString);
    ruleMap[newRule.name] = newRule;
  }
}
