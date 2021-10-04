fn main() {
    let mut user1 = User {
        email: String::from("someone@example.com"),
        username: String::from("someuser"),
        sign_in_count: 37,
        active: false,
    };

    println!("{}'s email address is: {}", user1.username, user1.email);
    user1.email = String::from("someonesother@example.com");
    println!("{}'s email address is: {}", user1.username, user1.email);
}

fn build_user(email: String, username: String) -> User {
    User {
        email,
        username,
        active: true,
        sign_in_count: 1,
    }
}

struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}
