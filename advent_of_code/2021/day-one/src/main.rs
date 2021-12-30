use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    // File hosts must exist in current path before this produces output
    if let Ok(lines) = read_lines("input.txt") {
        // Consumes the iterator, returns an (Optional) String
        let mut count: i32 = 0;
        let mut previous: Option<i32> = None;
        for line in lines {
            
            if let Ok(ip) = line {
                let parsed: i32 = ip.parse().unwrap();
                if let Some(number) = previous { 
                    if parsed > number {
                        count += 1;
                    }
                }
                previous = Some(parsed);
            }
        }
        println!("{}", count);
    }
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}