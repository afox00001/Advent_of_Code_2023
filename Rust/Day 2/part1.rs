use std::fs::File;
use std::io::stdin;
use std::io::BufReader;
use std::io::Lines;
use std::io::{self, BufRead};
use std::path::Path;

const FILE_PATH: &str = "input.txt";
const MAX_RED_CUBES: i32 = 12;
const MAX_BLUE_CUBES: i32 = 14;
const MAX_GREEN_CUBES: i32 = 13;
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
                let number_of_said_colors = color_segment
                    .split(color)
                    .nth(0)
                    .map(|s| s.trim()) // removes spaces around
                    .and_then(|s| s.parse::<i32>().ok());

                if let Some(number) = number_of_said_colors {
                    //println!("{} {}", color_segment, number);
                    return number;
                } else {
                    println!("Failed to parse number from '{}'", color_segment);
                }
            }
        }
    }

    0 // Default fallback if color not found or parse failed
}

fn is_game_possible(red_cubes: i32, blue_cubes: i32, green_cubes: i32) -> bool {
    red_cubes <= MAX_RED_CUBES && blue_cubes <= MAX_BLUE_CUBES && green_cubes <= MAX_GREEN_CUBES
}

fn main() {
    if let Ok(lines) = read_lines(FILE_PATH) {
        let mut sum: i32 = 0;
        for line in lines.map_while(Result::ok) {
            let mut game_id = 0;
            let games = line.split(";");

            let mut red_cubes: i32;
            let mut blue_cubes: i32;
            let mut green_cubes: i32;

            let mut is_possible: bool = true;
            for game in games {
                let mut formated_game_str: &str = game;
                if formated_game_str.contains("Game") {
                    game_id = game
                        .split("Game ")
                        .nth(1)
                        .unwrap()
                        .split(":")
                        .nth(0)
                        .unwrap()
                        .parse::<i32>()
                        .unwrap();
                    formated_game_str = game.split(":").nth(1).unwrap();
                }
                red_cubes = get_color(formated_game_str, "red");
                blue_cubes = get_color(formated_game_str, "blue");
                green_cubes = get_color(formated_game_str, "green");
                if !is_game_possible(red_cubes, blue_cubes, green_cubes) {
                    is_possible = false;
                }
            }
            if is_possible {
                sum += game_id;
            }
        }
        println!("Sum: {}", sum);
    }
    stdin().read_line(&mut String::new()).unwrap(); //stop the program from instantly closing
}