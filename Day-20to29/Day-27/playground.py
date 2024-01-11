def add(*args):
    print(args[0])

    result = 0
    for n in args:
        result += n
    print(result)
    
add(1,3,2,3,5,43,2,1,3,3,4,5,5,44,3,3,2,2,1,)


def calculate(n ,**kwargs):
    print(kwargs)
    for key , value in kwargs.items():
        print(key)
        print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(0,add=8,multiply=6)

class Car:

    def __init__(self,**kw) -> None:
        self.make = kw["make"]
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan",model="GT-R")
print(my_car.model)
