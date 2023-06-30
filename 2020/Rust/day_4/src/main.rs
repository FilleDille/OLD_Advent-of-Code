use std::fs::File;
use std::io::{BufRead, BufReader};
use std::io;

fn main() -> io::Result<()> {
    let file = File::open("input_4.txt")?;
    let reader = BufReader::new(file);
    let mut content = String::new();
    let mut formatted_input: Vec<String> = Vec::new();

    for line in reader.lines() {
        content.push_str(&line?.trim());
        content.push('\n');
    }

    content.pop(); // due to content.push('\n') on the last line

    let split_lines: Vec<&str> = content.split("\n\n").collect();

    for line in split_lines {
        let temp_line = line.replace('\n', " ");
        formatted_input.push(temp_line);
    }

    part_1(formatted_input);

    Ok(())
}

fn part_1(formatted_input: Vec<String>) {
    let mut counter: u16 = 0;

    for line in formatted_input {
        let attr_vec: Vec<&str> = line.split(" ").collect();

        if attr_vec.len() == 8 {
            counter += 1;
        }

        if attr_vec.len() == 7 && !line.contains("cid") {
            counter += 1;
            }
        }

    println!("Number of valid passports: {counter}");
}
