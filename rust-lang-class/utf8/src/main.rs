use std::{char::decode_utf16, fmt::Display};
fn main() {
    internal_rep();
}

fn internal_rep() {
    let hello = String::from("Здравствуйте");
    println!("{}", hello.len());

    //let char_hello = hello.chars();

    for c in hello.scalar_val() {
        println!("{}", c);
    }
}

fn intro() {

    let mut s = String::new();

    let addition = "bar";

    s.push_str("blah blah");

    println!("{}", s);

    s.push_str(addition);

    println!("{}", s);

    println!("{}", addition);

    s.push('&');

    println!("{}", s);
}
