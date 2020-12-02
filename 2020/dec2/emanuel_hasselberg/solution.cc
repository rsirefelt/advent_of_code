#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

void parseLine(string inLine, int &low, int &high, char &token, string &password)
{
  low = stoi(inLine.substr(0, inLine.find("-")));
  high = stoi(inLine.substr(inLine.find("-") + 1, inLine.find(" ")));
  token = inLine.substr(inLine.find(" ") + 1, inLine.find(":")).c_str()[0];
  password = inLine.substr(inLine.find(":") + 2, string::npos);
}

int main()
{
  std::ifstream infile("input.txt");
  std::string line;
  int nbrOfTrueFirst = 0;
  int nbrOfTrueSecond= 0;
  while (getline(infile, line))
  {
    int low, high;
    char token;
    string password;
    parseLine(line, low, high, token, password);

    size_t occurences = count(password.begin(), password.end(), token);
    if (low <= occurences && occurences <= high)
    {
      nbrOfTrueFirst++;
    }
 
    if((password.at(low-1) == token) != (password.at(high-1) == token))
    {
      nbrOfTrueSecond++;
    }
  }
  cout << "Number of true passwords first = " << nbrOfTrueFirst << "\n";
  cout << "Number of true passwords second = " << nbrOfTrueSecond << "\n";
}