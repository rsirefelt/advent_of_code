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
  for (int number : numbersSet)
  {
    for (int number2 : numbersSet)
    {
      if (number + number2 > 2020)
        continue;
      int neededNumber = 2020 - (number + number2);
      if (auto b = numbersSet.find(neededNumber); b != numbersSet.end())
      {
        std::cout << number << "*" << number2 << "*" << (*b) << "=" << number * number2 * (*b) << "\n";
        return 0;
      }
    }
  }
}