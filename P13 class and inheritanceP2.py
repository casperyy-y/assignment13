class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def discount_price(self):
        return self.sticker_price * 0.90  # 90% of sticker price

    def display_info(self):
        return f"Car: {self.make} {self.model}, Sticker Price: ${self.sticker_price:,.2f}, Discount Price: ${self.discount_price():,.2f}"

class Sport(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = False
        self.sport_engine = False
        self.sport_interior = False

    def add_sport_wheels(self):
        self.sport_wheels = True

    def add_sport_engine(self):
        self.sport_engine = True

    def add_sport_interior(self):
        self.sport_interior = True

    def price_with_options(self):
        total_price = self.discount_price()
        if self.sport_wheels:
            total_price += 1000
        if self.sport_engine:
            total_price += 3000
        if self.sport_interior:
            total_price += 2000
        return total_price

    def display_info(self):
        options = []
        if self.sport_wheels:
            options.append("Sport Wheels")
        if self.sport_engine:
            options.append("Sport Engine")
        if self.sport_interior:
            options.append("Sport Interior")
        
        options_str = ", ".join(options) if options else "None"
        return f"Sport Car: {self.make} {self.model}, Base Price: ${self.discount_price():,.2f}, Options: {options_str}, Total Price: ${self.price_with_options():,.2f}"

sport_car = Sport("Porsche", "911", 120000)
sport_car.add_sport_wheels()
sport_car.add_sport_engine()
print(sport_car.display_info())
