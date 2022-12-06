//
// They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:
//
//     [D]
// [N] [C]
// [Z] [M] [P]
//  1   2   3
//
// move 1 from 2 to 1
// move 3 from 1 to 3
// move 2 from 2 to 1
// move 1 from 1 to 2
//
// In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.
//
// Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:
//
// [D]
// [N] [C]
// [Z] [M] [P]
//  1   2   3

// Import regex
use regex::Regex;


// Create a struct for a stack of crates
struct Stack {
    // The crates are represented as vector of chars
    crates: Vec<char>,
}

struct Warehouse {
    // The warehouse is represented as a vector of stacks
    stacks: Vec<Stack>,
}

impl Stack {
    // Create a new stack from a string of crates
    fn new(crates: &str) -> Stack {
        Stack {
            crates: crates.chars().collect(),
        }
    }
}

struct Move {
    amount: usize,
    from: usize,
    to: usize,
}

impl Move {
    fn parse(input: &str) -> Vec<Move> {
        // move 1 from 2 to 1

        let mut moves = Vec::new();

        // Find the first line that starts with move and then parse them as above
        let mut lines = input.lines();

        // Create regex for parsing the moves
        let re = Regex::new(r"move (\d+) from (\d+) to (\d+)").unwrap();

        for line in lines {
            if line.starts_with("move") {
                // Parse the line
                let caps = re.captures(line).unwrap();
                let amount = caps.get(1).unwrap().as_str().parse::<usize>().unwrap();
                let from = caps.get(2).unwrap().as_str().parse::<usize>().unwrap() - 1;
                let to = caps.get(3).unwrap().as_str().parse::<usize>().unwrap() - 1;
                moves.push(Move { amount, from, to });
            }
        }
        moves
    }
}

impl Warehouse {
    fn do_crane_move(&mut self, m: &Move) {
        // Get the stack to move from
        for i in 0..m.amount {
            let crate_ = self.stacks[m.from].crates.pop().unwrap();
            self.stacks[m.to].crates.push(crate_);
        }
    }

    fn do_crane_move_9001(&mut self, m: &Move) {
        // Get the stack to move from
        let index = self.stacks[m.from].crates.len() - m.amount;
        let mut crates = self.stacks[m.from].crates.split_off(index);
        self.stacks[m.to].crates.append(&mut crates);
    }

    // Implement an index operator for the warehouse
    fn index(&mut self, index: usize) -> &mut Stack {
        &mut self.stacks[index]
    }

    fn parse_input(input: &str) -> Warehouse {
        let mut warehouse = Warehouse {
            stacks: Vec::new(),
        };
        // Find the first empty line, the input is split into two parts.
        // The first part is the stacks of crates, the second part is the moves.
        //     [D]
        // [N] [C]
        // [Z] [M] [P]
        //  1   2   3
        //
        // move 1 from 2 to 1


        // Find the empty line.
        let first_empty_line = input.lines().position(|line| line.is_empty()).unwrap();

        // The first part can be thought of as a 2D array of crates.
        // The length of the line + 1 divided by length of [D] is the number of stacks.

        let num_stacks = (input.lines().nth(first_empty_line - 2).unwrap().len() + 1)  / 4;
        println!("Number of stacks: {}", num_stacks);

        // Create num_stacks stacks
        for _ in 0..num_stacks {
            warehouse.stacks.push(Stack::new(""));
        }

        // Loop through each stack and fill it with crates until the top of input or a space is reached.
        for (stack_index, stack) in warehouse.stacks.iter_mut().enumerate() {
            let vec = input.lines().take(first_empty_line-1).collect::<Vec<&str>>();
            for &line in vec.iter().rev() {
                // Get the crate from the line
                let crate_ = line.chars().nth(stack_index * 4 + 1);
                // If the crate is a space, or no char is found, break
                match crate_ {
                    Some(' ') => break,
                    Some(crate_) => stack.crates.push(crate_),
                    None => break,
                }
            }
        }
        warehouse
    }

    // Implement a print function for the warehouse
    fn print(&self) {
        // Find the longest stack
        let mut longest_stack = 0;
        for stack in &self.stacks {
            if stack.crates.len() > longest_stack {
                longest_stack = stack.crates.len();
            }
        }

        // Print the stacks reversed
        for i in (0..longest_stack).rev() {
            for stack in &self.stacks {
                if stack.crates.len() > i {
                    print!("[{}]", stack.crates[i]);
                } else {
                    print!("[ ]");
                }
            }
            println!();
        }
        for i in 0..self.stacks.len() {
            print!(" {} ", i + 1);
        }
        println!();
    }

    fn clone(&self) -> Warehouse {
        let mut warehouse = Warehouse {
            stacks: Vec::new(),
        };
        for stack in &self.stacks {
            warehouse.stacks.push(Stack::new(&stack.crates.iter().collect::<String>()));
        }
        warehouse
    }
}




fn main() {
    let input = include_str!("input.txt");
    let mut warehouse = Warehouse::parse_input(input);
    let mut warehouse_9001 = warehouse.clone();
    let moves = Move::parse(input);
    warehouse.print();
    // Execute the moves
    for m in moves {
        warehouse.do_crane_move(&m);
        warehouse_9001.do_crane_move_9001(&m);
    }
    // Print the top of the stacks
    println!("Part 1 ");
    for stack in warehouse.stacks.iter() {
        print!("{}", stack.crates.last().unwrap());
    }
    println!();
    println!("Part 2 ");
    for stack in warehouse_9001.stacks.iter() {
        print!("{}", stack.crates.last().unwrap());
    }
}
