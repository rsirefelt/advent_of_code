pub const INPUT: &str = include_str!("../input.txt");

#[derive(Debug, PartialEq, Copy, Clone)]
pub enum Cell {
    OpenSquare,
    Tree,
}

#[derive(Debug, PartialEq)]
pub struct Row {
    pub cells: Vec<Cell>,
}

pub fn parse_row(row: &str) -> Option<Row> {
    let cells: Vec<Cell> = row
        .chars()
        .map(|c| match c {
            '.' => Some(Cell::OpenSquare),
            '#' => Some(Cell::Tree),
            _ => None,
        })
        .collect::<Option<_>>()?;
    Some(Row { cells })
}

pub fn count_trees_for_slope(rows: &[Row], slope_right: usize, slope_down: usize) -> i64 {
    let mut pos_x = 0;
    let mut pos_y = 0;
    let mut num_trees = 0;
    while pos_y < rows.len() {
        let row = &rows[pos_y];
        let cell = row.cells[pos_x % row.cells.len()];
        if cell == Cell::Tree {
            num_trees += 1;
        }
        pos_y += slope_down;
        pos_x += slope_right;
    }
    num_trees
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_row() {
        use Cell::OpenSquare as O;
        use Cell::Tree as T;

        let input = "..##.......";
        assert_eq!(
            parse_row(input),
            Some(Row {
                cells: vec![O, O, T, T, O, O, O, O, O, O, O]
            })
        );

        let input = "Not a valid row";
        assert_eq!(parse_row(input), None);
    }
}
