pub fn solve_system<F>(f: F, y0: Vec<f64>, ti: f64, tf: f64, h: f64) -> (Vec<f64>, Vec<Vec<f64>> )
where
    F: Fn(f64, &Vec<f64>) -> Vec<f64>,
{
    let mut t = ti;
    let mut y: Vec<f64> = y0;
    let mut t_values: Vec<f64> = vec![t];
    let mut y_values: Vec<Vec<f64>> = vec! [y.clone()]];

    while t < tf {
        for i: usize in 0..y.len() {
            y[i] = y[i] + h * f(t, &y)[i];
        }
        t = t + h;
        t_values.push(t);
        y_values.push(y.clone());
    }
    result
}