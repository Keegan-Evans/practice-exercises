fn main() {
    let n_th_fib = fib(35, 0, 1);
    println!("{}", n_th_fib);
}

fn fib(n: u32, n_2: u32, n_1: u32) -> u32 {
    if n == 3 {
        n_2 + n_1
    } else {
        fib(n - 1, n_1, n_2 + n_1)
    }
}
