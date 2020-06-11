use atoi::atoi;
use std::io;
use std::io::BufRead;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let input = io::stdin();
    let mut input = input.lock();

    let new_w = std::env::args().nth(1).unwrap();
    let new_w: u32 = new_w.parse()?;

    let mut buf = Vec::new();
    let mut k = 0;
    while let Ok(num) = input.read_until(b'\n', &mut buf) {
        if num == 0 {
            break;
        }
        buf.pop(); // remove \n
        for t in buf.split(|b| *b == b' ').filter(|t| !t.is_empty()) {
            let num: u8 = atoi(t).ok_or_else(|| {
                format!(
                    "failed to parse {:?} as an integer",
                    String::from_utf8_lossy(t)
                )
            })?;
            print!("{:08b}", num);
            k += 1;
            if k == new_w {
                print!("\n");
                k = 0;
            }
        }
        buf.clear();
    }
    Ok(())
}
