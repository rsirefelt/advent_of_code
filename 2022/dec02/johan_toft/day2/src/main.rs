const INPUT: &str = include_str!("testinput.txt");

enum Play {
    Rock,
    Paper,
    Scissors,
}

impl Play {
    // Implement clone
    fn clone(&self) -> Play {
        match self {
            Play::Rock => Play::Rock,
            Play::Paper => Play::Paper,
            Play::Scissors => Play::Scissors,
        }
    }
}

struct Round {
    player1: Play,
    player2: Play,
}

struct Strategy {
    // Rock paper scissors strategy guide, contains strategy for each round in a tournament.
    // Contains a vector of plays and responses for each round.
    strategy: Vec<Round>,
}

enum RoundStrategy {
    Win,
    Lose,
    Draw,
}

impl RoundStrategy
{
    fn calc_move(&self, opponent_play: Play) -> Play {
        match self {
            RoundStrategy::Win => {
                match opponent_play {
                    Play::Rock => Play::Paper,
                    Play::Paper => Play::Scissors,
                    Play::Scissors => Play::Rock,
                }
            }
            RoundStrategy::Lose => {
                match opponent_play {
                    Play::Rock => Play::Scissors,
                    Play::Paper => Play::Rock,
                    Play::Scissors => Play::Paper,
                }
            }
            RoundStrategy::Draw => opponent_play,
        }
    }
}

// The input is a strategy guide. The strategy guide contains a vector of rounds.
// For line in the input, the guide tells what play to make in each round.
// The first item on the line is the play for player 1, the second item is the play for player 2.
// Player 1 is encoded as A,B,C, player 2 is encoded as X,Y,Z.
fn parse_input(input: &str, real: bool) -> Strategy {
    let mut strategy = Strategy {
        strategy: Vec::new(),
    };
    let mut real_strategy = Strategy {
        strategy: Vec::new(),
    };

    for line in input.lines() {
        let mut round = Round {
            player1: Play::Rock,
            player2: Play::Rock,
        };

        let mut chars = line.chars();
        let player1 = chars.next().unwrap();

        // Dump whitespace
        chars.next();
        let player2 = chars.next().unwrap();

        match player1 {
            'A' => round.player1 = Play::Rock,
            'B' => round.player1 = Play::Paper,
            'C' => round.player1 = Play::Scissors,
            _ => panic!("Invalid input"),
        }

        match player2 {
            'X' => round.player2 = Play::Rock,
            'Y' => round.player2 = Play::Paper,
            'Z' => round.player2 = Play::Scissors,
            _ => panic!("Invalid input"),
        }

        // Actually the X, Y, Z means the strategy to use for the round.
        let round_strategy: RoundStrategy = match player2 {
            'X' => RoundStrategy::Lose,
            'Y' => RoundStrategy::Draw,
            'Z' => RoundStrategy::Win,
            _ => panic!("Invalid input"),
        };

        // Create new round for real strategy
        let round_real = Round {
            player1: round.player1.clone(),
            player2: round_strategy.calc_move(round.player2.clone()),
        };

        real_strategy.strategy.push(round_real);
        strategy.strategy.push(round);
    }

    return if real {
        real_strategy
    } else {
        strategy
    };
}

// Calculate the score for a strategy guide. The score for each round is calculated as follows:
// The winner of the whole tournament is the player with the highest score.
// Your total score is the sum of your scores for each round.
// The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
// plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
// You are playing as player 2 in the strategy above.
fn calculate_score(round: &Round) -> i64 {
    let mut score = 0;

    match round.player2 {
        Play::Rock => score += 1,
        Play::Paper => score += 2,
        Play::Scissors => score += 3,
    }

    match round.player1 {
        // Points are earned when player 2 wins.
        Play::Rock => {
            match round.player2 {
                Play::Paper => score += 6,
                Play::Scissors => score += 0,
                Play::Rock => score += 3,
            }
        }
        Play::Paper => {
            match round.player2 {
                Play::Paper => score += 3,
                Play::Scissors => score += 6,
                Play::Rock => score += 0,
            }
        }
        Play::Scissors => {
            match round.player2 {
                Play::Paper => score += 0,
                Play::Scissors => score += 3,
                Play::Rock => score += 6,
            }
        }
    }
    score
}

// Calculate the score for a strategy guide.
fn calculate_total_score(strategy: &Strategy) -> i64 {
    let mut total_score = 0;

    for round in &strategy.strategy {
        total_score += calculate_score(round);
    }

    total_score
}

fn main() {
    // Part 1.
    let strategy = parse_input(INPUT, false);
    println!("Total score: {}", calculate_total_score(&strategy));

    // Part 2.
    let real_strategy = parse_input(INPUT, true);
    println!("Total score: {}", calculate_total_score(&real_strategy));
}

// Add some tests
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_calculate_score() {
        assert_eq!(calculate_score(&Round::new(Play::Rock, Play::Rock)), 4);
        assert_eq!(calculate_score(&Round::new(Play::Rock, Play::Paper)), 8);
        assert_eq!(calculate_score(&Round::new(Play::Rock, Play::Scissors)), 3);
        assert_eq!(calculate_score(&Round::new(Play::Paper, Play::Rock)), 1);
        assert_eq!(calculate_score(&Round::new(Play::Paper, Play::Paper)), 5);
    }

    #[test]
    fn test_calculate_total_score() {
        let strategy = parse_input(INPUT, false);

        assert_eq!(calculate_total_score(&strategy), 12794);
    }
}
