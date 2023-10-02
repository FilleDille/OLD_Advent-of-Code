use std::fs;

struct Rectangle {
    length: u32,
    width: u32,
    height: u32,
    area_array: [u32; 3],
    side_array: [u32; 3],
}

trait PaperWrapping {
    fn smallest_area(&self) -> u32;
    fn create_area_array(&mut self);
    fn create_side_array(&mut self);
    fn get_surface_area(&self) -> u32;
}

impl PaperWrapping for Rectangle {
    fn smallest_area(&self) -> u32 {
        let min_option = self.area_array.iter().min();

        match min_option {
            Some(min) => *min,
            None => 0
        }
    }

    fn create_area_array(&mut self) {
        let array: [u32; 3] = [
            self.length * self.width,
            self.length * self.height,
            self.width * self.height
        ];

        self.area_array = array;
    }

    fn create_side_array(&mut self) {
        let array: [u32; 3] = [
            self.length,
            self.width,
            self.height
        ];

        self.side_array = array;
    }

    fn get_surface_area(&self) -> u32 {
        self.area_array.iter().map(|val|2*val).sum()
    }
}

impl Rectangle {
    fn new(length: u32, width: u32, height: u32) -> Self {
        let mut rectangle = Rectangle {
            length,
            width,
            height,
            area_array: [0; 3],
            side_array: [0; 3],
        };
        rectangle.create_area_array();
        rectangle.create_side_array();
        rectangle
    }
}

fn read_input(input_path: &str) -> String {
    fs::read_to_string(input_path).unwrap()
}

pub fn process_part_1() -> String {
    let input = read_input("input.txt");
    let input_vec: Vec<&str>  = input.split('\n').collect();
    let mut total_paper: u32 = 0;

    for row in input_vec.iter() {
        let split_row: Vec<u32> = row
            .split('x')
            .filter(|&line| !line.is_empty())
            .map(|line| line.parse::<u32>().unwrap())
            .collect();
        let temp_struct = Rectangle::new(
            split_row[0],
            split_row[1],
            split_row[2]
        );
        let smallest_area: u32 = temp_struct.smallest_area();
        let surface_area: u32 = temp_struct.get_surface_area();
        let required_area: u32 = smallest_area + surface_area;
        total_paper += required_area;
    }

    total_paper.to_string()
}

pub fn process_part_2() -> String {
    let input = read_input("input.txt");
    let input_vec: Vec<&str>  = input.split('\n').collect();
    let mut total_ribbon: u32 = 0;

    for row in input_vec.iter() {
        let split_row: Vec<u32> = row
            .split('x')
            .filter(|&line| !line.is_empty())
            .map(|line| line.parse::<u32>().unwrap())
            .collect();
        let temp_struct = Rectangle::new(
            split_row[0],
            split_row[1],
            split_row[2]
        );
        let mut side_array_clone = temp_struct.side_array.clone();
        side_array_clone.sort();
        let smallest_two_sides: [u32; 2] = [side_array_clone[0], side_array_clone[1]];
        let ribbon_around: u32 = smallest_two_sides.iter().cloned().sum::<u32>() * 2;
        let ribbon_bow_tie: u32 = temp_struct.side_array.iter().product();

        total_ribbon += ribbon_around + ribbon_bow_tie;
    }

    total_ribbon.to_string()
}
