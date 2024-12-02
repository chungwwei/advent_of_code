use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};

fn main() {
    let file_path = "input.txt";

    let (mut list_a, mut list_b) = match parse_lines(file_path) {
        Ok((a, b)) => (a, b),
        Err(e) => {
            eprintln!("Error reading file: {}", e);
            return;
        }
    };
    // part one
    let part_one = f(&mut list_a, &mut list_b);
    println!("part one: {}", part_one);

    // part two
    let part_two = f2(&mut list_a, &mut list_b);
    println!("part two: {}", part_two);
}

fn f(list_a: &mut Vec<i32>, list_b: &mut Vec<i32>) -> i32 {
    list_a.sort_by(|a, b| a.cmp(b));
    list_b.sort_by(|a, b| a.cmp(b));
    let mut total = 0;
    for (a, b) in list_a.iter().zip(list_b.iter()) {
        let diff = (a - b).abs();
        total += diff;
    }
    total
}

fn f2(list_a: &mut Vec<i32>, list_b: &mut Vec<i32>) -> i32 {
    let mut freq: HashMap<i32, i32> = HashMap::new();
    for num in list_b.iter() {
        *freq.entry(*num).or_insert(0) += 1;
    }

    let mut total = 0;
    for num in list_a.iter() {
        if let Some(&count) = freq.get(num) {
            total += num * count;
        }
    }
    total
}

fn parse_lines(filename: &str) -> io::Result<(Vec<i32>, Vec<i32>)> {
    let file = File::open(filename)?;
    let reader = io::BufReader::new(file);

    let mut list_a = Vec::new();
    let mut list_b = Vec::new();

    reader
        .lines()
        .filter_map(|line| line.ok()) // Filter out lines with errors
        .map(|content| {
            let words: Vec<&str> = content.split_whitespace().collect();
            if words.len() >= 2 {
                Some((words[0].parse::<i32>(), words[1].parse::<i32>()))
            } else {
                None
            }
        })
        .map(|pair| pair.unwrap())
        .filter(|(num1, num2)| num1.is_ok() && num2.is_ok())
        .for_each(|(num1, num2)| {
            list_a.push(num1.unwrap());
            list_b.push(num2.unwrap());
        });

    Ok((list_a, list_b))
}
