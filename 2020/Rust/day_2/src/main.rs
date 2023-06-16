use std::fs::File;
use std::io::prelude::*;

#[derive(PartialEq)]
enum ValidPassword {
    Yes,
    No,
}

#[allow(dead_code)]
struct Password {
    minimum_length: u16,
    maximum_length: u16,
    key_character: char,
    password_string: String,
    valid_password: ValidPassword,
}

fn main() -> std::io::Result<()> {
    let mut file = File::open("input.txt")?;
    let mut contents = String::new();

    file.read_to_string(&mut contents)?;

    let lines_str: Vec<&str> = contents.split('\n').filter(|&line| !line.is_empty()).collect();

    part_1(&lines_str);

    Ok(())
}

#[allow(dead_code)]
fn part_1(lines_str: &Vec<&str>) {
    let mut password_array: Vec<Password> = Vec::new();

    for line in lines_str {
        let mut parts = line.split_whitespace();
        let range = parts.next().unwrap();

        let mut range_parts = range.split('-');
        let min_len: u16 = range_parts.next().unwrap().parse().unwrap();
        let max_len: u16 = range_parts.next().unwrap().parse().unwrap();
        let key_char: char = parts.next().unwrap().chars().next().unwrap();
        let password: String = parts.last().unwrap().to_string();

        let valid_pw = {
            let bytes = &password.as_bytes();
            let mut char_count: u16 = 0;

            for (_i, &item) in bytes.iter().enumerate() {
                if item == key_char as u8 {
                    char_count += 1;
                }
            }

            if min_len <= char_count && max_len >= char_count {
                ValidPassword::Yes
            } else {
                ValidPassword::No
            }
        };

        let password_struct = Password {
            minimum_length: min_len,
            maximum_length: max_len,
            key_character: key_char,
            password_string: password,
            valid_password: valid_pw,
        };

        password_array.push(password_struct);
    }

    let count_valid_pw_yes = password_array.iter()
        .filter(|password| password.valid_password == ValidPassword::Yes)
        .count();

    println!("Number of correct passwords: {count_valid_pw_yes}");

}