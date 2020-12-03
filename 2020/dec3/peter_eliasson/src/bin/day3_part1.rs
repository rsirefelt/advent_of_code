use day3::*;

fn day3_part1(input: &str) -> i64 {
    let rows: Vec<Row> = input.lines().map(|r| parse_row(r).unwrap()).collect();
    count_trees_for_slope(&rows, 3, 1)
}

fn main() {
    let input = day3::INPUT.trim_end();
    println!("{:?}", day3_part1(input));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_day3_part1_example() {
        let input = "\
        ..##.......\n\
        #...#...#..\n\
        .#....#..#.\n\
        ..#.#...#.#\n\
        .#...##..#.\n\
        ..#.##.....\n\
        .#.#.#....#\n\
        .#........#\n\
        #.##...#...\n\
        #...##....#\n\
        .#..#...#.#\n";
        dbg!(input);
        assert_eq!(day3_part1(input), 7);
    }

    #[test]
    fn test_solve_day3_part1() {
        let input = day3::INPUT.trim_end();
        assert_eq!(day3_part1(input), 274);
    }
}
