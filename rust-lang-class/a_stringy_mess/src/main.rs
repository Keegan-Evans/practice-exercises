fn main() {
    let mut s = String::new();

    println!("my variable s: {}", s);

    let data = "starting here";

    s = data.to_string();

    println!("my variable s: {}", s);

    let data = "السلام عليكم";

    s = data.to_string();

    println!("my variable s: {}", s);

    s.push_str(" eh?");

    println!("my variable s: {}", s);

    let mut s1 = String::from("foo");

    let s2 = "bar";

    s1.push_str(s2);

    println!("s2 still is {} while s1 is now {}", s2, s1);
    
}
