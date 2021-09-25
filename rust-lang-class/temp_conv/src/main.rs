fn main() {
    temp_convert(19.4, 'c')
}

fn temp_convert(temp: f32, unit: char) {
    if unit == 'c' {
        let new_temp = c_to_f(temp);
        let opposite_unit = 'f';
        display_temp(new_temp, opposite_unit);
    } else if unit == 'f' {
        let new_temp = f_to_c(temp);
        let opposite_unit = 'c';
        display_temp(new_temp, opposite_unit);
    } else {
        println!("I am sorry, I do not know how to convert from the {} unit", unit)
    }
}

fn c_to_f(temp: f32) -> f32 {
    temp * (9.0 / 5.0) + 32.0
}

fn f_to_c(temp: f32) -> f32 {
    (temp - 32.0) * (5.0 / 9.0) 
}

fn display_temp(temp: f32, unit: char) {

    println!("The temp is {} {}", temp, unit);
}
