#include <fstream>
#include <iostream>
#include <map>
#include <regex>

using namespace std;

struct Rule
{
  string name;
  map<string, int> contains;
};

Rule createRule(string line)
{
  Rule outRule;
  std::smatch sm;
  regex re("(\\w+\\s\\w+)\\sbags\\scontain\\s(.*).");
  regex_match(line, sm, re);
  outRule.name = sm[1];
  if (sm[2] == "no other bags")
    return Rule{"test", map<string, int>()};

  re = regex("(\\d) (\\w+ \\w+) (?:bags|bag)");
  string nextLine = sm[2].str();
  while (regex_search(nextLine, sm, re))
  {
    outRule.contains[sm[2]] = stoi(sm[1]);
    nextLine = sm.suffix();
  }
  return outRule;
}

bool canContain(string color, Rule rule, map<string, Rule> &ruleMap)
{
  for (auto nextRule : rule.contains)
  {
    if (nextRule.first == color || canContain(color, ruleMap[nextRule.first], ruleMap))
      return true;
  }
  return false;
}

int contains(string color, Rule rule, map<string, Rule> &ruleMap)
{
  int otherbags = 1;
  for (auto nextRule : rule.contains)
  {
    otherbags += nextRule.second * contains(color, ruleMap[nextRule.first], ruleMap);
  }
  return otherbags;
}

int main()
{
  ifstream infile("input.txt");
  string ruleString;
  map<string, Rule> ruleMap;
  while (getline(infile, ruleString))
  {
    //cout << ruleString << "\n";
    Rule newRule = createRule(ruleString);
    ruleMap[newRule.name] = newRule;
  }
  int count = 0;
  for (auto rulePair : ruleMap)
  {
    if (canContain("shiny gold", rulePair.second, ruleMap))
    {
      count++;
    }
  }
  cout << "Count: " << count << "\n";

  int other = contains("shiny gold", ruleMap["shiny gold"], ruleMap);
  cout << "shiny gold Contains: " << other - 1; //Remove one for itself;
}
