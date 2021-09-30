#![allow(unused)]
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }
    &s[..]
}

fn main() {
    let my_string = String::from("hello world");

    let word = first_word(&my_string[0..6]);
    let word = first_word(&my_string);

    let my_string_literal = "hello, world!";
    
    //let mut s = String::from("hello world");
    //println!("{}", &s[..5]);

    //let word = first_word(&s);

    //s.clear();

    //println!("The index of the end of the first word is: {}", word);
}
