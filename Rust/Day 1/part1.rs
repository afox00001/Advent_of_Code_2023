use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

const FILE_PATH: &str = "input.txt";
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn main() {
    if let Ok(lines) = read_lines(FILE_PATH) {
        let mut sum: i32 = 0;

        for line in lines.map_while(Result::ok) {
            let mut first_number_str = String::new();
            let mut last_number_str = String::new();
            let mut is_first_number_in_line = true;

            for char in line.chars() {
                if char.is_ascii_digit() {
                    let char_string = char.to_string();
                    if is_first_number_in_line {
                        is_first_number_in_line = false;
                        first_number_str = char_string;
                    } else {
                        last_number_str = char_string;
                    }
                }
            }

            if last_number_str.is_empty() {
                last_number_str = first_number_str.clone();
            }

            let new_digit_as_string = format!("{}{}", first_number_str, last_number_str);
            let new_digit: i32 = new_digit_as_string.parse().unwrap();
            sum += new_digit;
        }
        println!("Sum: {}", sum);
    }
    std::io::stdin().read_line(&mut String::new()).unwrap(); //to quit the program from instantly closing
}