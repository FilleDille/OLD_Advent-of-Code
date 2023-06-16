use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut file = File::open("input.txt")?;
    let mut contents = String::new();

    file.read_to_string(&mut contents)?;

    let lines_str: Vec<&str> = contents.split('\n').collect();
    let lines_u: Vec<u32> = lines_str.iter()
        .filter(|&&line| !line.is_empty())
        .map(|line| line.parse::<u32>().unwrap())
        .collect();

    part_2(&lines_u);

    Ok(())
}

#[allow(dead_code)]
fn part_1(lines_u: &Vec<u32>) {
    for number in lines_u {
        let missing_number_1 = 2020 - number;

        if lines_u.contains(&missing_number_1) {
            let prod = number * missing_number_1;
            println!("{number} * {missing_number_1} = {prod}");
        }
    }
}

#[allow(dead_code)]
fn part_2(lines_u: &Vec<u32>) {
    'first_loop: for number_1 in lines_u {
        let missing_number_1 = 2020 - number_1;

        let lines_u_2: Vec<u32> = lines_u.iter()
            .filter(|&nmbr| *nmbr <= missing_number_1)
            .copied()
            .collect();

        for number_2 in &lines_u_2 {
            let missing_number_2 = missing_number_1 - number_2;

            if lines_u_2.contains(&missing_number_2) {
                let prod = number_1 * number_2 * missing_number_2;
                println!("{number_1} * {number_2} * {missing_number_2} = {prod}");
                break 'first_loop;
            }
        }
    }
}