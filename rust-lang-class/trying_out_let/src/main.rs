fn main() {
    let tasty = breakfast_picker(3);
    println!("{}", tasty);
}

fn breakfast_picker(num: i32) -> String {
    if let choice = num < 0 {
        String::from("bacon")
    } else if num == 0 {
        String::from("eggs")
    } else {
        String::from("oatmeal...bleh")
    }
}
