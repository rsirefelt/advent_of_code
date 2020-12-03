#include <fstream>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef vector<vector<bool>> TreeMap;

vector<bool> parseRow(string line)
{
  vector<bool> output;
  for (char c : line)
  {
    output.push_back(c == '#');
  }
  return output;
}

long runSlope(int right, int down, const TreeMap &treeMap)
{
  int xPos = 0;
  int yPos = 0;
  int nbrOfTrees = 0;
  while (yPos < treeMap.size())
  {
    const vector<bool> &line = treeMap[yPos];
    //cout << xPos << "%" << line.size() << "=" << xPos % line.size() << "\n";
    if (line[xPos % line.size()])
    {
      nbrOfTrees++;
    }
    xPos += right;
    yPos += down;
  }
  return nbrOfTrees;
}

int main()
{
  ifstream infile("input.txt");
  TreeMap treeMap;
  std::string line;
  while (getline(infile, line))
  {
    treeMap.push_back(parseRow(line));
  }
  int firstResult = runSlope(3, 1, treeMap);
  cout << "first nbrOfTrees: " << firstResult << "\n";

  long secondResult = runSlope(1, 1, treeMap) * runSlope(3, 1, treeMap) * runSlope(5, 1, treeMap) * runSlope(7, 1, treeMap) * runSlope(1, 2, treeMap);
  cout << "second prob?!?: " << secondResult << "\n";
}