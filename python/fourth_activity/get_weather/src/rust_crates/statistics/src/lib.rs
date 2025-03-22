use pyo3::prelude::*;

#[pyfunction]
fn mean (data: Vec<f32>) -> f32 {
    let sum: f32 = data.iter().sum();
    sum / data.len() as f32
}

#[pyfunction]
fn median (data: Vec<f32>) -> f32 {
    let mut sorted_data = data.clone();
    sorted_data.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let n = sorted_data.len();
    if n % 2 == 0 {
        (sorted_data[n / 2 - 1] + sorted_data[n / 2]) / 2.0
    } else {
        sorted_data[n / 2]
    }
}

#[pyfunction]
fn standard_deviation (data: Vec<f32>) -> f32 {
    let n = data.len() as f32;
    let mean = mean(data.clone());
    let sum: f32 = data.iter().map(|x| (x - mean).powi(2)).sum();
    (sum / n).sqrt()
}
/// Export a Python module implemented in Rust.

#[pymodule]
fn statistics(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(mean, m)?)?;
    m.add_function(wrap_pyfunction!(median, m)?)?;
    m.add_function(wrap_pyfunction!(standard_deviation, m)?)?;
    Ok(())
}

