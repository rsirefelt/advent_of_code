use logos::{Logos, Lexer};

use crate::Token::{Left, Right, Front, Back};
use std::collections::HashSet;
use std::iter::FromIterator;

#[derive(Logos, Debug, PartialEq)]
enum Token {
    #[token("F")]
    Front,
    #[token("B")]
    Back,
    #[token("L")]
    Left,
    #[token("R")]
    Right,
    #[token("\n")]
    Delimiter,
    #[error]
    #[regex("[\n ]", logos::skip)]
    Error,
}

fn parse_pass(tokens: &[Token]) -> (i64, i64)
{
    let mut upper = 128;
    let mut lower = 0;

    let mut left = 0;
    let mut right = 8;

    let mut final_row = -1;
    let mut final_col = -1;

    for token in tokens {
        let ul = upper - lower;
        let rl = right - left;

        match token {
            Front => upper -= ul / 2,
            Back => lower += ul / 2,
            Left => right -= rl / 2,
            Right => left += rl / 2,
            _ => {}
        }

        if ul == 1 && token == &Front { final_row = lower } else { final_row = upper }
        if rl == 1 && token == &Left { final_col = left } else { final_col = right }
    }
    return (final_row - 1, final_col - 1);
}

fn main()
{
    let input = include_str!("input_day5.txt");
    let tokens: Vec<Token> = Token::lexer(input).collect();
    let boarding_passes: Vec<(i64, i64)> = tokens
        .split(|x| x == &Token::Delimiter)
        .into_iter()
        .map(parse_pass)
        .collect();


    let max = boarding_passes.iter().map(|(r, c)| r * 8 + c).min().unwrap();
    let min = boarding_passes.iter().map(|(r, c)| r * 8 + c).max().unwrap();
    let mut test: Vec<i64> = boarding_passes.iter().filter(|(r, c)| r != &0 && r != &127).map(|(r, c)| r * 8 + c).collect();
    test.sort();

    let mut candidates: HashSet<i64> = HashSet::from_iter(55i64..906i64);


    for seat_id in test {
        candidates.remove(&seat_id);
    }
    println!("Part 1 {}", max);
    for i in candidates {
        println!("Part 2 {}", i)
    }
}