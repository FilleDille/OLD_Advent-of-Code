use std::fs::File;
use std::io::{self, BufRead};

fn count_trees(map: &[Vec<char>], right: usize, down: usize) -> usize {
    let mut tree_count = 0;
    let mut x = 0;
    let mut y = 0;
    let width = map[0].len();
    let height = map.len();

    while y < height {
        if map[y][x] == '#' {
            tree_count += 1;
        }
        x = (x + right) % width;
        y += down;
    }

    tree_count
}

fn main() -> io::Result<()> {
    let file = File::open("input_3.txt")?;
    let reader = io::BufReader::new(file);

    let mut map: Vec<Vec<char>> = Vec::new();

    for line in reader.lines() {
        let line = line?;
        let chars: Vec<char> = line.chars().collect();
        map.push(chars);
    }

    let tree_count = count_trees(&map, 3, 1);
    println!("Encountered trees: {}", tree_count);

    Ok(())
}
