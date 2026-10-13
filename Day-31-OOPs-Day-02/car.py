class Car:
    def __init__(self, brand, model, fuel):
        self.brand = brand
        self.model = model
        self.fuel = fuel  

    def drive(self, distance):
        
        fuel_needed = distance / 10

        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            print(f"{self.brand} {self.model} ne {distance} km drive kiya.")
            print(f"Remaining Fuel: {self.fuel:.1f} Litres")
        else:
            print(f"{self.brand} {self.model}: Fuel kam hai, {distance} km nahi chal sakti!")

    def refuel(self, litres):
        self.fuel += litres
        print(f"{self.brand} {self.model}: {litres} Litres fuel dalwaya.")
        print(f"Total Fuel: {self.fuel:.1f} Litres")

    def show_dashboard(self):
        print(f"Car: {self.brand} {self.model} | Current Fuel: {self.fuel:.1f} Litres")



if __name__ == "__main__":
    
    my_car = Car("Toyota", "Corolla", 20)

    
    my_car.show_dashboard()


    my_car.drive(50)

    
    my_car.drive(300)

    
    my_car.refuel(15)