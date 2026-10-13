class Mobile:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def make_call(self, minutes):
        
        if self.battery >= minutes:
            self.battery -= minutes
            print(f"{self.brand} {self.model}: Call ki gayi {minutes} minutes tak.")
            print(f"Remaining Battery: {self.battery}%")
        else:
            print(f"{self.brand} {self.model}: Battery low hai, call nahi ho sakti!")

    def charge(self, amount):
        self.battery += amount
        if self.battery > 100:
            self.battery = 100
        print(f"{self.brand} {self.model}: Charging ke baad battery {self.battery}% ho gayi.")

    def show_info(self):
        print(f"Phone: {self.brand} {self.model} | Battery: {self.battery}%")



if __name__ == "__main__":
    
    my_phone = Mobile("Samsung", "S23", 50)

    
    my_phone.show_info()


    my_phone.make_call(15)

    
    my_phone.charge(30)