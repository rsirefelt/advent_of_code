use std::fs;

fn find_num1(account : &Vec<i64>) -> i64
{
    for i in account {
        for j in account {
                if i + j == 2020 {
                    println! {"{} {} {}", i, j, i * j};
                    return i*j;
            }
        }
    }
    return 0;
}

fn find_num2(account : &Vec<i64>) -> i64
{
    for i in account {
        for j in account {
            for k in account {
                if i + j + k == 2020 {
                    println! {"{} {} {} {}", i, j, k, i * j * k};
                    return i*j*k;
                }
            }
        }
    }
    return 0;
}

fn main() {
    let filename = "input_day1.txt";
    let contents = fs::read_to_string(filename)
        .expect("Failed to read input file");


    let mut account :Vec<i64> = Vec::new();
    for element in contents.lines() {
        let num: i64 = element.parse().expect("Failed to parse input line");
        account.push(num);
    }

    find_num1(&account);
    find_num2(&account);
}
