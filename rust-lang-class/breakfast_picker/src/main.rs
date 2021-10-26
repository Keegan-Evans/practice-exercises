fn main() {
    let bob = String::from("bob");
    let bob_stat = name_checker(&bob);

    //println!("bob: {}", bob_stat);
}

fn name_checker(name: &str) -> Result<String, String> {
    match name  {
        "" => Err("no name".to_string()),
        _ => Ok(name.to_string()),
    }
}
