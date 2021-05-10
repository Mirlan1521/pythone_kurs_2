class Animal:
    def __init__(self, color, sex, klass):
        self.color = color
        self.sex = sex
        self.klass = klass



class Neko(Animal):
    def __init__(self, color, sex, klass, ear_size, fur, eye_color):
        super(Neko, self).__init__(color, sex, klass)
        self.ear_size = ear_size
        self.fur = fur
        self.eye_color = eye_color

n1 = Neko("grey", "male", "рпрпрп", "fdfd", "dfdfdf", "fdfdfdf")
print(n1.color)