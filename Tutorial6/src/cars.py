class Car:
    def __init__(self, speed: int, color: str):
        self.speed = speed
        self.color = color
    
    def accelerate(self, increment: int) -> None:
        self.speed += increment
    
    def __str__(self) -> str:
        return f"{self.color} car moving at {self.speed} km/h" 

    def __repr__(self) -> str:
        return f"Car(speed={self.speed}, color='{self.color}')"

my_car = Car(10, "red")
print(my_car.speed)  # Output: 10
print(my_car.color)  # Output: red
my_car.accelerate(40)
print(my_car)  # Output: red car moving at 50 km/h
another_car = Car(30, "blue")
print(repr(another_car))  # Output: Car(speed=30, color='blue')
