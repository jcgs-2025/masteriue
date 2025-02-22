
pub fn mean(left: u64, right: u64) -> u64 {
    (left + right) / 2
}

pub fn median(left: u64, right: u64) -> u64 {
    (left + right) / 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}
