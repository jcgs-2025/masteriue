fn book_example(t: f64, x: Vec<f64>) -> Vec<f64> {
    let dx_dt: f64 = (1.0 - 2.0 * t) * x[0];
    vec![dx_dt]
}