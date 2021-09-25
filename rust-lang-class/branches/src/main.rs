fn main() {
}

fn multi_branches() {
    let number = 9;

    if number % 4 == 0 {
        println!("number divisible by 4");
    } else if number % 3 == 0 {
        println!("number divisible by 3");
    } else if number % 2 == 0 {
        println!("number divisible by 2");
    } else {
        println!("number not divisible by 2, 3, or 4")
    }
}

fn cond_in_let() {
    let condition = false;
    let number = if condition { 5 } else { 6 };

    println!("the value of the number is: {}", number);
}

fn retun_val_from_loop() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    println!("the result is {}", result);
}

fn cond_w_while() {
    let mut number = 3;

    while number != 0 {
        println!("{}!", number);

        number -= 1;
    }

    println!("LIFTOFF!!!");
}

fn collection_loop_w_for() {
    let a = [10, 20, 30, 40, 50];
    let mut index = 0;

    while index < 5 {
        println!("the value is: {}", a[index]);

        index += 1;
    }
}

fn for_iter() {
    let a = [10, 20, 30, 40, 50];

    for element in a.iter() {
        println!("the (iterated)value is: {}", element);
    }
}

fn for_cntdwn() {
    for number in (1..4).rev() {
        println!("{}!", number);
    }
    println!("LIFTOFF!!!");
}
