#include <fstream>
#include <iostream>
#include <bitset>
#include <vector>
using namespace std;

int main()
{
  ifstream infile("input.txt");
  string boardingPass;
  int maxSeatID = 0;
  vector<bool> places(1<<10,false);
  cout << places.size();
  while (infile >> boardingPass)
  {
    bitset<7> rowCode;
    for (size_t i = 0; i < 7; i++)
    {
      rowCode.set(6-i, boardingPass[i] == 'B');
    }
    bitset<3> seatCode;
    for (size_t i = 0; i < 3; i++)
    {
     
      seatCode.set(2 - i, boardingPass[i+7] == 'R');
    }
    int seatID = rowCode.to_ulong() * 8 + seatCode.to_ulong();
    places[seatID] = true;
    if (seatID > maxSeatID)
      maxSeatID = seatID;
  }

  cout << "Max seat ID = " << maxSeatID << "\n";
  bool firstSeated = false;
  for(size_t i = 0; i < places.size(); i++)
  {
    if (firstSeated && !places[i])
    {
      cout <<"Your seat: " <<  i << "\n";
      break;
    }
    if(places[i])
    {
      firstSeated = true;
    }
  }
}