use std::fs::File;
use std::io::{self, BufRead};

struct Directions {
    right: usize,
    down: usize,
}

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
    let mut dir_vec: Vec<Directions> = Vec::new();
    let mut hit_vec: Vec<usize> = Vec::new();
    let mut map: Vec<Vec<char>> = Vec::new();
    let tree_prod: usize;

    for line in reader.lines() {
        let line = line?;
        let chars: Vec<char> = line.chars().collect();
        map.push(chars);
    }

    dir_vec.push(Directions{right: 1, down: 1});
    dir_vec.push(Directions{right: 3, down: 1});
    dir_vec.push(Directions{right: 5, down: 1});
    dir_vec.push(Directions{right: 7, down: 1});
    dir_vec.push(Directions{right: 1, down: 2});

    for dir in dir_vec {
        hit_vec.push(count_trees(&map, dir.right, dir.down));
    }

    tree_prod = hit_vec.iter().product();

    println!("Encountered trees: {}", tree_prod);

    Ok(())
}
