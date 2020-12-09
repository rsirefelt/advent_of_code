#include <fstream>
#include <deque>
#include <iostream>

using namespace std;
int main()
{
  std::ifstream infile("input.txt");
  int a;
  deque<int> deque;

  for (int i = 0; i < 25; i++)
  {
    infile >> a;
    deque.push_back(a);
  }

  while (true)
  {
    infile >> a;
    bool approved = false;
    for (int i = 0; i < 25; i++)
    {
      for (int j = 0; j < 25; j++)
      {
        if (i==j)
        {
          continue;
        }
        if(deque[i] + deque[j] == a)
        {
          approved = true;
          break;
        }
      }
      if(approved)
      break;
    }
    if(!approved)
    {
      cout << "Value: " << a;
      break;
    }
    deque.push_back(a);
    deque.pop_front();
  }
}