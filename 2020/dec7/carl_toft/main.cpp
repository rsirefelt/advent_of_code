#include <iostream>
#include <fstream>
#include <vector>
#include <string>

// This function reads the .txt file given as input, and returns its lines
// as a vector of strings. The last line is not included if it is empty.
// If the file can not be opened for reading it terminates the program.
std::vector<std::string> readLines(std::string filename) {
    std::vector<std::string> lines; // to be returned
    std::string line;               // will hold each individual line

    // Open file
    std::ifstream file(filename);
    if (file.is_open()) {
        // Read the lines one by one and add to vector "lines"
        while (getline(file, line)) {
            lines.push_back(line);
        }
    }
    else {
        // File failed to open for some reason. Report the error and exit the program.
        std::cout << "FAILED TO OPEN FILE: " << filename << "\nAborting...";
        exit(0);
    }

    // Remove the last line if it is empty (equal to "")
    if (lines.back() == "") {
        lines.pop_back();
    }

    // Done!
    return lines;
}

std::vector<std::string> splitString(std::string line, char delimiter) {
    std::vector<std::string> substrings;

    // First, find all occurences of the delimiter
    std::vector<long int> delimiter_indices;
    delimiter_indices.push_back(-1);
    for (long int i = 0; i < line.length(); i++) {
        if (line.at(i) == delimiter) {
            delimiter_indices.push_back(i);
        }
    }
    delimiter_indices.push_back(line.length());

    // Now that we have found all the delimiters, split the string into
    // appropriate substrings
    unsigned int substring_length = 0;
    for (unsigned int i = 0; i < delimiter_indices.size() - 1; i++) {
        substring_length = delimiter_indices[i+1] - delimiter_indices[i] - 1;
        substrings.push_back(line.substr(delimiter_indices[i]+1, substring_length));
    }

    return substrings;
}

void parseInputLine(std::string line, std::string& parentBag, std::vector<std::string>& childrenBags, std::vector<int>& numChildrenBags) {
    // Clear outputs
    childrenBags.clear();
    numChildrenBags.clear();

    line.erase(line.length()-1); // remove the trailing .
    auto pos = line.find("contain");
    parentBag = line.substr(0, pos-6);
    std::string tmp = line.substr(pos+8);
    auto splits = splitString(tmp, ',');
    for (int i = 0; i < splits.size(); i++) {
        if (splits[i].at(0) == ' ')
            splits[i] = splits[i].substr(1, splits[i].length()-1);
    }
    for (auto split : splits) {
        auto words = splitString(split, ' ');
        if (words[0] == "no")
            continue;
        childrenBags.push_back(words[1] + " " + words[2]);
        numChildrenBags.push_back(std::stoi(words[0]));
    }
    int x = 3;
}

struct Bag {
    std::string name;
    std::vector<Bag*> childrenBags;
    std::vector<int> numChildrenBags;
    std::vector<Bag*> parentBags;
    bool canContainGold, visited, numChildBagsCounted;
    unsigned long long int totalNumChildBags;
};

void upwardTraverse(Bag* bag) {
    if (bag->visited == true)
        return;

    bag->visited = true;
    bag->canContainGold = true;
    for (int i = 0; i < bag->parentBags.size(); i++)
        upwardTraverse(bag->parentBags[i]);
}

unsigned long long int countChildBags(Bag* bag) {
    if (bag->numChildBagsCounted == true)
        return bag->totalNumChildBags;

    for (int i = 0; i < bag->childrenBags.size(); i++) {
        bag->totalNumChildBags = bag->totalNumChildBags + bag->numChildrenBags[i] + bag->numChildrenBags[i]*countChildBags(bag->childrenBags[i]);
    }

    bag->numChildBagsCounted = true;
    return bag->totalNumChildBags;
}

int main() {
    // Read the input
    std::vector<std::string> input = readLines("/home/carl/CLionProjects/AdventOfCode/Day7/input.txt");
    std::string parentBag;
    std::vector<std::string> childrenBags;
    std::vector<int> numChildrenBags;
    std::vector<Bag> bags;

    // Initialize the bags
    for (std::string line : input) {
        parseInputLine(line, parentBag, childrenBags, numChildrenBags);
        Bag bag;
        bag.name = parentBag;
        bag.numChildrenBags = numChildrenBags;
        bag.canContainGold = false;
        bag.visited = false;
        bag.numChildBagsCounted = false;
        bag.totalNumChildBags = 0;
        bags.push_back(bag);
    }

    // Add the parent and children bag information
    for (int i = 0; i < input.size(); i++) {
        std::string line = input[i];
        parseInputLine(line, parentBag, childrenBags, numChildrenBags);

        // Add child and parent bag information
        for (std::string childBag : childrenBags) {
            for (int k = 0; k < bags.size(); k++) {
                if (bags[k].name == childBag) {
                    bags[i].childrenBags.push_back(&bags[k]);
                    bags[k].parentBags.push_back(&bags[i]);
                }
            }
        }
    }

    // Now we have finally loaded all the bag information!
    // Count how many bags the shiny gold bag contains.
    unsigned long long int numberOfBagsInsideShinyGold = 0;
    for (int i = 0; i < bags.size(); i++) {
        if (bags[i].name == "shiny gold") {
            upwardTraverse(&bags[i]);
            bags[i].canContainGold = false;
            numberOfBagsInsideShinyGold = countChildBags(&bags[i]);
        }
    }

    // Count the number of bags that can contain the shiny gold
    unsigned int numBagsCanContainGold = 0;
    for (Bag bag : bags) {
        if (bag.canContainGold == true)
            numBagsCanContainGold++;
    }

    std::cout << "Part 1: " << numBagsCanContainGold << "\nPart 2: " << numberOfBagsInsideShinyGold << "\n";

    return 0;
}
