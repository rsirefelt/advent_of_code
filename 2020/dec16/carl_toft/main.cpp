#include <iostream>
#include <fstream>
#include <vector>
#include <string>

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

struct Range {
    unsigned long long int lower, upper;

    bool isNumberValid(unsigned long long int number) const {
        return (lower <= number && number <= upper);
    }
};

struct Field {
    std::string field_name;
    std::vector<Range> ranges;

    bool isNumberValid(unsigned long long int number) const {
        for (Range range : ranges) {
            if (range.isNumberValid(number))
                return true;
        }
        return false;
    }
};

typedef std::vector<unsigned long long int> Ticket;

Ticket parseTicket(std::string ticket_string) {
    auto parts = splitString(ticket_string, ',');
    Ticket ticket;
    for (auto num : parts)
        ticket.push_back(std::stoi(num));

    return ticket;
}

void parseInput(const std::vector<std::string>& input, std::vector<Field>& fields, Ticket& our_ticket, std::vector<Ticket>& nearby_tickets) {
    // Clear the inputs just in case
    fields.clear();
    our_ticket.clear();
    nearby_tickets.clear();

    // First, parse the fields
    unsigned long int i = 0;
    while (input[i] != "") {
        Field field;
        Range range;

        auto parts = splitString(input[i], ':');
        field.field_name = parts[0];
        parts = splitString(parts[1].substr(1, parts[1].length()-1), ' ');

        // Add first range
        auto range_parts = splitString(parts[0], '-');
        range.lower = std::stoi(range_parts[0]);
        range.upper = std::stoi(range_parts[1]);
        field.ranges.push_back(range);

        // Add second range
        range_parts = splitString(parts[2], '-');
        range.lower = std::stoi(range_parts[0]);
        range.upper = std::stoi(range_parts[1]);
        field.ranges.push_back(range);

        fields.push_back(field);

        i++;
    }
    i += 2; // Skip until we reach our ticket
    our_ticket = parseTicket(input[i]);

    i += 3; // Skip until we reach the first nearby ticket
    for (; i < input.size(); i++) {
        nearby_tickets.push_back(parseTicket(input[i]));
    }
}

std::vector<bool> findPossibleField(unsigned int field_number, const std::vector<Ticket>& tickets, const std::vector<Field>& fields) {
    std::vector<bool> possible_fields;
    for (int i = 0; i < fields.size(); i++)
        possible_fields.push_back(true);

    for (Ticket ticket : tickets) {
        for (unsigned  int i = 0; i < fields.size(); i++) {
            if (fields[i].isNumberValid(ticket[field_number]) == false)
                possible_fields[i] = false;
        }
    }

    return possible_fields;
}

struct TicketField {
    std::vector<bool> possibleFields;
    long int actual_field;

    TicketField() {actual_field = -1; }
};

std::vector<unsigned int> getPossibleFields(TicketField ticketField) {
    std::vector<unsigned int> possible_fields;
    for (int i = 0; i < ticketField.possibleFields.size(); i++) {
        if (ticketField.possibleFields[i] == true)
            possible_fields.push_back(i);
    }

    return possible_fields;
}

int main() {
    // Read the puzzle input
    std::vector<std::string> input = readLines("/home/carl/CLionProjects/AdventOfCode/Day16/input.txt");

    // Define the problem data
    std::vector<Field> fields;
    Ticket our_ticket;
    std::vector<Ticket> nearby_tickets;
    std::vector<Ticket> nearby_valid_tickets;

    // Parse the puzzle input
    parseInput(input, fields, our_ticket, nearby_tickets);

    // Find the valid tickets, and compute the ticket scanning error rate
    unsigned long long int ticket_scanning_error_rate = 0;
    for (Ticket ticket : nearby_tickets) {
        bool isTicketValid = true;
        for (auto number : ticket) {
            bool is_valid = false;
            for (auto field : fields) {
                if (field.isNumberValid(number)) {
                    is_valid = true;
                }
            }
            if (is_valid == false) {
                isTicketValid = false;
                std::cout << number << "\n";
                ticket_scanning_error_rate += number;
            }
        }

        if (isTicketValid)
            nearby_valid_tickets.push_back(ticket);
    }
    nearby_valid_tickets.push_back(our_ticket);

    std::cout << "Part 1: " << ticket_scanning_error_rate << "\n";

    // For each field on the ticket, find which fields it could correspond to
    std::vector<TicketField> ticket_fields;
    for (int i = 0; i < nearby_valid_tickets[0].size(); i++) {
        TicketField ticketField;
        auto currPossibleFields = findPossibleField(i, nearby_valid_tickets, fields);
        ticketField.possibleFields = currPossibleFields;
        ticket_fields.push_back(ticketField);
    }

    bool found_a_unique_field = true;
    while (found_a_unique_field == true) {
        found_a_unique_field = false;
        // Find the ticket fields that only have one possible field assignment
        for (int i = 0; i < ticket_fields.size(); i++) {
            if (ticket_fields[i].actual_field != -1)
                continue; // this field is done, move on to next one
            auto possibleFields = getPossibleFields(ticket_fields[i]);
            if (possibleFields.size() == 1) {
                // Only one field possible!
                //std::cout << "One field possible!\n" << i << "\n";
                ticket_fields[i].actual_field = possibleFields[0]; // we found the field!
                found_a_unique_field = true;

                // Set this field as not possible for all other tickets
                for (int j = 0; j < ticket_fields.size(); j++) {
                    if (i == j)
                        continue;
                    ticket_fields[j].possibleFields[possibleFields[0]] = false;
                }
            }
        }
    }

    unsigned long long int prod = 1;
    for (unsigned int i = 0; i < ticket_fields.size(); i++) {
        if (ticket_fields[i].actual_field < 6) {
            prod *= our_ticket[i];
        }
    }

    std::cout << "Part 2: " << prod << "\n";

    return 0;
}
