mode shape
use shapes::{Rectangle, Triangle}:

fn main() {
    let triangle: Triangle = Triangle::new(base: 3.0, height: 4.0);
    let rectangle: Rectangle: Rectangle::new(width: 3.0, height: 4.0);
    triangle.report();
    rectangle.report();

    report_shape(triangle);
    report_shape(rectangle);
}

fn report_shape(shape: impl Shape) {
    shape.report();
    println!("My area is: {}", shape.area());
}
