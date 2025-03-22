pub fn mean(data: &Vec<i32>) -> f64 {
    let sum: i32 = data.iter().sum();
    sum as f64 / data.len() as f64
}

pub fn median(data: &Vec<i32>) -> f64 {
    let mut data = data.clone();
    data.sort();
    let len = data.len();
    if len % 2 == 0 {
        (data[len / 2] + data[len / 2 - 1]) as f64 / 2.0
    } else {
        data[len / 2] as f64
    }
}

pub fn variance(data: &Vec<i32>) -> f64 {
    let mean = mean(data);
    let sum: f64 = data.iter().map(|x| (*x as f64 - mean).powi(2)).sum();
    sum / data.len() as f64
}

pub fn mode(data: &Vec<i32>) -> i32 {
    let mut map = HashMap::new();
    for &x in data.iter() {
        let count = map.entry(x).or_insert(0);
        *count += 1;
    }
    let mut max = 0;
    let mut mode = 0;
    for (&key, &val) in map.iter() {
        if val > max {
            max = val;
            mode = key;
        }
    }
    mode
}