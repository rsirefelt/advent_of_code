#include <fstream>
#include <deque>
#include <vector>
#include <iostream>
#include <numeric>
#include <algorithm>

using namespace std;

int nbrOfLeaves(deque<int> deque, int start)
{
  for (int a : deque)
  {
    cout << a << " ";
  }
  cout << "\n";
  cout << "deque size " << deque.size() << "Start: " << start << "\n";

  if (deque.size() == 1)
  {
    cout << "returning one\n";
    return 1;
  }
  int leaves = 0;
  while (deque.size() > 1 && (start - deque.front() <= 3))
  {
    int value = deque.front();
    cout << value << "\n";
    deque.pop_front();
    leaves += nbrOfLeaves(deque, value);
  }
  cout << "leaves:" << leaves << "\n";

  return leaves;
}

int main()
{
  std::ifstream infile("tiny.txt");
  int a;
  deque<int> deque;

  while (infile >> a)
  {
    deque.push_back(a);
  }
  sort(deque.begin(), deque.end());
  int nbrOf1 = 0;
  int nbrOf3 = 1;
  int currentJolt = 0;
  for (int jolt : deque)
  {
    cout << "Current:" << currentJolt << " Next:" << jolt << "\n";
    switch (jolt - currentJolt)
    {
    case 1:
      nbrOf1++;
      break;
    case 3:
      nbrOf3++;
      break;

    default:
      break;
    }
    currentJolt = jolt;
  }

  cout << "result: " << nbrOf1 * nbrOf3 << "\n";

  int result = nbrOfLeaves(deque, 0);
  cout << "result2: " << result << "\n";
}