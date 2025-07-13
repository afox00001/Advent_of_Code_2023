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

fn get_color(line: &str, color: &str) -> i32 {
    for pick in line.split(';') {
        for color_segment in pick.split(", ") {
            if color_segment.contains(color) {
                let number_of_said_colors: Option<i32> = color_segment
                    .split(color)
                    .nth(0)
                    .map(|s| s.trim())
                    .and_then(|s| s.parse::<i32>().ok());

                if let Some(number) = number_of_said_colors {
                    return number;
                } else {
                    println!("Failed to parse number from '{}'", color_segment);
                }
            }
        }
    }

    0 // Default fallback if color not found or parse failed
}

fn main() {
    if let Ok(lines) = read_lines(FILE_PATH) {
        let mut sum: i32 = 0;
        for line in lines.map_while(Result::ok) {
            let games = line.split(";");

            let mut red_cubes: i32;
            let mut blue_cubes: i32;
            let mut green_cubes: i32;

            let mut max_red_cubes: i32 = 1;
            let mut max_blue_cubes: i32 = 1;
            let mut max_green_cubes: i32 = 1;

            for game in games {
                let mut formated_game_str: &str = game;
                if formated_game_str.contains("Game") {
                    formated_game_str = game.split(":").nth(1).unwrap();
                }
                red_cubes = get_color(formated_game_str, "red");
                blue_cubes = get_color(formated_game_str, "blue");
                green_cubes = get_color(formated_game_str, "green");

                if red_cubes > max_red_cubes {
                    max_red_cubes = red_cubes;
                }
                if blue_cubes > max_blue_cubes {
                    max_blue_cubes = blue_cubes;
                }
                if green_cubes > max_green_cubes {
                    max_green_cubes = green_cubes;
                }
            }
            let product: i32 = max_red_cubes * max_blue_cubes * max_green_cubes;
            sum += product;
        }
        println!("Sum: {}", sum);
    } else {
        println!("Failed to read lines from file '{}'", FILE_PATH);
    }
    stdin().read_line(&mut String::new()).unwrap(); //stop the program from instantly closing
}