//For example, consider the following list of section assignment pairs:
//
// 2-4,6-8
// 2-3,4-5
// 5-7,7-9
// 2-8,3-7
// 6-6,4-6
// 2-6,4-8
//
// For the first few pairs, this list means:
//
//     Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
//     The Elves in the second pair were each assigned two sections.
//     The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.

struct Section {
    start: u32,
    end: u32,
}
struct AssignmentPair {
    first: Section,
    second: Section,
}

impl AssignmentPair {
    fn new(first: Section, second: Section) -> AssignmentPair {
        AssignmentPair {
            first,
            second,
        }
    }

    fn parse(input: &str) -> AssignmentPair {

        // Split the input into two parts, separated by a comma.
        let mut parts = input.split(',');

        // Parse the first part.
        let first = parts.next().unwrap();
        let mut first_parts = first.split('-');
        let first_start = first_parts.next().unwrap().parse::<u32>().unwrap();
        let first_end = first_parts.next().unwrap().parse::<u32>().unwrap();
        let first_section = Section {
            start: first_start,
            end: first_end,
        };

        // Parse the second part.
        let second = parts.next().unwrap();
        let mut second_parts = second.split('-');
        let second_start = second_parts.next().unwrap().parse::<u32>().unwrap();
        let second_end = second_parts.next().unwrap().parse::<u32>().unwrap();
        let second_section = Section {
            start: second_start,
            end: second_end,
        };

        AssignmentPair::new(first_section, second_section)
    }

    fn check_if_fully_overlaps(&self) -> bool {
        // Check whether the first section is fully contained in the other.
        return if self.first.start >= self.second.start && self.first.end <= self.second.end {
            true
        } else if self.second.start >= self.first.start && self.second.end <= self.first.end {
            true
        } else {
            false
        }
    }

    fn check_for_any_overlap(&self) -> bool {
        // Check whether the sections overlap at all.
        return if self.first.start <= self.second.end && self.first.end >= self.second.start {
            true
        } else if self.second.start <= self.first.end && self.second.end >= self.first.start {
            true
        } else {
            false
        }
    }
}

fn main() {
    const INPUT: &str = include_str!("input.txt");

    // Check the input for fully overlapping sections.
    let mut fully_overlapping = 0;
    let mut any_overlapping = 0;
    for line in INPUT.lines() {
        let pair = AssignmentPair::parse(line);
        if pair.check_if_fully_overlaps() {
            fully_overlapping += 1;
        }
        if pair.check_for_any_overlap() {
            any_overlapping += 1;
        }
    }
    println!("Fully overlapping: {}", fully_overlapping);
    println!("Any overlapping: {}", any_overlapping);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse() {
        let pair = AssignmentPair::parse("2-4,6-8");
        assert_eq!(pair.first.start, 2);
        assert_eq!(pair.first.end, 4);
        assert_eq!(pair.second.start, 6);
        assert_eq!(pair.second.end, 8);
    }

    #[test]
    fn test_check_if_fully_overlaps() {
        let pair1 = AssignmentPair::parse("2-4,6-8");
        let pair2 = AssignmentPair::parse("2-6,4-5");
        assert_eq!(pair1.check_if_fully_overlaps(), false);
        assert_eq!(pair2.check_if_fully_overlaps(), true);
    }

    #[test]
    fn test_check_for_any_overlap() {
        let pair1 = AssignmentPair::parse("2-4,6-8");
        let pair2 = AssignmentPair::parse("2-5,5-6");
        assert_eq!(pair1.check_for_any_overlap(), false);
        assert_eq!(pair2.check_for_any_overlap(), true);
    }
}
