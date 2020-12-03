use day3::*;

fn day3_part2(input: &str) -> i64 {
    let rows: Vec<Row> = input.lines().map(|r| parse_row(r).unwrap()).collect();
    let slopes = vec![(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)];
    slopes
        .iter()
        .map(|&(slope_right, slope_down)| count_trees_for_slope(&rows, slope_right, slope_down))
        .product()
}

fn main() {
    let input = day3::INPUT.trim_end();
    println!("{:?}", day3_part2(input));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_day3_part2_example() {
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
        assert_eq!(day3_part2(input), 336);
    }

    #[test]
    fn test_solve_day3_part2() {
        let input = day3::INPUT.trim_end();
        assert_eq!(day3_part2(input), 6050183040);
    }
}
