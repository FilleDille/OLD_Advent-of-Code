use std::fs;

trait Interpreting {
    fn interpret(&self) -> i32;
}

impl Interpreting for char {
    fn interpret(&self) -> i32 {
        if *self == '(' {
            1
        } else if *self == ')' {
            -1
        } else {
            0
        }
    }
}

fn read_input(input_path: &str) -> String {
    fs::read_to_string(input_path).unwrap()
}

pub fn process_part_1() -> String {
    let mut floor: i32 = 0;
    let input = read_input("input.txt");

    for c in input.chars() {
        floor += c.interpret();
    }

    floor.to_string()
}

pub fn process_part_2() -> String {
    let mut floor: i32 = 0;
    let input = read_input("input.txt");
    let mut floor_index: u32 = 1;

    for c in input.chars() {
        floor += c.interpret();

        if floor == -1 {
            break;
        } else {
            floor_index += 1;
        }
    }

    floor_index.to_string()
}
