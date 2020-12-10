#include <fstream>
#include <deque>
#include <vector>
#include <iostream>
#include <numeric>
#include <algorithm>
#include <map>

using namespace std;

long nbrOfLeaves(deque<int> deque, int start, std::map<int, long> &cache)
{
  if (deque.size() == 0)
  {
    return 1;
  }
  long leaves = 0;
  while (deque.size() > 0 && (deque.front() - start <= 3))
  {
    int value = deque.front();
    deque.pop_front();

    if (cache.find(value) != cache.end())
    {
      leaves += cache[value];
    }
    else
    {
      leaves += nbrOfLeaves(deque, value, cache);
    }
  }
  cache[start] = leaves;
  return leaves;
}

int main()
{
  std::ifstream infile("input1.txt");
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
    }
    currentJolt = jolt;
  }

  cout << "result: " << nbrOf1 * nbrOf3 << "\n";
  std::map<int,long> cache;
  long result = nbrOfLeaves(deque, 0, cache);
  cout << "result2: " << result << "\n";
}