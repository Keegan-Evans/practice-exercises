#![allow(unused)]

fn main() {
}
fn dangling_reference_danger() {
    let reference_to_nothing = dangle();
}

fn dangle() -> &String {
    let s = String::from("hello");

    &s
}
    
fn first_use_of_ref() {
    let mut s = String::from("hello");

    let len = calculate_length(&s);

    println!("The length of '{}' is {}.", s, len);
    
    change(&mut s);

    let len = calculate_length(&s);

    println!("The length of '{}' is {}.", s, len);
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}

fn calculate_length(s: &String) -> usize {
    let length = s.len();

    length
}

fn give_and_give_and_take() {
    let s1 = gives_ownership();

    let s2 = String::from("hello");
    println!("{}", s2);

    let s3 = takes_and_gives_back(s2);

    println!("{}", s3);
}


fn gives_ownership() -> String {
    let some_string = String::from("hello");

    some_string
}


fn takes_and_gives_back(a_string: String) -> String {
    a_string
}


fn takes_ownership(some_string: String) {
    println!("{}", some_string);
}


fn makes_copy(some_integer: i32) {
    println!("{}", some_integer);
}


fn first_ownership() {
    let s = String::from("hello");

    takes_ownership(s);

    let x = 5;

    makes_copy(x);
}

// Preliminaries...

fn deep_vs_shallow() {
    let mut s1 = String::from("hello");
    let s2 = s1.clone();
    println!("s1: {}\ns2: {}", s1, s2);
}
fn basics() {
    let mut s = String::from("hello");
    s.push_str(", world!");
    println!("{}", s);
}
