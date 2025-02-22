pub fn factorial(n: u32) -> Result<u32,String> {
    if n < 0 {
        return Err("Negative numbers are not allowed".to_string());
    }
    if n == 0 {
        return Ok(1);
    }
    return Ok(n * factorial(n - 1).unwrap());
}
