pub trait Area {
    fn calculate_area(&self) -> f32;
}

struct Point {
    x: f32,
    y: f32,
}

struct Triangle {
    a: Point,
    b: Point,
    c: Point,
    : Option<f32>,
    ac: Option<f32>,
    bc: Option<f32>,
}

impl Triangle {
    fn distance(first_point: Point, second_point: Point) -> f32 {
        (second_point.x - first_point.x)
    }

}

impl Area for Triangle {
    fn calculate_area(&self) -> f32 {
        0.5 * 
    }
}
