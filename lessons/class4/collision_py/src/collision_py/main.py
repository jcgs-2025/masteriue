import time
import collision

def benchmark_collision_detection(x1, y1, r1, x2, y2, r2, iterations = 10000):
    
    for _ in range(iterations):
        _ = ((x1 - x2)**2 + (y1 - y2)**2) < (r1 + r2)**2
        
def main():
    iterations = 1000000
    #python
    start_time = time.time()
    python_time = benchmark_collision_detection(0, 0, 10, 10, 10, 10, iterations)
    python_time = time.time() - start_time
    print(f"{iterations} iterations in Python: {python_time:.6f} seconds")
    
    #rust
    start_time = time.time()
    rust_time = collision.benchmark_collision_detection(0, 0, 10, 10, 10, 10, iterations)
    rust_time = time.time() - start_time
    print(f"{iterations} iterations in Rust: {rust_time:.6f} seconds")
    
if __name__ == "__main__":
    main()
        