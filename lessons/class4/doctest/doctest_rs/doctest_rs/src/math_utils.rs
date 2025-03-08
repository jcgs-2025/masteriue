///! # Math Utils
///!
///! `math_utils` is a collection of utilities for mathematical operations.

/// #Calculate the factorial of a number
/// 
/// ## arguments:
/// * `n` - The number to calculate the factorial.
/// 

/// Returns the factorial of `n`.
///
/// # Examples
///
/// ```
/// use doctest_rs::math_utils::factorial;
///assert_eq!(factorial(0), 1);
///assert_eq!(factorial(1), 1);
///assert_eq!(factorial(2), 2);
///assert_eq!(factorial(3), 6);
///assert_eq!(factorial(4), 24);
///assert_eq!(factorial(5), 120);
/// ```
pub fn factorial(n: u64) -> u64 {
    match n {
        0 => 1,
        _ => n * factorial(n - 1),
    }
}