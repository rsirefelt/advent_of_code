use std::fs;

fn get_data(data :&Vec<&str>, x : i32, y : i32) -> char
{
    let size_x = data[0].chars().count() as i32;
    let x_index = (x%size_x) as usize;
    return data[y as usize].chars().nth(x_index).unwrap();
}

fn calc_hit_trees(data :&Vec<&str>, stride_x : i32, stride_y : i32) -> i64
{
    let size_y = data.len() as i32;

    let mut y = 0;
    let mut x = 0;

    let mut hits = 0;

    while y+stride_y < size_y {
        x+= stride_x;
        y+= stride_y;

        if get_data(data, x, y) == '#' {
            hits += 1
        }
    }
    return hits;
}


fn main()
{
    let filename = "input_day3.txt";
    let contents = fs::read_to_string(filename)
        .expect("Failed to read input file");
    let mut grid:Vec<&str> = Vec::new();
    for line in contents.lines(){
        grid.push(line.clone());
    }

    let size_y = grid.len();

    let mut hit_trees = 0;

    let a = calc_hit_trees(&grid, 1, 1);
    let b =calc_hit_trees(&grid, 3, 1);
    let c = calc_hit_trees(&grid, 5, 1);
    let d = calc_hit_trees(&grid, 7, 1);
    let e =calc_hit_trees(&grid, 1, 2);

    println!("{}, {}, {}, {}, {}, {}",a,b,c,d,e, a*b*c*d*e);
}