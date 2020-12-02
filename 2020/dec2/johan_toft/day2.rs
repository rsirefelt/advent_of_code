use std::fs;
use regex::Regex;

fn count_occurences(str : &str, target : char) -> i32 {
    let mut n = 0;
    for ch in str.chars() {
        if ch == target{
            n += 1;
        }
    }
    return n;
}

fn valid_pass(lower : i32, upper : i32, count : i32) -> bool
{
    return (lower <= count) && (count <= upper);
}

fn valid_pass2(lower : i32, upper : i32, pass_char : char, pass : &str) -> bool
{
    let i1 : usize = lower as usize -1;
    let i2 : usize = upper as usize -1;
    let c1 = pass.as_bytes()[i1] as char;
    let c2 = pass.as_bytes()[i2] as char;

    let match1 = c1 == pass_char;
    let match2 = c2 == pass_char;

    return match1 != match2;
}

fn main() {
    let filename = "input_day2.txt";
    let contents = fs::read_to_string(filename)
        .expect("Failed to read input file");

    let re = Regex::new(r"(\d+)-(\d+) (\w): (\w+)").expect("failed to compile regex");


    let mut valid_passwords = 0;
    let mut valid_passwords_part2 = 0;

    for line in contents.lines(){
        let cap = re.captures(line).unwrap();

        let lower_limit : i32 = cap[1].parse().expect("Failed to parse");
        let upper_limit : i32 = cap[2].parse().expect("Failed to parse");
        let c = cap[3].chars().nth(0).unwrap();

        let count = count_occurences(&cap[4], c);

        if valid_pass(lower_limit, upper_limit, count) {
            valid_passwords += 1;
        }

        if valid_pass2(lower_limit, upper_limit, c, &cap[4]) {
            valid_passwords_part2 += 1;
        }

        //println!("{}", count);

    }
    println!{"{}", valid_passwords}
    println!{"{}", valid_passwords_part2}

}