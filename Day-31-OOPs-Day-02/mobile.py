class Mobile:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def make_call(self, minutes):
        # Har minute call par 1% battery kam hogi
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


# Testing the Mobile class
if __name__ == "__main__":
    # Naya phone banaya
    my_phone = Mobile("Samsung", "S23", 50)

    # Info display karna
    my_phone.show_info()

    # Call karna
    my_phone.make_call(15)

    # Phone charge karna
    my_phone.charge(30)