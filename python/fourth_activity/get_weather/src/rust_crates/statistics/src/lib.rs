use pyo3::prelude::*;
use std::time::Instant;


#[pyfunction]

"""
Calculate the mean of a list of numbers

Args:
    data (List[float]): A list of numbers

Returns:
    float: The mean of the list of numbers
"""
fn mean (data: Vec<f32>) -> f32 {
    let sum: f32 = data.iter().sum();
    sum / data.len() as f32
}

"""
Calculate the median of a list of numbers

Args:
    data (List[float]): A list of numbers

Returns:
    float: The median of the list of numbers
"""

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

"""
Calculate the standard deviation of a list of numbers

Args:
    data (List[float]): A list of numbers

Returns:
    float: The standard deviation of the list of numbers
"""

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

