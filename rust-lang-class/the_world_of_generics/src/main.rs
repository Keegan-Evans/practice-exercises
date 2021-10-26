// Previous Run Through.
//
//fn largest<T: PartialOrd + Copy>(list: &[T]) -> T {
//    let mut largest = list[0];
//
//    for &item in list {
//        if item > largest {
//            largest = item;
//        }
//    }
//
//    largest
//}
//
//fn largest_refed<T: std::cmp::PartialOrd>(list: &[T]) -> &T {
//    let mut largest = &list[0];
//
//    for item in list {
//        if item > largest {
//            largest = item;
//        }
//    }
//
//    largest
//}
////fn call_largest() {
////    let number_list = vec![34, 50, 25, 100, 65];
////
////    let result = largest(&number_list);
////    println!("The largest number is {}", result);
////
////    let char_list = vec!['y', 'm', 'a', 'q'];
////
////    let result = largest(&char_list);
////    println!("The largest char is {}", result);
////}
//
//struct Point<T, U> {
//    x: T,
//    y: U,
//}
//
//impl Point<f32, f32> {
//
//    fn dist_from_origin (&self) -> f32 {
//        (self.x.powi(2) + self.y.powi(2)).sqrt()
//    }
//}
//
//impl Point<i32, i32> {
//    fn dist_from_origin (&self) -> f32 {
//        let float_point = Point {
//            x: *&self.x as f32,
//            y: *&self.y as f32,
//        };
//        float_point.dist_from_origin()
//    }
//}
//
//
//
//impl<T, U> Point<T, U> {
//    fn x (&self) -> &T {
//        &self.x
//    }
//
//}
////
////
////fn ThePoint() {
////    let int = Point { x: 5, y: 10 };
////    let flt = Point { x: 1.0, y: 4.0};
////
////    let int_float = Point { x: 1.32, y: 3.75 };
////}
//
//fn main() {
//    let p = Point { x: 5, y: 10 };
//
//    println!("p.x = {}", p.x());
//
//    println!("dist from orgin = {}", p.dist_from_origin());
//
//    let _integer = Some(5);
//    let _float = Some(5.0);
//
//    println!("Largest is working:\n-----------------------");
//    let number_list = vec![34, 50, 25, 100, 65];
//
//    let result = largest(&number_list);
//    println!("The largest number is {}", result);
//
//    let char_list = vec!['y', 'm', 'a', 'q'];
//
//    let result = largest(&char_list);
//    println!("The largest char is {}", result);
//
//    let refed_result = largest_refed(&char_list);
//    println!("The largest char is {}", refed_result);
//}

// Second Time
fn main() {
    run_largest();
}

fn run_generic_largest() {
    
    let number_list = vec![34, 50, 25, 65];

    generic_largest(&number_list);
}

fn generic_largest<T>(list: &[T]) -> T {
    let mut largest = list[0];

    for &item in list.iter() {
        if item > largest {
            largest = item;
        }
    }
    largest
}

fn run_largest() {
    let number_list = vec![34, 50, 25, 65];

    largest(&number_list);

    let number_list = vec![18, 303545, 370198, 993874, 32, 42];

    largest(&number_list);
}

fn largest(list: &[i32]) -> i32 {

    let mut largest = list[0];

    for number in list {
        if number > &largest {
            largest = *number;
        }
    }

    println!("The largest number is: {}", largest);
    largest
}
