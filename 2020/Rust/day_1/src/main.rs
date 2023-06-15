use std::fs::File;
use std::io::prelude::*;
use std::time::Instant;

fn main() -> std::io::Result<()> {
    let t0 = Instant::now();

    let mut file = File::open("input.txt")?;
    let mut contents = String::new();

    file.read_to_string(&mut contents)?;

    let lines_str: Vec<&str> = contents.split('\n').collect();
    let lines_int: Vec<i32> = lines_str.iter()
        .filter(|&&line| !line.is_empty())
        .map(|line| line.parse::<i32>().unwrap())
        .collect();

    for number in &lines_int {
        let missing_number = 2020 - number;
        if lines_int.contains(&missing_number) {
            let prod = number * missing_number;
            println!("{number} * {missing_number} = {prod}");
            break;
        }
    }

    let duration = t0.elapsed();
    println!("Elapsed time: {:?}", duration);

    Ok(())
}