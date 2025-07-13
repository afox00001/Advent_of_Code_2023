use std::collections::HashSet;
use std::fs::File;
use std::io::stdin;
use std::io::BufReader;
use std::io::Lines;
use std::io::{self, BufRead};
use std::path::Path;
use std::str::SplitWhitespace;

const FILE_PATH: &str = "input.txt";
fn read_lines<P>(filename: P) -> io::Result<Lines<BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file: File = File::open(filename)?;
    Ok(BufReader::new(file).lines())
}

fn main() {
    let mut sum: i32 = 0;
    if let Ok(lines) = read_lines(FILE_PATH) {
        for line in lines.map_while(Result::ok) {
            let mut current_points_total: i32 = 0;
            let parts: Vec<&str> = line.split('|').collect();
            let winning_numbers: HashSet<&str> = parts[1].split_whitespace().collect();
            let ticket_numbers: SplitWhitespace = parts[0].split_whitespace();
            for ticket_number in ticket_numbers {
                if !winning_numbers.contains(ticket_number) {
                    continue;
                }
                if current_points_total == 0 {
                    current_points_total = 1;
                } else {
                    current_points_total *= 2;
                }
            }
            sum += current_points_total;
        }
        println!("Sum of Points: {}", sum);
    }
    stdin().read_line(&mut String::new()).unwrap(); //stop the program from instantly closing
}