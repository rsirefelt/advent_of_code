#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <set>
#include <vector>

using namespace std;

set<char> getGroupAnswers(std::ifstream &infile)
{
  set<char> answers;
  string line;
  while (getline(infile, line))
  {
    cout << line << "\n";
    if (line.empty())
      break;

    for (char c : line)
    {
      answers.insert(c);
    }
  }
  return answers;
}

set<char> getSameGroupAnswers(std::ifstream &infile)
{
  set<char> groupAnswers;
  set<char> intersect;
  string line;
  bool first = true;
  while (getline(infile, line))
  {
    set<char> answer;

    cout << line << "\n";
    if (line.empty())
      break;

    for (char c : line)
    {
      answer.insert(c);
    }
    if (first)
    {
      groupAnswers = answer;
      first = false;
    }
    else
    {
      intersect.clear();
      set_intersection(answer.begin(), answer.end(), groupAnswers.begin(), groupAnswers.end(), std::inserter(intersect, intersect.begin()));
      groupAnswers = intersect;
    }
  }
  return groupAnswers;
}

int main()
{
  std::ifstream infile("input.txt");
  int sumAnswers = 0;
  while (!infile.eof())
  {
    //set<char> answers = getGroupAnswers(infile);
    set<char> answers = getSameGroupAnswers(infile);
    sumAnswers += answers.size();
    cout << "set :\n";

    for (char c : answers)
    {
      cout << c;
    }
    cout << "\n"
         << answers.size() << "\n\n";
  }
  cout << "\n Sum: " << sumAnswers << "\n\n";
}