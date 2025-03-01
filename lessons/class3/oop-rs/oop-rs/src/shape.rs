struct Triangle {
    base: f64,
    height: f64,
}

impl Triangle {
    pub fn new(base: f64, height: f64) -> Triangle {
        Triangle { base, height }
    }
    pub fn area(&self) -> f64 {
        0.5 * self.base * self.height
    }
    pub fn report(&self) {
        println!("Triangle: base = {}, height = {}, area = {}", self.base, self.height, self.area());
    }
