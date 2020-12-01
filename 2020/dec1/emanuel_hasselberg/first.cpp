#include <iostream>
#include <fstream>

#include <set>

int main()
{
  std::ifstream infile("input.txt");
  int a;
  std::set<int> numbersSet;
  while (infile >> a)
  {
    numbersSet.insert(a);
  }
  for (int number : numbersSet )
  {
    int neededNumber = 2020 - number;
    if(auto b = numbersSet.find(neededNumber); b != numbersSet.end())
    {
      std::cout << number << "*" << (*b) << "=" << number*(*b) << "\n";
      break;
    }
  }
}