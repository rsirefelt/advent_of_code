use std::collections::HashMap;
use regex::Regex;
use lazy_static::lazy_static;

type Entry = HashMap<String, String>;


fn validate_limits<T: std::cmp::PartialOrd>(lower: &T, upper: &T, val: &T) -> bool
{
    (lower <= val) && (val <= upper)
}

lazy_static! {
    static ref RE_HCL: Regex = Regex::new(r"^#[\da-f]{6}$").unwrap();
    static ref RE_PID: Regex = Regex::new(r"^\d{9}$").unwrap();
}
fn validate_hcl(hcl: &String) -> bool {
    RE_HCL.is_match(hcl)
}

fn validate_ecl(ecl: &String) -> bool {
    let valid_colors = vec!["amb", "blu", "brn", "gry", "grn", "hzl", "oth"];
    return valid_colors.contains(&ecl.as_str());
}

fn validate_pid(pid: &String) -> bool {
    RE_PID.is_match(pid)
}

fn validate_entry(key: &String, value: &String) -> bool
{
    match key.as_str() {
        "byr" => {
            let val: i64 = value.parse().unwrap();
            validate_limits(&1920, &2002, &val)
        }
        "iyr" => {
            let val: i64 = value.parse().unwrap();
            validate_limits(&2010, &2020, &val)
        }
        "eyr" => {
            let val: i64 = value.parse().unwrap();
            validate_limits(&2020, &2030, &val)
        }
        "hgt" => {
            let unit = &value[(value.len() - 2)..]; //value.chars().into_iter().rev().take(2).collect::<String>();
            let val_str = &value[..(value.len() - 2)];//:String = value.chars().into_iter().take(value.len()-2).collect::<String>();
            let val: i32 = val_str.parse().unwrap();
            match unit {
                "cm" => { validate_limits(&150, &193, &val) }
                "in" => { validate_limits(&59, &76, &val) }
                _ => { false }
            }
        }
        "hcl" => { validate_hcl(&value) }
        "ecl" => { validate_ecl(&value) }
        "pid" => { validate_pid(&value) }
        "cid" => { true }
        &_ => { true }
    }
}


fn is_valid(entry: &Entry) -> bool
{
    let req_fields = vec!["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];

    for req in req_fields {
        if entry.contains_key(req) {
            if validate_entry(&req.to_string(), &entry.get(req).unwrap()) {} else { return false; }
        } else {
            return false;
        }
    }
    return true;
}

fn main() {
    let req_fields = vec!["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"];

    let data = include_str!("input.txt");

    let test: Vec<&str> = data.split("\n\n").collect();

    let mut valid_count = 0;

    for entry_raw in test {
        let mut entry: Entry = HashMap::new();
        //println!("NEW ENTRY");
        let subs: Vec<&str> = entry_raw.split(|x| x == ' ' || x == '\n').collect();
        for sub in subs {
            let res: Vec<&str> = sub.split(":").collect();
            entry.insert(res[0].to_string(), res[1].to_string());
        }
        if is_valid(&entry) {
            valid_count += 1;
            //println!("VALID {}", entry_raw)
        } else {//println!("INVALID {}", entry_raw)
        }
    }

    println!("NUM_VALID {}", valid_count);
}
