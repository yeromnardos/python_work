class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def onyesha(self):
        print(f"My dream car is{self.make} and my model is{self.model} manufacture in {self.year}  and is {self.color}")


myobj = Car("Toyota", "Vits", "2020", "black")
myobj.onyesha()
myobj = Car("Range", "Rover", "2013", "maroon")
myobj.onyesha()
