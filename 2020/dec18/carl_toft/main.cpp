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

/*unsigned long long int evaluateExpression2(std::string expression) {
    // An expression must start with a number or a '('
    if (expression.at(0) == '(') {
        // DEAL WITH THIS
    } else {
        // The expression starts with a number
        unsigned int index = expression.find(" ");

        // THERE IS A BASE CASE TO BE DEALT WITH HERE

        unsigned long long int nextVal = std::stoi(expression.substr(0, index));
        std::string remainingExpression = expression.substr(index+1, expression.length() - (index+1));

        // Start the recursion
        if (expression.at(index+1) == '+') {
            return nextVal + evaluateExpression(remainingExpression);
        } else if (expression.at(index+1) == '*') {
            return nextVal * evaluateExpression(remainingExpression);
        }
    }
}*/

long long int toInt(std::string num) {
    unsigned long int multiplier = 1;
    long long int number = 0;
    for (int idx = num.length()-1; idx >= 0; idx--) {
        number = number + multiplier*(int(num.at(idx))-48);
        multiplier *= 10;
    }
    return number;
}

unsigned long long int evaluateExpressionWithoutParentheses(std::string expression) {
    unsigned int END = std::string::npos;

    // Evaluate the first two numbers
    unsigned int index1 = expression.find(" ");

    // Address base case (the string is just a number)
    if (index1 == END)
        return toInt(expression);

    unsigned long long int number1 = toInt(expression.substr(0, index1));
    std::string substring = expression.substr(index1+3, expression.length() - (index1+3));

    // DEAL WITH THE POSSIBILITY OF PARENTHESES HERE
    unsigned int index2 = substring.find(" ");
    unsigned long long int number2;
    if (index2 == END)
        number2 = toInt(substring);
    else
        number2 = toInt(substring.substr(0, index2));

    unsigned long long int new_number;
    if (expression.at(index1+1) == '+') {
        new_number = number1 + number2;
    } else if (expression.at(index1+1) == '*') {
        new_number = number1*number2;
    }

    if (index2 == END) {
        return new_number;
    } else {
        std::string new_expression = std::to_string(new_number) + substring.substr(index2, substring.length() - index2);
        return evaluateExpressionWithoutParentheses(new_expression);
    }
}

std::string carryOutAdditions(std::string expression) {
    bool done = false;
    while (!done) {
        done = true;
        for (int i = 0; i < expression.length(); i++) {
            if (expression.at(i) == '+') {
                // Find left number
                int idx_left, idx_right;
                for (idx_left = i-2; idx_left >= 0; idx_left--) {
                    if (expression.at(idx_left) == ' ')
                        break;
                }
                for (idx_right = i+2; idx_right < expression.length(); idx_right++) {
                    if (expression.at(idx_right) == ' ')
                        break;
                }
                std::string inner = expression.substr(idx_left + 1, idx_right - idx_left - 1);
                unsigned long long int new_number = evaluateExpressionWithoutParentheses(inner);

                std::string left_part, middle_part, right_part;
                if (idx_left == -1)
                    left_part = "";
                else
                    left_part = expression.substr(0, idx_left + 1);
                middle_part = std::to_string(new_number);
                right_part = expression.substr(idx_right, expression.length()-(idx_right));
                expression = left_part + middle_part + right_part;
                done = false;
                break;
            }
        }
    }

    // When we get here, all parentheses should have been removed
    return expression;
}

unsigned long long int evaluateExpressionWithoutParentheses2(std::string expression) {
    expression = carryOutAdditions(expression);
    return evaluateExpressionWithoutParentheses(expression);
}

unsigned long long int evaluateExpression(std::string expression) {
    unsigned int lastOpeningParenthesis = 0;
    bool done = false;
    while (!done) {
        done = true;
        for (int i = 0; i < expression.length(); i++) {
            if (expression.at(i) == '(')
                lastOpeningParenthesis = i;
            if (expression.at(i) == ')') {
                std::string inner = expression.substr(lastOpeningParenthesis + 1, (i - lastOpeningParenthesis - 1));
                unsigned long long int new_number = evaluateExpressionWithoutParentheses2(inner);
                expression = expression.substr(0, lastOpeningParenthesis) + std::to_string(new_number) + expression.substr(i+1, expression.length()-(i+1));
                done = false;
                break;
            }
        }
    }

    // When we get here, all parentheses should have been removed
    return evaluateExpressionWithoutParentheses2(expression);
}

int main() {
    std::vector<std::string> input = readLines("/home/carl/CLionProjects/AdventOfCode/Day18/input.txt");

    unsigned long long int sum = 0, value;
    for (int i = 0; i < input.size(); i++) {
        value = evaluateExpression(input[i]);
        sum += value;
    }

    std::cout << "Part 2: " << sum << "\n";

    return 0;
}

