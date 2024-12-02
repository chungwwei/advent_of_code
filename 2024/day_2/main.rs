use std::fs::File;
use std::io::{self, BufRead};

fn main() {
    let file_path = "input.txt";

    let matrix = match parse_lines(file_path) {
        Ok(matrix) => matrix,
        Err(e) => {
            eprintln!("Error reading file: {}", e);
            return;
        }
    };
    // part one
    let part_one = matrix.iter().filter(|row| is_safe(row)).count();
    println!("part one: {}", part_one);

    // part two
    let part_two = matrix.iter().filter(|row| is_safe2(row)).count();
    println!("part one: {}", part_two);
}

fn is_safe2(list: &Vec<i32>) -> bool {
    fn is_increasing(list: &[i32]) -> bool {
        list.windows(2).all(|w| w[0] < w[1] && (w[1] - w[0]) <= 3)
    }

    fn is_decreasing(list: &[i32]) -> bool {
        list.windows(2).all(|w| w[0] > w[1] && (w[0] - w[1]) <= 3)
    }

    if is_increasing(list) || is_decreasing(list) {
        return true;
    }

    for i in 0..list.len() {
        let filtered: Vec<i32> = list
            .iter()
            .enumerate()
            .filter(|&(idx, _)| idx != i)
            .map(|(_, &val)| val)
            .collect();
        if is_increasing(&filtered) || is_decreasing(&filtered) {
            return true;
        }
    }

    false
}

fn is_safe(list: &Vec<i32>) -> bool {
    let increasing = list
        .windows(2)
        .all(|w| w[0] < w[1] && (w[1] - w[0]).abs() <= 3);
    let decreasing = list
        .windows(2)
        .all(|w| w[0] > w[1] && (w[1] - w[0]).abs() <= 3);
    return increasing || decreasing;
}

fn parse_lines(filename: &str) -> io::Result<Vec<Vec<i32>>> {
    let file = File::open(filename)?;
    let reader = io::BufReader::new(file);

    let matrix = reader
        .lines()
        .filter_map(|line| line.ok())
        .filter(|line| !line.trim().is_empty())
        .map(|line| {
            line.split_whitespace()
                .map(|num| num.parse::<i32>().unwrap())
                .collect::<Vec<i32>>()
        })
        .collect::<Vec<Vec<i32>>>();

    Ok(matrix)
}
