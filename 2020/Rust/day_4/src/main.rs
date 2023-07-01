use std::fs::File;
use std::io::{BufRead, BufReader};
use std::io;

#[allow(non_camel_case_types)]
enum Attribute {
    byr,
    iyr,
    eyr,
    hgt,
    hcl,
    ecl,
    pid,
    cid,
    None,
}

struct PassportAttribute {
    attr: Attribute,
    val: String,
}

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

    part_2(formatted_input);

    Ok(())
}

#[allow(dead_code)]
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

#[allow(dead_code)]
fn part_2(formatted_input: Vec<String>) {
    let mut counter: u16 = 0;

    'passport_loop: for line in formatted_input {
        let attr_vec: Vec<&str> = line.split(" ").collect();
        let mut attr_counter: u8 = 0;
        let mut cid_present: bool = false;

        for attr_raw in attr_vec {
            let attr_split: Vec<&str> = attr_raw.split(":").collect();
            let attr_key: &str = &attr_split[0];
            let attr_val: &str = &attr_split[1];
            let mut passport = PassportAttribute {
                attr: Attribute::None,
                val: attr_val.to_string()
            };

            match attr_key {
                "byr" => passport.attr = Attribute::byr,
                "iyr" => passport.attr = Attribute::iyr,
                "eyr" => passport.attr = Attribute::eyr,
                "hgt" => passport.attr = Attribute::hgt,
                "hcl" => passport.attr = Attribute::hcl,
                "ecl" => passport.attr = Attribute::ecl,
                "pid" => passport.attr = Attribute::pid,
                "cid" => {
                    passport.attr = Attribute::cid;
                    cid_present = true;
                }
                _ => passport.attr = Attribute::None,
            }

            if validate_passport_attribute(&passport) == false {
                continue 'passport_loop;
            }

            attr_counter += 1;
        }

        if attr_counter == 8 {
            counter += 1;
        }

        if attr_counter == 7 && cid_present == false {
            counter += 1;
        }
    }

    println!("Number of valid passports: {counter}");
}

fn validate_passport_attribute(attribute: &PassportAttribute) -> bool {
    match attribute.attr {
        Attribute::byr => {
            if let Ok(year) = attribute.val.parse::<u32>() {
                year >= 1920 && year <= 2002
            } else {
                false
            }
        }
        Attribute::iyr => {
            if let Ok(year) = attribute.val.parse::<u32>() {
                year >= 2010 && year <= 2020
            } else {
                false
            }
        }
        Attribute::eyr => {
            if let Ok(year) = attribute.val.parse::<u32>() {
                year >= 2020 && year <= 2030
            } else {
                false
            }
        }
        Attribute::hgt => {
            if attribute.val.ends_with("cm") {
                if let Ok(height) = attribute.val[..attribute.val.len() - 2].parse::<u32>() {
                    height >= 150 && height <= 193
                } else {
                    false
                }
            } else if attribute.val.ends_with("in") {
                if let Ok(height) = attribute.val[..attribute.val.len() - 2].parse::<u32>() {
                    height >= 59 && height <= 76
                } else {
                    false
                }
            } else {
                false
            }
        }
        Attribute::hcl => {
            attribute.val.len() == 7 && &attribute.val[..1] == "#" &&
                attribute.val.chars().skip(1).all(|c| c.is_digit(16))
        }
        Attribute::ecl => {
            attribute.val == "amb" || attribute.val == "blu" || attribute.val == "brn" ||
                attribute.val == "gry" || attribute.val == "grn" || attribute.val == "hzl" ||
                attribute.val == "oth"
        }
        Attribute::pid => {
            attribute.val.len() == 9 && attribute.val.chars().all(|c| c.is_digit(10))
        }

        Attribute::cid => true,
        Attribute::None => false,
    }
}