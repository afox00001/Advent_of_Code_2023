use std::collections::HashMap;
use std::collections::VecDeque;
use std::fs::File;
use std::io::stdin;
use std::io::BufReader;
use std::io::Lines;
use std::io::{self, BufRead};
use std::path::Path;

const FILE_PATH: &str = "input.txt";
fn read_lines<P>(filename: P) -> io::Result<Lines<BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file: File = File::open(filename)?;
    Ok(BufReader::new(file).lines())
}

fn join_2_i32_into_one_i32(n1: i32, n2: i32) -> i32 {
    n1 * 10 + n2
}
fn word_to_number(word: &str) -> Option<i32> {
    let number_words: HashMap<&str, i32> = [
        ("zero", 0),
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
    ]
    .iter()
    .cloned()
    .collect();

    number_words.get(word).copied()
}

fn extract_first_and_last_number_from_line(line: String) -> (i32, i32) {
    let number_words: Vec<&str> = vec![
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    ];

    let mut buffer: VecDeque<char> = VecDeque::new();
    const MAX_WORD_LEN: usize = 5;

    let mut first_number: Option<i32> = None;
    let mut last_number: Option<i32> = None;

    for char in line.chars() {
        if char.is_ascii_digit() {
            let digit = char.to_digit(10).unwrap() as i32;
            if first_number.is_none() {
                first_number = Some(digit);
            }
            last_number = Some(digit);
        } else {
            buffer.push_back(char);
            if buffer.len() > MAX_WORD_LEN {
                buffer.pop_front();
            }

            let buffer_str: String = buffer.iter().collect();
            for &word in &number_words {
                if buffer_str.ends_with(word) {
                    if let Some(num) = word_to_number(word) {
                        if first_number.is_none() {
                            first_number = Some(num);
                        }
                        last_number = Some(num);
                        break;
                    }
                }
            }
        }
    }

    let first = first_number.unwrap_or(0);
    let last = last_number.unwrap_or(first);
    (first, last)
}

fn main() {
    if let Ok(lines) = read_lines(FILE_PATH) {
        let mut sum: i32 = 0;
        for line in lines.map_while(Result::ok) {
            let (first, last) = extract_first_and_last_number_from_line(line);
            sum += join_2_i32_into_one_i32(first, last)
        }
        println!("Sum: {}", sum);
    }
    stdin().read_line(&mut String::new()).unwrap(); //stop the program from instantly closing
}