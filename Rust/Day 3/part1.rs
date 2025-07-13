use std::collections::HashSet;
use std::fs::File;
use std::io::stdin;
use std::io::BufReader;
use std::io::Lines;
use std::io::{self, BufRead};
use std::path::Path;

const FILE_PATH: &str = "input.txt";
#[derive(Debug, Clone, Hash, Eq, PartialEq)]
struct TableCoordinate {
    x: usize,
    y: usize,
}

impl TableCoordinate {
    fn new(x: usize, y: usize) -> Self {
        TableCoordinate { x, y }
    }
}
fn read_lines<P>(filename: P) -> io::Result<Lines<BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file: File = File::open(filename)?;
    Ok(BufReader::new(file).lines())
}

fn is_symbol(check_str: &str) -> bool {
    const SYMBOLS: [&str; 23] = [
        "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}",
        "|", "\\", "/", ":", ";",
    ];
    SYMBOLS.contains(&check_str)
}
fn get_full_number_from_char_in_table(
    start_coord: &TableCoordinate,
    table: &[Vec<char>],
) -> String {
    let mut x: usize = start_coord.x;
    let y: usize = start_coord.y;
    let mut number = String::new();

    while x < table[y].len() && table[y][x].is_digit(10) {
        number.push(table[y][x]);
        x += 1;
    }

    number
}
fn get_number_start_coord(coord: &TableCoordinate, table: &[Vec<char>]) -> TableCoordinate {
    let mut x: usize = coord.x;
    let y: usize = coord.y;

    while x > 0 && table[y][x - 1].is_digit(10) {
        x -= 1;
    }

    TableCoordinate::new(x, y)
}

fn sum_of_parts_next_to_symbol(symbol_coordinate: TableCoordinate, table: &Vec<Vec<char>>) -> i32 {
    let directions: [(isize, isize); 8] = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ];

    let mut seen_starts: HashSet<TableCoordinate> = HashSet::new();
    let mut sum = 0;

    for (dx, dy) in directions.iter() {
        let new_x = symbol_coordinate.x as isize + dx;
        let new_y = symbol_coordinate.y as isize + dy;

        if !new_x >= 0 || !new_y >= 0 {
            continue;
        }
        let (new_x, new_y) = (new_x as usize, new_y as usize);

        if !new_y < table.len() || !new_x < table[new_y].len() {
            continue;
        }
        if !table[new_y][new_x].is_digit(10) {
            continue;
        }

        let touched_coord: TableCoordinate = TableCoordinate::new(new_x, new_y);
        let number_start: TableCoordinate = get_number_start_coord(&touched_coord, &table);
        if seen_starts.insert(number_start.clone()) {
            let num_str: String = get_full_number_from_char_in_table(&number_start, &table);
            if let Ok(num) = num_str.parse::<i32>() {
                sum += num;
            }
        }
    }
    sum
}

fn create_table(file_path: &str) -> Vec<Vec<char>> {
    let mut table: Vec<Vec<char>> = Vec::new();
    if let Ok(lines) = read_lines(file_path) {
        for line in lines.map_while(Result::ok) {
            table.push(line.chars().collect());
        }
    }
    table
}
fn main() {
    let mut sum: i32 = 0;
    let table: Vec<Vec<char>> = create_table(FILE_PATH);

    for (y, line) in table.iter().enumerate() {
        for (x, ch) in line.iter().enumerate() {
            if !is_symbol(&ch.to_string()) {
                continue;
            }
            let coord: TableCoordinate = TableCoordinate::new(x, y);
            sum += sum_of_parts_next_to_symbol(coord, &table);
        }
    }
    println!("Sum: {}", sum);
    stdin().read_line(&mut String::new()).unwrap(); //stop the program from instantly closing
}