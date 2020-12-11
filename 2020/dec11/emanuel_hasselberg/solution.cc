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
    size_t max_col = m_theMap[i].size();
    size_t max_row = m_theMap.size();
    for (size_t i_2 = -1; i_2 <= 1; i_2++)
    {
      for (size_t j_2 = -1; j_2 <= 1; j_2++)
      {
        if (m_theMap[max((size_t)0, min(i + i_2, max_row))][max((size_t)0, min(j + j_2, max_row))] == Place::used)
        {
          return false;
        }
      }
    }
    return true;
  }

  int nbrOfNeighbours(int i, int j)
  {
    int max_col = m_theMap[i].size();
    int max_row = m_theMap.size();
    int nbrOfUsed = 0;
    for (int i_2 = -1; i_2 <= 1; i_2++)
    {
      for (int j_2 = -1; j_2 <= 1; j_2++)
      {
        if ((i_2 == 0 && j_2 == 0) || i + i_2 < 0 || i + i_2 > max_row - 1 ||
            j + j_2 < 0 || j + j_2 > max_col - 1)
        {
          continue;
        }
        if (m_theMap[i + i_2][j + j_2] == Place::used)
        {
          nbrOfUsed++;
        }
      }
    }
    return nbrOfUsed;
  }

  int nbrOfNeighboursFar(int i, int j)
  {
    int max_col = m_theMap[i].size();
    int max_row = m_theMap.size();
    int nbrOfUsed = 0;
    vector<pair<int, int>> directions = {{1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}, {0, -1}, {1, -1}};
    for (auto dir : directions)
    {
      int len = 1;

      while (true)
      {
        int dx = dir.first * len;
        int dy = dir.second * len;

        if (i + dx < 0 || i + dx > max_row - 1 ||
            j + dy < 0 || j + dy > max_col - 1)
        {
          break;
        }
        if (m_theMap[i + dx][j + dy] == Place::used)
        {
          nbrOfUsed++;
          break;
        }
        if (m_theMap[i + dx][j + dy] == Place::empty)
        {
          break;
        }
        len++;
      }
    }
    return nbrOfUsed;
  }

  bool propagate()
  {
    vector<vector<Place>> newMap;
    bool change = false;
    for (size_t i = 0; i < m_theMap.size(); i++)
    {
      newMap.push_back(vector<Place>());

      for (size_t j = 0; j < m_theMap[i].size(); j++)
      {
        // if (isEmpty(i, j) && nbrOfNeighbours(i, j) == 0)
        if (isEmpty(i, j) && nbrOfNeighboursFar(i, j) == 0)
        {
          change = true;
          newMap[i].push_back(Place::used);
        }
        // else if (m_theMap[i][j] == Place::used && nbrOfNeighbours(i, j) >= 4)
        else if (m_theMap[i][j] == Place::used && nbrOfNeighboursFar(i, j) >= 5)
        {
          change = true;
          newMap[i].push_back(Place::empty);
        }
        else
        {
          newMap[i].push_back(m_theMap[i][j]);
        }
      }
    }
    m_theMap = newMap;
    return change;
  }

  int seatsOccupied()
  {
    int nbrOfSeats = 0;
    for (auto row : m_theMap)
    {
      for (auto tPlace : row)
      {
        if (tPlace == Place::used)
          nbrOfSeats++;
      }
    }
    return nbrOfSeats;
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
  cout << "Seats occupied: " << cm.seatsOccupied();
}