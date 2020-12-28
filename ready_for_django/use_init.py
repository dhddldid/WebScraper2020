class Car():
    
    def __init__(self, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black") # color가 제공되지 않으면 black
        self.price = kwargs.get("price", "$20")
    # __str__ overriding
    def __str__(self):
        return f"Car with {self.wheels} wheels"   

porche = Car(color="green", price="$40")
print(porche.color, porche.price)
    

class Convertible(Car):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"
    
    def __str__(self):
            return f"Car with no roof"

myCar = Convertible(color="녹색",price="5천만원")
print(myCar.color, myCar.price)

