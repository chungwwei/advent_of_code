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
    let part_one = part_one(&matrix);
    println!("part one: {}", part_one);

    // part two
    let part_two = part_two(&matrix);
    println!("part two: {}", part_two);
}

fn part_two(matrix: &Vec<Vec<char>>) -> i32 {
    let mut cnt = 0;
    matrix.iter().enumerate().for_each(|(row_idx, row)| {
        row.iter().enumerate().for_each(|(col_idx, &char)| {
            if char == 'A' {
                let mut right = false;
                let mut left = false;

                if (row_idx > 0
                    && col_idx > 0
                    && row_idx + 1 < matrix.len()
                    && col_idx + 1 < row.len())
                    && matrix[row_idx - 1][col_idx - 1] == 'M'
                    && matrix[row_idx + 1][col_idx + 1] == 'S'
                {
                    right = true;
                }

                if (row_idx > 0
                    && col_idx + 1 < row.len()
                    && row_idx + 1 < matrix.len()
                    && col_idx > 0)
                    && matrix[row_idx - 1][col_idx + 1] == 'M'
                    && matrix[row_idx + 1][col_idx - 1] == 'S'
                {
                    left = true;
                }

                if (row_idx > 0
                    && col_idx > 0
                    && row_idx + 1 < matrix.len()
                    && col_idx + 1 < row.len())
                    && matrix[row_idx - 1][col_idx - 1] == 'S'
                    && matrix[row_idx + 1][col_idx + 1] == 'M'
                {
                    right = true;
                }

                if (row_idx > 0
                    && col_idx + 1 < row.len()
                    && row_idx + 1 < matrix.len()
                    && col_idx > 0)
                    && matrix[row_idx - 1][col_idx + 1] == 'S'
                    && matrix[row_idx + 1][col_idx - 1] == 'M'
                {
                    left = true;
                }

                if left && right {
                    cnt += 1;
                }
            }
        });
    });

    return cnt;
}

fn part_one(matrix: &Vec<Vec<char>>) -> i32 {
    let mut cnt = 0;
    let target = vec!['X', 'M', 'A', 'S'];
    let directions = vec![
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ];

    for (row_idx, row) in matrix.iter().enumerate() {
        for (col_idx, &char) in row.iter().enumerate() {
            if char == 'X' {
                for &(dx, dy) in &directions {
                    if check_word(&matrix, row_idx, col_idx, &target, dx, dy) {
                        cnt += 1;
                    }
                }
            }
        }
    }
    return cnt;
}

fn check_word(
    matrix: &Vec<Vec<char>>,
    start_row: usize,
    start_col: usize,
    target: &[char],
    dx: isize,
    dy: isize,
) -> bool {
    let rows = matrix.len();
    let cols = matrix[0].len();

    for (i, &ch) in target.iter().enumerate() {
        let new_row = start_row as isize + i as isize * dx;
        let new_col = start_col as isize + i as isize * dy;

        if new_row < 0 || new_col < 0 || new_row >= rows as isize || new_col >= cols as isize {
            return false;
        }

        if matrix[new_row as usize][new_col as usize] != ch {
            return false;
        }
    }

    true
}

fn parse_lines(filename: &str) -> io::Result<Vec<Vec<char>>> {
    let file = File::open(filename)?;
    let reader = io::BufReader::new(file);

    let matrix = reader
        .lines()
        .filter_map(|line| line.ok())
        .map(|line| line.trim().chars().collect())
        .collect();

    Ok(matrix)
}
