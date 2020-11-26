class First_try:

    def __init__(self, number_a, number_b):
        self.num_a = number_a
        self.num_b = number_b

    def __str__(self):
        return "I am a dummy calculator"

    def add(self):
        """
        comments here
        """
        return self.num_a + self.num_b

    def sub(self):
        """
        Take this self.

        :returns: number
        """
        return self.num_a - self.num_b

    def mul(self):
        """
        :type: string
        """
        return self.num_a * self.num_b

    def div(self):
        """
        :param: isitok
        """
        return self.num_a / self.num_b


if __name__ == "__main__":
    calc1 = First_try(5, 3)
    calc1.add()
