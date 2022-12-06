///For example, suppose you receive the following datastream buffer:
//
// mjqjpqmgbljsphdztnvjfqwrcgsmlb
//
// After the first three characters (mjq) have been received, there haven't been enough characters received yet to find the marker. The first time a marker could occur is after the fourth character is received, making the most recent four characters mjqj. Because j is repeated, this isn't a marker.
//
// The first time a marker appears is after the seventh character arrives. Once it does, the last four characters received are jpqm, which are all different. In this case, your subroutine should report the value 7, because the first start-of-packet marker is complete after 7 characters have been processed.
//
// Here are a few more examples:
//
//     bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
//     nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
//     nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
//     zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11
//
// How many characters need to be processed before the first start-of-packet marker is detected?


const INPUT: &str = include_str!("input.txt");

struct Stream {
    buffer: Vec<char>,
    marker: Option<usize>,
}

impl Stream {
    fn new(v: Vec<char>) -> Stream {
        let mut stream = Stream {
            buffer: v,
            marker: None,
        };
        stream.marker = stream.find_marker();
        stream
    }

    fn find_marker(&self) -> Option<usize> {
        let mut marker = None;

        // Iterate through a window of 4 characters
        for (idx, window) in self.buffer.windows(4).enumerate() {
            // Check if the window elements are all unique
            if window.iter().all(|&c| window.iter().filter(|&c2| c == *c2).count() == 1) {
                // If so, we have found a marker
                marker = Some(idx + 4);
                break;
            }
        }
        marker
    }

    // A start message marker is the same as a normal marker, but contains 14 characters instead of 4
    fn find_start_message(&self) -> Option<usize> {
        let mut marker = None;

        // Iterate through a window of 14 characters
        for (idx, window) in self.buffer.windows(14).enumerate() {
            // Check if the window elements are all unique
            if window.iter().all(|&c| window.iter().filter(|&c2| c == *c2).count() == 1) {
                // If so, we have found a marker
                marker = Some(idx + 14);
                break;
            }
        }
        marker
    }
}

fn main() {
    // Part 1, print the first marker.
    let stream = Stream::new(INPUT.chars().collect());
    println!("First marker: {:?}", stream.marker);

    // Part 2, print the first start message marker.
    println!("First start message: {:?}", stream.find_start_message());
}

// Here are a few more examples:
//
//     bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
//     nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
//     nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
//     zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11

// Add tests
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_find_marker() {
        let stream = Stream::new("bvwbjplbgvbhsrlpgdmjqwftvncz".chars().collect());
        assert_eq!(stream.find_marker(), Some(5));
        let stream = Stream::new("nppdvjthqldpwncqszvftbrmjlhg".chars().collect());
        assert_eq!(stream.find_marker(), Some(6));
        let stream = Stream::new("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg".chars().collect());
        assert_eq!(stream.find_marker(), Some(10));
        let stream = Stream::new("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw".chars().collect());
        assert_eq!(stream.find_marker(), Some(11));
    }
}