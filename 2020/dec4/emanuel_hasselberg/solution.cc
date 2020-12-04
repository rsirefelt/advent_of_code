#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <map>
#include <sstream>
#include <regex>

using namespace std;
using Record = map<string, string>;

Record getNextRecord(std::ifstream &infile)
{
  map<string, string> record;
  string line;
  while (getline(infile, line))
  {
    cout << line << "\n";
    if (line.empty())
      break;

    stringstream ss(line);
    string word;
    while (ss >> word)
    {
      std::smatch sm;
      regex re("([#a-zA-Z0-9]+):([#a-zA-Z0-9]+)");
      regex_match(word, sm, re);

      record[sm[1]] = sm[2];
    }
  }
  return record;
}

bool isValid(Record &record)
{
  //cout << record["byr"] << record["iyr"] << record["eyr"] << "\n";
  bool byrOk = stoi(record["byr"]) >= 1920 && stoi(record["byr"]) <= 2020;
  bool iyrOk = stoi(record["iyr"]) >= 2010 && stoi(record["iyr"]) <= 2020;
  bool eyrOk = stoi(record["eyr"]) >= 2020 && stoi(record["eyr"]) <= 2030;
  std::smatch sm;
  regex re("([0-9]+)(\\w*)");
  regex_match(record["hgt"], sm, re);
  bool hgtOk;
  if (sm[2] == "cm")
  {
    hgtOk = stoi(record["hgt"]) >= 150 && stoi(record["hgt"]) <= 193;
  }
  else
  {
    hgtOk = stoi(record["hgt"]) >= 59 && stoi(record["hgt"]) <= 76;
  }

  re = "?:#(w*)|([a-f{6}])";
  regex_match(record["hcl"], sm, re);
  std::cout << "the " << sm.size() << " matches were: ";
  for (unsigned i = 0; i < sm.size(); ++i)
  {
    std::cout << "[" << sm[i] << "] ";
  }
  return byrOk && iyrOk && eyrOk && hgtOk;
}

int main()
{
  std::ifstream infile("input.txt");
  string line;
  int nbrValid = 0;
  int nbrValid2 = 0;
  while (!infile.eof())
  {
    Record record = getNextRecord(infile);

    cout << "processing!\n";
    cout << "number" << record.size() << "\n";
    if (record.size() >= 8)
    {
      nbrValid++;
      if (isValid(record))
      {
        nbrValid2++;
      }
    }
    else if (record.size() == 7)
    {
      if (record.find("cid") == record.end())
      {
        nbrValid++;
        if (isValid(record))
        {
          nbrValid2++;
        }
      }
    }
  }
  cout << "Nbr Valid: " << nbrValid;
  cout << "Nbr Valid2: " << nbrValid;
}