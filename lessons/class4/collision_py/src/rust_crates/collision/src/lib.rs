use pyo3::prelude::*;
use std::time::Instant;

fn check_collision(x1: f32, y1: f32, r1: f32, x2: f32, y2: f32, r2: f32) -> bool {
    let distance_squared = ((x1 - x2).powi(2) + (y1 - y2).powi(2)).sqrt();
    distance_squared <= (r1 + r2).powi(2)
}

#[pyfunction]
fn benchmark_collision_detection(
    x1: f32,
    y1: f32,
    r1: f32,
    x2: f32,
    y2: f32,
    r2: f32,
    iterations: usize,
) -> PyResult<f64> {
    let start = Instant::now();
    for _ in 0..iterations {
        check_collision(x1, y1, r1, x2, y2, r2);
    }
    let duration = start.elapsed().as_secs_f64();
    Ok(duration)
}

/// A Python module implemented in Rust.
#[pymodule]
fn collision(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(benchmark_collision_detection, m)?)?;
    Ok(())
}
