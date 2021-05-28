class Passport:

    def __init__(self, id, series):
        self.id = id
        self.series = series


class Citizen:

    def __init__(self, name: str, country: str, passport: Passport):
        self.name = name
        self.country = country
        self._passport = passport

    def __str__(self):
        return f"{self.country}-{self.name}"

    def __repr__(self):
        return f"{self.country}-{self.name}"

    def get_passport_data(self):
        return f"{self.name} {self._passport.id} {self._passport.series}"


class Country:

    def __init__(self, citizens: list):
        self._citizens = citizens

    @property
    def citizens(self):
        return self._citizens

    @citizens.setter
    def citizens(self, person: Citizen):
        if person.country == "Kyrgyz":
            print("Kyrgyz can't get citizenship")
        else:
            self._citizens.append(person)


r_passport = Passport("1", "russian")
r_passport2 = Passport("2", "russian")
k_passport = Passport("3", "kyrgyz")

russian = Citizen("Andrei", "Russia", r_passport)
russian2 = Citizen("Dmitriy", "Russia", r_passport2)
kyrgyz = Citizen("Kadyr", "Kyrgyz", k_passport)
country = Country([])
print(russian.get_passport_data())

country.citizens = kyrgyz
print(country.citizens)

country.citizens = russian2
print(country.citizens)

country.citizens = russian
print(country.citizens)