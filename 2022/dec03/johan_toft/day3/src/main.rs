// One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey.
// Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.
// Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments.
// The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.
// The Elves have made a list of all of the items currently in each rucksack (your puzzle input),
// but they need your help finding the errors.
// Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).
// The list of items for each rucksack is given as characters all on a single line.
// A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment,
// while the second half of the characters represent items in the second compartment.
// For example, suppose you have the following list of contents from six rucksacks

// vJrwpWtwJgWrhcsFMMfFFhFp
// jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
// PmmdzqPrVvPwwTWBwg
// wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
// ttgJtRGJQctTZtZT
// CrZsJsPPZsGzwwsLwLmpwMDw

// The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
// The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
// The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
// The fourth rucksack's compartments only share item type v.
// The fifth rucksack's compartments only share item type t.
// The sixth rucksack's compartments only share item type s.

// To help prioritize item rearrangement, every item type can be converted to a priority:

// Lowercase item types a through z have priorities 1 through 26.
// Uppercase item types A through Z have priorities 27 through 52.

// In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

use std::collections::HashSet;

fn priority(c: char) -> u32 {
    if c.is_ascii_lowercase() {
        c as u32 - 'a' as u32 + 1
    } else {
        c as u32 - 'A' as u32 + 27
    }
}

struct Rucksack {
    first: Vec<char>,
    second: Vec<char>,
}

impl Rucksack {
    fn new(first: Vec<char>, second: Vec<char>) -> Rucksack {
        Rucksack {
            first,
            second,
        }
    }

    fn parse(input: &str) -> Rucksack {
        let mut first = Vec::new();
        let mut second = Vec::new();

        for (i, c) in input.chars().enumerate() {
            if i < input.len() / 2 {
                first.push(c);
            } else {
                second.push(c);
            }
        }

        Rucksack {
            first,
            second,
        }
    }

    // Iterate over all items
    fn items(&self) -> impl Iterator<Item = char> + '_ {
        self.first.iter().copied().chain(self.second.iter().copied())
    }

    fn get_common(&self) -> HashSet<char> {
        let mut common = HashSet::new();
        for c in self.first.iter() {
            if self.second.contains(c) {
                common.insert(*c);
            }
        }
        common
    }

    fn get_common_rucksack(&self, other: &Rucksack) -> HashSet<char> {
        let mut common = HashSet::new();
        for c in self.items() {
            if other.items().any(|c2| c == c2) {
                common.insert(c);
            }
        }
        common
    }
}
const TEST_INPUT: &str = include_str!("testinput.txt");
const INPUT: &str = include_str!("input.txt");

fn main() {
    let mut sum = 0;
    for line in INPUT.lines() {
        let rucksack = Rucksack::parse(line);
        let common = rucksack.get_common();
        println!("Common: {:?}", common);
        for c in common {
            sum += priority(c);
        }
    }
    println!("{}", sum);

    // Part2

    // Split the list of rucksacks in groups of three, and find the common item in the groups.
    // Sum the priorities of the common item.
    let mut sum = 0;
    let mut rucksacks = Vec::new();
    for line in INPUT.lines() {
        rucksacks.push(Rucksack::parse(line));
    }
    // Split into groups of three consecutive rucksacks, increase index by 3 each time
    for i in (2..rucksacks.len()).step_by(3) {
        let common = rucksacks[i-2].get_common_rucksack(&rucksacks[i-1]);
        let common2 = rucksacks[i-1].get_common_rucksack(&rucksacks[i]);
        let all_common = common.intersection(&common2).copied().collect::<Vec<_>>();
        assert_eq!(all_common.len(), 1);
        for c in all_common {
            sum += priority(c);
        }
    }
    println!("{}", sum);
}

// Add some tests
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse() {
        let rucksack = Rucksack::parse("vJrwpWtwJgWrhcsFMMfFFhFp");
        assert_eq!(rucksack.first, vec!['v', 'J', 'r', 'w', 'p', 'W', 't', 'w', 'J', 'g', 'W', 'r']);
        assert_eq!(rucksack.second, vec!['h', 'c', 's', 'F', 'M', 'M', 'f', 'F', 'F', 'h', 'F', 'p']);
    }

    #[test]
    fn test_get_common() {
        let rucksack = Rucksack::new(vec!['v', 'r'], vec!['h', 'r']);
        let common = rucksack.get_common();
        assert_eq!(common, vec!['r'].into_iter().collect::<HashSet<char>>());
    }

    #[test]
    fn test_priority() {
        assert_eq!(priority('a'), 1);
        assert_eq!(priority('z'), 26);
        assert_eq!(priority('A'), 27);
        assert_eq!(priority('Z'), 52);
    }

    #[test]
    fn test_sum() {
        let mut sum = 0;
        for line in TEST_INPUT.lines() {
            let rucksack = Rucksack::parse(line);
            let common = rucksack.get_common();
            for c in common {
                sum += priority(c);
            }
        }
        assert_eq!(sum, 157);
    }
}

