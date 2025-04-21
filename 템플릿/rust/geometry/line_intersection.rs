fn line_numbers() -> Vec<i128> {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect()
}

struct P {
    x: i128,
    y: i128,
}

fn ccw(a: &P, b: &P, c: &P) -> i128 {
    (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
}

fn is_intersect(a: &P, b: &P, c: &P, d: &P) -> bool {
    ccw(a, b, c) * ccw(a, b, d) < 0 && ccw(c, d, a) * ccw(c, d, b) < 0
}

fn main() {
    // std::fs::File::open("geometry/input.txt").map(|f| std::io::BufReader::new(f).lines());
    let line = line_numbers();
    let a = P { x: line[0], y: line[1] };
    let b = P { x: line[2], y: line[3] };
    let line = line_numbers();
    let c = P { x: line[0], y: line[1] };
    let d = P { x: line[2], y: line[3] };
    
    println!("{}", if is_intersect(&a, &b, &c, &d) { 1 } else { 0 });
} 