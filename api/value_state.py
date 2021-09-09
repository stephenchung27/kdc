class ValueState:
    # TODO: Change the name of the class to something more semantic

    def __init__(self, fuel=100, food=50, drink=50, entertainment=75, time=100):
        self.fuel = fuel
        self.food = food
        self.drink = drink
        self.entertainment = entertainment
        self.time = time

    def calculate_action(self, action):
        self.fuel = min(100, self.fuel + action.fuel)
        self.food = min(100, self.food + action.food)
        self.drink = min(100, self.drink + action.drink)
        self.entertainment = min(100, self.entertainment + action.entertainment)
        self.time -= 4

    @property
    def total_value(self):
        return self.food + self.drink + self.entertainment

    @property
    def valid(self):
        return (self.fuel > 0 and
                self.food > 0 and
                self.drink > 0 and
                self.entertainment > 0)

    def __eq__(self, other):
        return self.total_value == other.total_value

    def __lt__(self, other):
        return self.total_value < other.total_value

    def __str__(self):
        return "Fuel: {}, Food: {}, Drink: {}, Entertainment: {}, Time: {}".format(
            self.fuel, self.food, self.drink, self.entertainment, self.time
        )

    def __dict__(self):
        return {
            "fuel": self.fuel,
            "food": self.food,
            "drink": self.drink,
            "entertainment": self.entertainment,
            "time": self.time,
        }
