// Directly include the input.txt file in the built binary

const INPUT: &str = include_str!("input.txt");

fn main() {
    // Parse the input as multiple lists of integer, each list is separated by a blank line
    let mut input: Vec<Vec<i64>> = INPUT.split("\n\n").map(|group| {
        group.lines().map(|line| {
            line.parse().unwrap()
        }).collect()
    }).collect();

    // Part 1: Find the group with the largest sum

    let part1 = input.iter().map(|group| {
        group.iter().sum::<i64>()
    }).max().unwrap();


    println!("Part 1: {}", part1);

    // Part 2: Find the sum of the top three groups
    let part2 : Vec<i64> = input.iter().map(|group| {
        group.iter().sum::<i64>()
    }).collect::<Vec<i64>>();

    // Sort the vector in descending order
    let mut part2 = part2;
    part2.sort_by(|a, b| b.cmp(a));

    println!("Part 2: {:?}", part2.iter().take(3).sum::<i64>());
}
