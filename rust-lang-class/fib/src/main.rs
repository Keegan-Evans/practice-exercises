fn main() {
    fib(3);
}

fn fib(n: isize) {
    if n > 0 {
        println!("{}", n);
        fib(n - 1);
    }
}
