fn main() {
    constructing_w_tuples();
    first_way();
    ownership();
}

fn constructing_w_tuples() {
    use std::collections::HashMap;

    let teams = vec![String::from("Blue"), String::from("Yellow")];
    let initial_scores = vec![10, 50];

    let _scores: HashMap<_, _> =
        teams.into_iter().zip(initial_scores.into_iter()).collect();
}

fn first_way() {

    use std::collections::HashMap;

    let mut scores = HashMap::new();

    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);

    for (key, value) in &scores {
        println!("{}: {}", key, value);
    }

    // Overwriting
    scores.insert(String::from("Blue"), 25);

    println!("{:?}", scores);

    // Only insert if key has no value
    scores.entry(String::from("Yellow")).or_insert(55);
    scores.entry(String::from("Pink")).or_insert(75);

    println!("{:?}", scores);

    // updating based on old value
    let text = "hello world wonderful world";

    let mut map = HashMap::new();

    for word in text.split_whitespace() {
        let count = map.entry(word).or_insert(0);
        *count += 1;
    }

    println!("{:?}", map);
}

fn ownership(){
    use std::collections::HashMap;

    let field_name = String::from("Favorite color");
    let field_value = String::from("Blue");

    let mut map = HashMap::new();
    map.insert(field_name, field_value);
}
