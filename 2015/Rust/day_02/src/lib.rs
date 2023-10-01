use std::fs;

struct Rectangle {
    length: u32,
    width: u32,
    height: u32,
}

trait PaperWrapping {
    fn smallest_side(&self) -> u32;
    fn create_area_array(&self) -> [u32; 3];
    fn get_surface_area(&self) -> u32;
}

impl PaperWrapping for Rectangle {
    fn smallest_side(&self) -> u32 {
        let binding = self.create_area_array();
        let min_option = binding.iter().min();
        match min_option {
            Some(min) => *min,
            None => 0
        }
    }

    fn create_area_array(&self) -> [u32; 3] {
        let array: [u32; 3] = [
            self.length * self.width,
            self.length * self.height,
            self.width * self.height
        ];
        array
    }

    fn get_surface_area(&self) -> u32 {
        let binding = self.create_area_array();
        binding.iter().map(|val|2*val).sum()
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
        let temp_struct = Rectangle { length: split_row[0], width: split_row[1], height: split_row[2]};
        let smallest_side: u32 = temp_struct.smallest_side();
        let surface_area: u32 = temp_struct.get_surface_area();
        let required_area: u32 = smallest_side + surface_area;
        total_paper += required_area;
    }

    total_paper.to_string()
}
