class Car():
    wheels = 4
    doors = 4
    windows = 4
    seats = 4

    #Method
    def start(self):
        print(self.doors)
        print("I started")


porche = Car()
porche.color="Red sexy Red"
porche.start()

print(dir(Car))