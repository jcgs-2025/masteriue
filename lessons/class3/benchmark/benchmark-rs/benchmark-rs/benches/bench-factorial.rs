use benchmark_rs::factorial;
use criterion::{criterion_group, criterion_main, BatchSize, BenchmarkId, Criterion};

fn factorial_benchmark(c: &mut Criterion) {
    let inputs = vec![1, 2, 4, 8, 16, 32];
    let mut group = c.benchmark_group("factorial");
    for input in inputs {
        group.bench_with_input(BenchmarkId::from_parameter(input), &input, |b, &n| {
            b.iter_batched(|| n, |n| factorial(n), BatchSize::LargeInput);
        });
    }
    group.finish();
}

criterion_group! {
    name = benches;
    config = Criterion::default().sample_size(100);
    targets = factorial_benchmark
}
criterion_main!(benches);