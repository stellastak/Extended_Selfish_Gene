class Calculator:

    def __init__(self, number_a, number_b):
        self.num_a = number_a
        self.num_b = number_b

    def __str__(self):
        return "I am a dummy calculator"

    def add(self):
        return self.num_a + self.num_b

    def sub(self):
        return self.num_a - self.num_b

    def mul(self):
        return self.num_a * self.num_b

    def div(self):
        return self.num_a / self.num_b
