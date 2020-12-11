#include <fstream>
#include <vector>
#include <iostream>

using namespace std;

enum Place
{
  empty,
  used,
  floor
};

std::ostream &operator<<(std::ostream &out, const Place value)
{
  switch (value)
  {
  case Place::empty:
    return out << 'L';
    break;

  case Place::used:
    return out << '#';
    break;

  case Place::floor:
    return out << '.';
    break;
  }
  return out << "x";
}

class ChairMap
{
public:
  vector<vector<Place>> m_theMap;
  ChairMap(ifstream &ifs)
  {
    string line;
    int row = 0;
    while (ifs >> line)
    {
      m_theMap.push_back(vector<Place>());
      for (char a : line)
      {
        switch (a)
        {
        case 'L':
          m_theMap[row].push_back(Place::empty);
          break;

        case '.':
          m_theMap[row].push_back(Place::floor);
          break;
        }
      }
      row++;
    }
  }

  void print()
  {
    for (auto row : m_theMap)
    {
      for (auto tPlace : row)
      {
        cout << tPlace;
      }
      cout << "\n";
    }
    cout << "\n";
  }

  bool isEmpty(int i, int j)
  {
    return m_theMap[i][j] == Place::empty;
  }

  bool noOccupiedNeighbours(int i, int j)
  {
    
  }

  bool propagate()
  {
    vector<vector<Place>> newMap;
    bool change = false;
    for (size_t i = 0; i < m_theMap.size(); i++)
    {
      newMap.push_back(vector<Place>());

      for (size_t j = 0; i < m_theMap[i].size(); i++)
      {
        if (isEmpty(i,j) && noOccupiedNeighbours(i,j))
        {
          change =true;
          newMap[i].push_back(Place::used);
        }
      }
    }
    return change;
  }
};

int main()
{
  ifstream ifs("input.txt");
  ChairMap cm(ifs);
  cm.print();
  while (cm.propagate())
  {
    cm.print();
  }
}