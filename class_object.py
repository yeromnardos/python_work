class Gari:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def describe_gari(self):
        return f"{self.model} {self.year} {self.make}"

    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it"

    def update_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You cant roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


mycar = Gari("toyota", "vits", "2020")
print(mycar.describe_gari())
print(mycar.read_odometer())
mycar.update_odometer(100)
print(mycar.read_odometer())
mycar.increment_odometer(50)
print(mycar.read_odometer())
